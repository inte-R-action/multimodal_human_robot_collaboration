#!/usr/bin/env python3.7

# encoding: utf-8

"""Module to connect to a kinect through ROS + OpenNI and access
the skeleton postures.
"""

from __future__ import print_function
import tf2_ros
import time
from image_geometry import PinholeCameraModel
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from std_msgs.msg import String
from rospy.numpy_msg import numpy_msg
from geometry_msgs.msg import Pose
from sam_custom_messages.msg import skeleton, diagnostics
from diagnostic_msgs.msg import KeyValue
import cv2
import sys
import tf
import rospy
import roslib
roslib.load_manifest('skeleton_tracking')

BASE_FRAME = 'camera_rgb_optical_frame'  # '/openni_depth_frame'
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

image = None
camera_info = None


class diag_class:
    def __init__(self, frame_id, user_id=1, user_name="unknown", queue=1, keyvalues=[]):
        # frame_id=str, user_id=int, user_name=str, queue=int, keyvalues=list of KeyValue items
        # Diagnostic message definitions
        self.diag_msg = diagnostics()
        self.diag_msg.Header.stamp = rospy.get_rostime()
        self.diag_msg.Header.seq = None
        self.diag_msg.Header.frame_id = frame_id
        self.diag_msg.UserId = user_id
        self.diag_msg.UserName = user_name
        self.diag_msg.DiagnosticStatus.level = 1 # 0:ok, 1:warning, 2:error, 3:stale
        self.diag_msg.DiagnosticStatus.name = frame_id
        self.diag_msg.DiagnosticStatus.message = "Starting..."
        self.diag_msg.DiagnosticStatus.hardware_id = "N/A"
        self.diag_msg.DiagnosticStatus.values = keyvalues

        self.publisher = rospy.Publisher('SystemStatus', diagnostics, queue_size=queue)
        self.publish(1, "Starting...")

    def publish(self, level, message, keyvalues=[]):
        self.diag_msg.DiagnosticStatus.level = level # 0:ok, 1:warning, 2:error, 3:stale
        self.diag_msg.DiagnosticStatus.message = message
        self.diag_msg.DiagnosticStatus.values = keyvalues
        self.diag_msg.Header.stamp = rospy.get_rostime()
        if self.diag_msg.Header.seq is None:
            self.diag_msg.Header.seq = 0
        else:
            self.diag_msg.Header.seq += 1

        self.publisher.publish(self.diag_msg)


class Kinect:
    def __init__(self, user, name='kinect_listener'):
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
                self.listener.waitForTransform(
                    BASE_FRAME, "/%s_%d" % (frame, self.user), rospy.Time(), rospy.Duration(4.0))

                trans, rot = self.listener.lookupTransform(
                    BASE_FRAME, "/%s_%d" % (frame, self.user), LAST)
                frames.append((trans, rot))
                #frames.append((trans))

            return frames
        except (tf.LookupException,
                tf.ConnectivityException,
                tf.ExtrapolationException):
            raise IndexError


class image_converter:
    def __init__(self):
        #self.image_pub = rospy.Publisher("image_topic_2",Image)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber(
            "/camera/rgb/image_color", Image, self.callback)
        #self.image_sub = rospy.Subscriber("/camera/depth/image",Image,self.callback)

    def callback(self, data):
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


def image_info_cb(data):
    global camera_info
    camera_info = data


def main(args):
    global image
    disp = True
    frame_id = 'skeleton_viewer'
    rospy.init_node(frame_id, anonymous=True)

    image_info_sub = rospy.Subscriber("/camera/rgb/camera_info", CameraInfo, image_info_cb)
    joints_publisher = rospy.Publisher('SkeletonJoints', skeleton, queue_size = 1)
    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1)

    user_id = 1
    joints_msg = skeleton()
    joints_msg.Header.stamp = rospy.get_rostime()
    joints_msg.Header.seq = 0
    joints_msg.Header.frame_id = frame_id
    joints_msg.UserId = user_id
    joints_msg.UserName = 'l'

    # Init the Kinect object
    kin = Kinect(user_id)

    ic = image_converter()

    cam_model = PinholeCameraModel()
    while (not camera_info) and (not rospy.is_shutdown()):
        time.sleep(1)
        diag_obj.publish(1, "Waiting for camera info")
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

    pose_msg = Pose()
    diag_timer = time.time()
    rate = rospy.Rate(1)  # 1hz
    while not rospy.is_shutdown():
        try:
            frames = kin.get_posture()

            for i in range(len(FRAMES)):
                pose_msg = Pose()
                pose_msg.position.x = frames[i][0][0]
                pose_msg.position.y = frames[i][0][1]
                pose_msg.position.z = frames[i][0][2]
                pose_msg.orientation.x = frames[i][1][0]
                pose_msg.orientation.y = frames[i][1][1]
                pose_msg.orientation.z = frames[i][1][2]
                pose_msg.orientation.w = frames[i][1][3]

                setattr(joints_msg, FRAMES[i], pose_msg)

            joints_msg.Header.stamp = rospy.get_rostime()
            joints_msg.Header.seq += 1
            joints_publisher.publish(joints_msg)

            if disp:
                disp_image = image
                i = 0
                for trans, rot in frames:
                    coords = cam_model.project3dToPixel(trans)
                    disp_image = cv2.circle(disp_image, (int(coords[0]), int(
                        coords[1])), radius=10, color=(0, 0, 255), thickness=-1)
                    disp_image = cv2.putText(disp_image, FRAMES[i], (int(coords[0]), int(coords[1])), font,
                                            fontScale, color, thickness, cv2.LINE_AA)
                    i += 1
                #coords = cam_model.project3dToPixel(trans)
                disp_image = cv2.circle(disp_image, (int(cam_model.cx()), int(
                    cam_model.cy())), radius=5, color=(0, 255, 0), thickness=-1)
                cv2.imshow("Image window", disp_image)
                cv2.waitKey(1)

            # rate.sleep()
            if time.time()-diag_timer >1:
                diag_obj.publish(0, "Running")
                diag_timer = time.time()
        except tf2_ros.TransformException:
            print("user not found error")
        except Exception as e:
            print("skeleton viewer error: ", e)


if __name__ == '__main__':
    try:
        main(sys.argv)
    except rospy.ROSInterruptException:
        cv2.destroyAllWindows()
