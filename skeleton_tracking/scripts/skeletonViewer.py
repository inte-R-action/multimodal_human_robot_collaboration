#!/usr/bin/env python3

# encoding: utf-8

"""Module to connect to a kinect through ROS + OpenNI and access
the skeleton postures.
"""

from __future__ import print_function
import roslib
roslib.load_manifest('skeleton_tracking')
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

BASE_FRAME = 'camera_rgb_optical_frame'#'/openni_depth_frame'
FRAMES = [
        'head',
        'neck',
        'torso',
        'left_shoulder',
        'left_elbow',
        'left_hand',
        'left_hip',
        'left_knee',
        'left_foot',
        'right_shoulder',
        'right_elbow',
        'right_hand',
        'right_hip',
        'right_knee',
        'right_foot',
        ]
LAST = rospy.Duration()


class Kinect:

    def __init__(self, name='kinect_listener', user=1):
        self.listener = tf.TransformListener()
        self.user = user

    
    def get_posture(self):
        """Returns a list of frames constituted by a translation matrix
        and a rotation matrix.
        Raises IndexError when a frame can't be found (which happens if
        the requested user is not calibrated).
        """
        try:
            frames = []
            for frame in FRAMES:
                self.listener.waitForTransform(BASE_FRAME, "/%s_%d" % (frame, self.user), rospy.Time(), rospy.Duration(4.0))

                trans, rot = self.listener.lookupTransform(BASE_FRAME, "/%s_%d" % (frame, self.user), LAST)
                #frames.append((trans, rot))
                frames.append((trans))
            return frames, trans
        except (tf.LookupException,
                tf.ConnectivityException,
                tf.ExtrapolationException):
            raise IndexError

image = None
class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)

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

    

    # try:
    #   #self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    #   pass
    # except CvBridgeError as e:
    #   print(e)

camera_info = None
def image_info_cb(data):
    global camera_info 
    camera_info = data

def main(args):
    global image
    rospy.init_node('skeleton_viewer', anonymous=True)

    image_info_sub = rospy.Subscriber("/camera/rgb/camera_info", CameraInfo, image_info_cb) 

    # Init the Kinect object
    kin = Kinect()

    ic = image_converter()

    cam_model = PinholeCameraModel()
    while not camera_info:
        time.sleep(1)
        print("waiting for camera info")

    cam_model.fromCameraInfo(camera_info)
    print(cam_model.cx(), cam_model.cy())

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
      
    # fontScale
    fontScale = 1
       
    # Blue color in BGR
    color = (255, 0, 0)
      
    # Line thickness of 2 px
    thickness = 2

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        try:
            frames, trans = kin.get_posture()
            disp_image = image
            i=0
            for frame in frames:
                coords = cam_model.project3dToPixel(frame)
                disp_image = cv2.circle(disp_image, (int(coords[0]), int(coords[1])), radius=10, color=(0, 0, 255), thickness=-1)
                disp_image = cv2.putText(disp_image, FRAMES[i], (int(coords[0]), int(coords[1])), font, 
                       fontScale, color, thickness, cv2.LINE_AA)
                i+=1
            #coords = cam_model.project3dToPixel(frame)
            disp_image = cv2.circle(disp_image, (int(cam_model.cx()), int(cam_model.cy())), radius=5, color=(0, 255, 0), thickness=-1)
            cv2.imshow("Image window", disp_image)
            cv2.waitKey(1)
            #rate.sleep()
        except tf2_ros.TransformException:
            print("user not found error")

if __name__ == '__main__':
    try:
        main(sys.argv)
    except rospy.ROSInterruptException:
        cv2.destroyAllWindows()