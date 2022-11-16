#!/usr/bin/env python3.7
# Must be run from scripts folder
method = 'dip'
import argparse
import os
import sys
import time
import traceback
import cv2
import numpy as np
from std_msgs.msg import Int8
from vision_recognition.rs_cam import rs_cam
from vision_recognition.shape_detector import rectangle_detector, detect_blobs
if method == 'CNN':
    from vision_recognition.detect import classifier

try:
    import rospy
    from pub_classes import diag_class
    test = False
except ModuleNotFoundError:
    print("rospy module not found, proceeding in test mode")
    test = True
    # Hacky way of avoiding errors

    class ROS():
        def is_shutdown(self):
            return False

    rospy = ROS()


os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/"))
sys.path.insert(0, "./sam_nodes/scripts/vision_recognition")  # Need to add path to "models" parent dir for pickler


def realsense_run():
    # ROS node setup
    frame_id = 'Realsense_node'

    if not test:
        rospy.init_node(frame_id, anonymous=True)
        diag_obj = diag_class(frame_id=frame_id, queue=1)
        fastener_publisher = rospy.Publisher('RawFastenerCount', Int8, queue_size=1)
        rate = rospy.Rate(10)

    diag_timer = time.time()
    frames = cam.pipeline.wait_for_frames()
    color_image_raw = cam.colour_frames(frames)
    if method == 'CNN':
        img_classifier = classifier('cpu', 'best.pt', 640, color_image_raw, 0.25, 0.45)
    while (not rospy.is_shutdown()) or test:
        try:
            # Get frameset of color and depth
            frames = cam.pipeline.wait_for_frames()
            color_image_raw = cam.colour_frames(frames)

            try:
                if method == 'CNN':
                    im_with_keypoints, det = img_classifier.detect(color_image_raw, classes=['screw', 'hand'])

                    if img_classifier.names.index('hand') not in [item[-2] for item in det]:
                        fastener_publisher.publish(len(det))  # Publish number fasteners
                
                elif method == 'dip':
                    # Greyscale and threshold image
                    imgGry = cv2.cvtColor(color_image_raw, cv2.COLOR_BGR2GRAY)
                    _, thrash = cv2.threshold(imgGry, 120, 255, cv2.CHAIN_APPROX_NONE)#cv2.THRESH_BINARY)
                    # cv2.imshow('imgGry', imgGry)
                    # cv2.imshow('thrash', thrash)
                    
                    # dil_kernel = np.ones((4,4),np.uint8)
                    # thrash = cv2.dilate(thrash, dil_kernel)
                    # cv2.imshow('dialte', thrash)
                    
                    # er_kernel = np.ones((5,5),np.uint8)
                    # thrash = cv2.erode(thrash, er_kernel)
                    # cv2.imshow('erode', thrash)

                    # thrash = cv2.erode(thrash, er_kernel)
                    # cv2.imshow('erode2', thrash)

                    # thrash = cv2.erode(thrash, er_kernel)
                    # cv2.imshow('erode3', thrash)

                    kernel = np.ones((5,5),np.uint8)
                    # opening the image
                    thrash = cv2.morphologyEx(thrash, cv2.MORPH_OPEN,
                           kernel, iterations=5)
                    # cv2.imshow('open', thrash)
                    # closing the image
                    # thrash = cv2.morphologyEx(thrash, cv2.MORPH_CLOSE,
                    #        kernel, iterations=3)
                    # cv2.imshow('close', thrash)
                   
                    

                    

                    # Detect bounding rectangle of fastener area
                    rectangle = rectangle_detector(thrash)
                    # Detect blobs (fastenerss)
                    key_points = detect_blobs(thrash)
                    im_with_keypoints = cv2.drawKeypoints(color_image_raw, key_points, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                    if rectangle is not None:
                        cv2.drawContours(im_with_keypoints, [rectangle], 0, (0, 255, 0), 5)
                        final_points = []
                        for point in key_points:
                            if (cv2.pointPolygonTest(rectangle, point.pt, False)) == 1.0:
                                final_points.append(point)
                            
                        im_with_keypoints = cv2.drawKeypoints(im_with_keypoints, final_points, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                        if not test:
                            fastener_publisher.publish(len(final_points))  # Publish number fasteners
                
                else:
                    print(f"Incorrect vision recognition method: {method}")

            except Exception as e:
                print("Image processing error: ", e)

            if (time.time()-diag_timer) > 1:
                if not test:
                    diag_obj.publish(0, "Running")
                diag_timer = time.time()

        except TypeError as e:
            rospy.sleep(1)
            if not test:
                diag_obj.publish(2, "TypeError")
        except Exception as e:
            print("**Get Image Error**")
            print(e)
            if not test:
                diag_obj.publish(2, f"Realsense image error: {e}")
            traceback.print_exc(file=sys.stdout)
            break

        if args.disp:
            disp_im = im_with_keypoints  # color_image

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
            # rospy.sleep(1)
            pass


## Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Run realsense vision recognition ROS node')
    parser.add_argument('--disp', '-V',
                        help='Enable displaying of camera image',
                        default=True,
                        action="store")
    parser.add_argument('--test',
                        default=test,
                        help='Test mode for visual recognition without ROS')

    args = parser.parse_known_args()[0]

    cam = rs_cam(False)

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
