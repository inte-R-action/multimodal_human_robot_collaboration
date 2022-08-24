#!/usr/bin/env python3.7
# Must be run from scripts folder

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
    while (not rospy.is_shutdown()) or test:
        try:
            # Get frameset of color and depth
            frames = cam.pipeline.wait_for_frames()
            color_image_raw = cam.colour_frames(frames)

            try:
                # Greyscale and threshold image
                imgGry = cv2.cvtColor(color_image_raw, cv2.COLOR_BGR2GRAY)
                _, thrash = cv2.threshold(imgGry, 120, 255, cv2.CHAIN_APPROX_NONE)#cv2.THRESH_BINARY)

                # Detect bounding rectangle of fastener area
                rectangle = rectangle_detector(thrash)
                # Detect blobs (fastenerss)
                key_points = detect_blobs(thrash)
                im_with_keypoints = cv2.drawKeypoints(color_image_raw, key_points, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                if rectangle is not None:
                    cv2.drawContours(im_with_keypoints, [rectangle], 0, (0, 255, 0), 5)
                    if not test:
                        fastener_publisher.publish(len(key_points))  # Publish number fasteners

            except Exception as e:
                print("Image processing error: ", e)

            if (time.time()-diag_timer) > 1:
                if not test:
                    diag_obj.publish(0, "Running")
                diag_timer = time.time()

        except TypeError as e:
            time.sleep(1)
            if not test:
                diag_obj.publish(2, "TypeError")
        except Exception as e:
            print("**Get Image Error**")
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
            # time.sleep(1)
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
