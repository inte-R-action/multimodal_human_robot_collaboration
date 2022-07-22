#!/usr/bin/env python3.7

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Accel, Vector3
from sam_custom_messages.msg import object_state


class obj_class:
    def __init__(self, frame_id, names, queue=1):
        # frame_id=str, names=pytorch classifer output names, queue=int
        # Object message definitions
        self.obj_msg = object_state()
        self.obj_msg.Header.stamp = rospy.get_rostime()
        self.obj_msg.Header.seq = None
        self.obj_msg.Header.frame_id = frame_id
        self.obj_msg.Object.Id = None
        self.obj_msg.Object.Obj_type = None
        self.obj_msg.Object.Info = None
        self.obj_msg.Pose.orientation.x = None
        self.obj_msg.Pose.orientation.y = None
        self.obj_msg.Pose.orientation.z = None
        self.obj_msg.Pose.orientation.w = None
        self.obj_msg.Pose.position.x = None
        self.obj_msg.Pose.position.y = None
        self.obj_msg.Pose.position.z = None
        self.names = names

        self.publisher = rospy.Publisher('ObjectStates', object_state, queue_size=queue)

    def publish(self, det, msg_type):
        if msg_type == "classifier":
            # cnn classifier method type
            # det=object for items in image?
            if self.obj_msg.Header.seq is None:
                self.obj_msg.Header.seq = 0
            else:
                self.obj_msg.Header.seq += 1
            
            for *xyxy, conf, cls, dist in det:
                self.obj_msg.Object.Id = 0
                self.obj_msg.Object.Obj_type = int(cls)
                self.obj_msg.Object.Info = [self.names[int(cls)]]
                self.obj_msg.Pose.orientation.x = xyxy[0]
                self.obj_msg.Pose.orientation.y = xyxy[1]
                self.obj_msg.Pose.orientation.z = xyxy[2]
                self.obj_msg.Pose.orientation.w = xyxy[3]
                self.obj_msg.Pose.position.x = (xyxy[0]+xyxy[2])/2
                self.obj_msg.Pose.position.y = (xyxy[1]+xyxy[3])/2
                self.obj_msg.Pose.position.z = dist
                self.obj_msg.Header.stamp = rospy.get_rostime()

                self.publisher.publish(self.obj_msg)

        elif msg_type == "dip":
            #Digital impage processing method type
            if self.obj_msg.Header.seq is None:
                self.obj_msg.Header.seq = 0
            else:
                self.obj_msg.Header.seq += 1
            
            self.obj_msg.Object.Id = 0
            self.obj_msg.Object.Obj_type = int(det[1])
            self.obj_msg.Object.Info = det[2]
            self.obj_msg.Pose = det[0]
            self.obj_msg.Header.stamp = rospy.get_rostime()

            self.publisher.publish(self.obj_msg)


class move_class:
    def __init__(self, frame_id, queue=10):
        # frame_id=str, queue=int
        # Current action message definitions
        #self.move_msg = robot_move()
        #self.move_msg.Header.stamp = rospy.get_rostime()
        #self.move_msg.Header.seq = None
        #self.move_msg.Header.frame_id = frame_id

        self.publisher = rospy.Publisher('RobotMove', String, queue_size=queue)

    def publish(self, command):
        # command = str()
        # if self.move_msg.Header.seq is None:
        #     self.move_msg.Header.seq = 0
        # else:
        #     self.move_msg.Header.seq += 1

        #self.move_msg.Command = commands
        #self.move_msg.Header.stamp = rospy.get_rostime()

        #self.msg = command

        self.publisher.publish(command)
