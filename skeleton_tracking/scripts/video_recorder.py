#!/usr/bin/env python3

# encoding: utf-8

"""Module to connect to a kinect through ROS and record stream
"""

## Need this to be running for camera: roslaunch openni_launch openni.launch

from __future__ import print_function
import rospy
import tf
import sys
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from image_geometry import PinholeCameraModel
import time
import tf2_ros
import os

os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/user_trial_data_recording/videos/"))

test_mode = False
file = f"hrc_output_{time.time()}.avi"

image = None

class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)
    #self.image_sub = rospy.Subscriber("/camera/depth/image",Image,self.callback)

  def callback(self,data):
    global image
    try:
      #cv_image = self.bridge.imgmsg_to_cv2(data, "32FC1")
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    image = cv_image

camera_info = None
def image_info_cb(data):
    global camera_info 
    camera_info = data

def main(args):
    global image
    rospy.init_node('skeleton_viewer', anonymous=True)

    image_info_sub = rospy.Subscriber("/camera/rgb/camera_info", CameraInfo, image_info_cb)

    if test_mode:
        cap= cv2.VideoCapture(0)

        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        	int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    else:
        ic = image_converter()

        cam_model = PinholeCameraModel()
        while (not camera_info) and (not rospy.is_shutdown()):
            time.sleep(1)
            print("waiting for camera info")

        cam_model.fromCameraInfo(camera_info)
        size = cam_model.fullResolution()
        print(cam_model.cx(), cam_model.cy(), cam_model.fullResolution())

    fps = 30
    rate = rospy.Rate(fps)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    writer = cv2.VideoWriter()
    success = writer.open(file, fourcc, fps, size, True) 

    while not rospy.is_shutdown():
        if test_mode:
            ret,image= cap.read()

        writer.write(image) 

        cv2.imshow("Image window", image)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        rate.sleep()

    if test_mode:
        cap.release()

    writer.release()


if __name__ == '__main__':
    try:
        main(sys.argv)
    except rospy.ROSInterruptException:
        cv2.destroyAllWindows()