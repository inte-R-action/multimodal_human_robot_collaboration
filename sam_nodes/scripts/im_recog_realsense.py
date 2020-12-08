#!/usr/bin/env python3

# Import Statements
import pyrealsense2 as rs
import numpy as np
import traceback
import argparse
import sys
import time
import cv2
import rospy
from image_screw_detector import ImScrewDetector  # Image screw detector class
from sam_custom_messages.msg import object_state, diagnostics
from diagnostic_msgs.msg import KeyValue

class rs_cam:
    def __init__():
        # Create a pipeline
        self.pipeline = rs.pipeline()
        #Create a config and configure the pipeline to stream
        #  different resolutions of color and depth streams
        config = rs.config()
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        if args.depth:
            config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        
        # Start streaming
        profile = pipeline.start(config)

        if args.depth:
            # Getting the depth sensor's depth scale (see rs-align example for explanation)
            depth_sensor = profile.get_device().first_depth_sensor()
            depth_scale = depth_sensor.get_depth_scale()
            #print("Depth Scale is: " , depth_scale)
            # We will be removing the background of objects more than
            #  clipping_distance_in_meters meters away
            clipping_distance_in_meters = 0.5 #1 meter
            clipping_distance = clipping_distance_in_meters / depth_scale
            # Create an align object
            # rs.align allows us to perform alignment of depth frames to others frames
            # The "align_to" is the stream type to which we plan to align depth frames.
            align_to = rs.stream.color
            self.align = rs.align(align_to)

    def colour_frames(self, frames):
        color_frame = frames.get_color_frame()
        # Validate that both frames are valid
        if not color_frame:
            continue
        color_image = np.asanyarray(color_frame.get_data())

        return color_image

    def depth_frames(self, frames):
        #frames.get_depth_frame() is a 640x360 depth image
        # Align the depth frame to color frame
        aligned_frames = self.align.process(frames)

        # Get aligned frames
        aligned_depth_frame = aligned_frames.get_depth_frame() # aligned_depth_frame is a 640x480 depth image
        color_frame = aligned_frames.get_color_frame()

        # Validate that both frames are valid
        if not aligned_depth_frame or not color_frame:
            continue
        depth_image = np.asanyarray(aligned_depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        return color_image, depth_image, depth_colormap

    def scale(image): # zooms on image
        height, width, channels = image.shape
        scale = 2  # x? digital zoom
        centerX, centerY = int(height / 2), int(width / 2)
        radiusX, radiusY = int(height / (scale * 2)), int(width / (scale * 2))
        minX, maxX = centerX - radiusX, centerX + radiusX
        minY, maxY = centerY - radiusY, centerY + radiusY
        image = cv2.resize(image[minX:maxX, minY:maxY], (width, height), interpolation=cv2.INTER_LINEAR)
        return image

def define_diag():
    frame_id = 'Realsense node'
    # Diagnostic message definitions
    diag_msg = diagnostics()
    diag_msg.Header.stamp = None #rospy.get_rostime()
    diag_msg.Header.seq = 0
    diag_msg.Header.frame_id = frame_id
    diag_msg.UserId = args.user_id
    diag_msg.UserName = args.user_name
    diag_msg.DiagnosticStatus.level = 1 # 0:ok, 1:warning, 2:error, 3:stale
    diag_msg.DiagnosticStatus.name = frame_id
    diag_msg.DiagnosticStatus.message = "Starting..."
    diag_msg.DiagnosticStatus.hardware_id = "N/A"
    diag_msg.DiagnosticStatus.values = []
    return diag_msg

cam = rs_cam()

def realsense_run():
    # ROS node setup
    rospy.init_node(f'Realsense main', anonymous=True)
    diag_msg = define_diag()
    diag_pub = rospy.Publisher('SystemStatus', diagnostics, queue_size=1)
    diag_pub.publish(diag_msg)

    rate = rospy.Rate(10)
    try:
        im_screw_detect = ImScrewDetector()
    except Exceptionas as e:
        print("**Screw Detect Error**")
        traceback.print_exc(file=sys.stdout)
        diag_msg.DiagnosticStatus.level = 2 # 0:ok, 1:warning, 2:error, 3:stale
        diag_msg.DiagnosticStatus.message = f"load screwdetector error: {e}"

    t = time.time()
    while not rospy.is_shutdown():
        try:
            # Get frameset of color and depth
            frames = pipeline.wait_for_frames()

            if args.depth:
                images = cam.depth_frames(frames)
            else:
                images = cam.colour_frames(frames)

            # Remove background - Set pixels further than clipping_distance to grey
            #grey_color = 153
            #depth_image_3d = np.dstack((depth_image,depth_image,depth_image)) #depth image is 1 channel, color is 3 channels
            #bg_removed = np.where((depth_image_3d > clipping_distance) | (depth_image_3d <= 0), grey_color, color_image)
            #image = scale(bg_removed)

            diag_msg.DiagnosticStatus.level = 0 # 0:ok, 1:warning, 2:error, 3:stale
            diag_msg.DiagnosticStatus.message = f"Running"
        except TypeError as e:
            time.sleep(1)
            diag_msg.DiagnosticStatus.level = 2 # 0:ok, 1:warning, 2:error, 3:stale
            diag_msg.DiagnosticStatus.message = f"TypeError"
        except Exception as e:
            print("**Get Image Error**")
            diag_msg.DiagnosticStatus.level = 2 # 0:ok, 1:warning, 2:error, 3:stale
            diag_msg.DiagnosticStatus.message = f"Realsense image error: {e}"
            traceback.print_exc(file=sys.stdout)
            break

        #im_screw_states, tally = im_screw_detect.detect_screws(image, args.disp)
        #im_screw_states = im_screw_states.tolist()
        if args.disp:
            disp_image = np.hstack([i for i in images])
            cv2.namedWindow('Realsense viewer', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('Realsense viewer', disp_image)
            key = cv2.waitKey(1)
            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break

        diag_pub.publish(diag_msg)
        rate.sleep()


## Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Run realsense vision recognition ROS node')
    parser.add_argument('--disp', '-V',
                        help='Enable displaying of camera image',
                        default=None,
                        action="store_true")
    parser.add_argument('--depth', '-D',
                        help='Depth active',
                        default=False,
                        action="store_true")

    args = parser.parse_args()

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
