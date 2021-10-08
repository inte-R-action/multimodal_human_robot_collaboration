#!/usr/bin/env python3.7
# Must be run from scripts folder
# Import Statements
import pyrealsense2 as rs
import numpy as np
import traceback
import argparse
import sys, os
import time
import cv2
import matplotlib
matplotlib.use( 'tkagg' )
import matplotlib.pyplot as plt
from vision_recognition.blob_detector import detect_blobs
from vision_recognition.rs_cam import rs_cam
import imutils
from sam_custom_messages.msg import object_state
from geometry_msgs.msg import Pose 
from math import sin, cos, radians
from collections import OrderedDict
# from scipy.spatial import distance as dist

try:
    from pub_classes import diag_class, obj_class
    import rospy
    test=False
except ModuleNotFoundError:
    print(f"rospy module not found, proceeding in test mode")
    test = True
    # Hacky way of avoiding errors
    class ROS():
        def is_shutdown(self):
            return False
    rospy = ROS()

def nothing(x):
    pass
class block_detector:
    # https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
    # https://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
    def __init__(self, test, frame_id):
        # setup object message publisher
        self.test = test
        if not self.test:
            self.obj_obj = obj_class(frame_id=frame_id, names=['block'], queue=1)

        # initialize the colors dictionary, containing the color
        # name as the key and the RGB tuple as the value
        self.colours = {
            "red_1": (0, 7),
            "red_2": (165, 180),
            "green": (45, 75),
            "blue": (90, 150),
            "yellow": (15, 28),
            "orange": (7, 15)}

    def detect(self, c):
        # initialize the shape name and approximate the contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        x = y = angle = shape = None

        # if the shape has 4 vertices, it is either a square or
        # a rectangle
        if len(approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            ((x, y), (w, h), angle) = cv2.minAreaRect(approx)#cv2.boundingRect(approx)
            ar = w / float(h)
            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            shape = "square" if ar >= 0.8 and ar <= 1.2 else None

        return x, y, angle, shape

    def create_pose(self, x, y, angle, dist):

        cameraInfo = cam.depth_intrinsics
        _intrinsics = rs.intrinsics()
        _intrinsics.width = cameraInfo.width
        _intrinsics.height = cameraInfo.height
        _intrinsics.ppx = cameraInfo.ppx
        _intrinsics.ppy = cameraInfo.ppy
        _intrinsics.fx = cameraInfo.fx
        _intrinsics.fy = cameraInfo.fy
        ###_intrinsics.model = cameraInfo.distortion_model
        #_intrinsics.model  = rs.distortion.none
        #_intrinsics.coeffs = [i for i in cameraInfo.D]
        result = rs.rs2_deproject_pixel_to_point(cameraInfo, [x, y], dist)

        p = Pose()
        p.position.x = result[2]
        p.position.y = -result[0]
        p.position.z = -result[1]
        # Make sure the quaternion is valid and normalized
        angle = radians(angle+45)
        p.orientation.x = sin(angle/2) * 1
        p.orientation.y = sin(angle/2) * 0
        p.orientation.z = sin(angle/2) * 0
        p.orientation.w = cos(angle/2)

        return p

    def get_colour(self, hsv_image, c):
        try:
            # Create mask for shape contour
            mask1 = np.ones(hsv_image.shape[:2], dtype="uint8")*255
            cv2.drawContours(mask1, [c], -1, 0, -1)
            mask1 = cv2.erode(mask1, None, iterations=2)
            # mask_im = cv2.bitwise_and(hsv_image, hsv_image, mask=mask1)
            # cv2.imshow('mask1', mask1)

            # Create mask for high saturation reflections
            lower = np.array([0, 50, 0])
            upper = np.array([255, 255, 255])
            mask2 = cv2.bitwise_not(cv2.inRange(hsv_image, lower, upper))
            # s_filtered = cv2.bitwise_and(mask_im, mask_im, mask=mask2)
            # cv2.imshow('mask2', mask2)

            # Combine masks
            mask = cv2.bitwise_or(mask1, mask2)
            # cv2.imshow('masktotal', mask)

            hsv_arr = np.asarray(hsv_image)[:, :, 0]
            mask_im = np.ma.MaskedArray(hsv_arr, mask=mask)
            
            mean = int(mask_im.mean())

            for colour in self.colours:
                if mean in range(self.colours[colour][0], self.colours[colour][1]):
                    if (colour == "red_1") or (colour == "red_2"):
                        colour = "red"
                    return colour, mean
                    
        except Exception as e:
            print(e)

        return "unknown", mean

    def process_img(self, image, depth_image):
        # load the image and resize it to a smaller factor so that
        # the shapes can be approximated better
        resized = imutils.resize(image, width=300)
        ratio = image.shape[0] / float(resized.shape[0])

        # Convert to HSV format and color threshold
        # Set minimum and maximum HSV values to display
        lower = np.array([0, 50, 0])
        upper = np.array([255, 255, 255])
        hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        col_filtered = cv2.bitwise_and(resized, resized, mask=mask)
        cv2.imshow("col_filtered", col_filtered)
        # convert the resized image to grayscale, blur it slightly,
        # and threshold it
        gray = cv2.cvtColor(col_filtered, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # find contours in the thresholded image and initialize the
        # shape detector
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # loop over the contours
        for c in cnts:
            try:
                # compute the center of the contour, then detect the name of the
                # shape using only the contour
                #M = cv2.moments(c)
                #cX = int((M["m10"] / M["m00"]) * ratio)
                #cY = int((M["m01"] / M["m00"]) * ratio)
                
                # Filter out small artefacts
                area = cv2.contourArea(c)
                if area > 90:
                    x, y, angle, shape = self.detect(c)
                    if shape is not None:

                        colour, mean = self.get_colour(hsv, c)
                        obj_name = f"{colour}_small_block"

                        x = int(x*ratio)
                        y = int(y*ratio)

                        # multiply the contour (x, y)-coordinates by the resize ratio,
                        # then draw the contours and the name of the shape on the image
                        c = c.astype("float")
                        c *= ratio
                        c = c.astype("int")
                    
                        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    
                        image = cv2.circle(image, (x,y), radius=0, color=(0, 255, 0), thickness=5)
                    
                        cv2.putText(image, colour+": "+str(mean)+" area: "+str(area), (x+50, y+100), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 2)

                        dist = depth_image[x, y]
                        p = self.create_pose(x, y, angle, dist)
                        cv2.putText(image, f"{int(angle)} x:{p.position.x} y:{p.position.y} z:{p.position.z}", (x+50, y+50), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 2)

                        if not self.test:
                            # data to pass to publisher: pose, class
                            det = [p, 0, obj_name]
                            self.obj_obj.publish(det, 'dip')

                # # show the output image
                # cv2.namedWindow('detector viewer', cv2.WINDOW_AUTOSIZE)
                # cv2.imshow("detector viewer", image)
                #cv2.waitKey(0)
            except ZeroDivisionError:
                pass
            except Exception as e:
            	print(e)

def realsense_run():
    # ROS node setup
    frame_id = 'Realsense_node'
    if not test:
        rospy.init_node(frame_id, anonymous=True)
        diag_obj = diag_class(frame_id=frame_id, user_id=args.user_id, user_name=args.user_name, queue=1)
        rate = rospy.Rate(10)

    # Create block detector
    detector = block_detector(test, frame_id)

    # Get initial frames from camera
    frames = cam.pipeline.wait_for_frames()
    color_image, depth_colormap, depth_image = cam.depth_frames(frames)
    # Create a window
    cv2.namedWindow('image')

    if args.tuning_mode:
        # Create trackbars for color change
        # Hue is from 0-179 for Opencv
        cv2.createTrackbar('HMin', 'image', 0, 179, nothing)
        cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
        cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
        cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
        cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
        cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

        # Set default value for Max HSV trackbars
        cv2.setTrackbarPos('HMax', 'image', 179)
        cv2.setTrackbarPos('SMax', 'image', 255)
        cv2.setTrackbarPos('VMax', 'image', 255)

        # Initialize HSV min/max values
        hMin = sMin = vMin = hMax = sMax = vMax = 0
        phMin = psMin = pvMin = phMax = psMax = pvMax = 0

        while(1):
            # Get initial frames from camera
            frames = cam.pipeline.wait_for_frames()
            image, depth_colormap, depth_image = cam.depth_frames(frames)
            # Get current positions of all trackbars
            hMin = cv2.getTrackbarPos('HMin', 'image')
            sMin = cv2.getTrackbarPos('SMin', 'image')
            vMin = cv2.getTrackbarPos('VMin', 'image')
            hMax = cv2.getTrackbarPos('HMax', 'image')
            sMax = cv2.getTrackbarPos('SMax', 'image')
            vMax = cv2.getTrackbarPos('VMax', 'image')

            # Set minimum and maximum HSV values to display
            lower = np.array([hMin, sMin, vMin])
            upper = np.array([hMax, sMax, vMax])

            # Convert to HSV format and color threshold
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)
            result = cv2.bitwise_and(image, image, mask=mask)

            # Print if there is a change in HSV value
            if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
                print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
                phMin = hMin
                psMin = sMin
                pvMin = vMin
                phMax = hMax
                psMax = sMax
                pvMax = vMax

            # Display result image
            # cv2.imshow('image', result)
            # if cv2.waitKey(10) & 0xFF == ord('q'):
                # break

        cv2.destroyAllWindows()

    diag_timer = time.time()
    while (not rospy.is_shutdown()) or test:
        try:
            # Get frames from camera
            frames = cam.pipeline.wait_for_frames()
            color_image, depth_colormap, depth_image = cam.depth_frames(frames)

            detector.process_img(color_image, depth_image)

            if (time.time()-diag_timer) > 1:
                if not test:
                    diag_obj.publish(0, f"Running")
                diag_timer = time.time()

        except TypeError as e:
            time.sleep(1)
            if not test:
                diag_obj.publish(2, f"TypeError")
        except Exception as e:
            print("**Get Image Error**")
            if not test:
                diag_obj.publish(2, f"Realsense image error: {e}")
            traceback.print_exc(file=sys.stdout)
            break
        

        if args.disp:
            disp_im = np.hstack((color_image, depth_colormap))
            
            cv2.namedWindow('Realsense viewer', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('Realsense viewer', disp_im)
            key = cv2.waitKey(1)
            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
            
        if not test:
            rate.sleep()
        else:
            #time.sleep(1)
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run realsense vision recognition ROS node')
    parser.add_argument('--disp', '-V',
                        help='Enable displaying of camera image',
                        default=True,
                        action="store")
    parser.add_argument('--tuning_mode', '-T',
                        help='tune hsv filter params',
                        default=False,
                        action="store")
    parser.add_argument('--user_name', '-N',
                    help='Set name of user, default: unknown',
                    default='N/A',
                    action="store_true")
    parser.add_argument('--user_id', '-I',
                    help='Set id of user, default: None',
                    default=0,
                    action="store_true")
    parser.add_argument('--img_size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--test', default=test, help='Test mode for visual recognition without ROS')
    
    args = parser.parse_known_args()[0]

    cam = rs_cam(args.disp)

    try:
        realsense_run()
    except rospy.ROSInterruptException:
        print("realsense_run ROS exception")
    except Exception as e:
        print("**Image Error**")
        traceback.print_exc(file=sys.stdout)
    finally:
        cam.pipeline.stop()
        cv2.destroyAllWindows()
        plt.close('all')