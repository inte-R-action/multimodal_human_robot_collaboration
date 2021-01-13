#!/usr/bin/env python3

import rospy
import numpy as np
from std_msgs.msg import String
from user import User
from sam_custom_messages import hand_pos, capability, current_action, user_prediction#, diagnostics
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class

# diag_msg = diagnostics
# diag_msg.Header.Stamp = rospy.get_rostime()
# diag_msg.Header.Seq = 0
# diag_msg.Header.FrameId = "users_node"
# diag_msg.UserId = None
# diag_msg.UserName = None
# diag_msg.Diagnosticstatus.Level = 1
# diag_msg.Diagnosticstatus.Name = "users_node"
# diag_msg.Diagnosticstatus.Message = "Starting..."
# diag_msg.Diagnosticstatus.HardwareId = "N/A"
# diag_msg.Diagnosticstatus.values = [KeyValue(key = 'Runstop hit', value = 'False'),
#                                     KeyValue(key = 'Estop hit', value = 'False')]

def setup_user(name=None):

    id = len(users)
    if name is None:
        name = f"unknown_user_{id}"
    
    users.append[User(name, id)]

def hand_pos_callback(data):
    if users[data.UserId].name != data.UserName:
        print(f"ERROR: users list name {users[data.UserId].name} does not match hand_pos msg name {data.UserName}")
    else:
        if data.Hand == 0:
            self.left_h_pos = [Pose.Position.X, Pose.Position.Y, Pose.Position.Z]
            self.left_h_rot = [Pose.Orientation.X, Pose.Orientation.Y, Pose.Orientation.Z, Pose.Orientation.W]      
        elif data.Hand == 1:
            self.right_h_pos = [Pose.Position.X, Pose.Position.Y, Pose.Position.Z]
            self.right_h_rot = [Pose.Orientation.X, Pose.Orientation.Y, Pose.Orientation.Z, Pose.Orientation.W]
        else:
            print(f"ERROR: hand_pos.hand msg is {data.Hand} but should be 0 (left) or 1 (right)")

    return
    

def current_action_callback(data):
    if users[data.UserId].name != data.UserName:
        print(f"ERROR: users list name {users[data.UserId].name} does not match current_action msg name {data.UserName}")
    else:
        users[data.UserId].current_action = data.action_probs

    return

def users_node():

    frame_id = "users_node"
    rospy.init_node('users_node', anonymous=True)

    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1, keyvalues=keyvalues)
    #status_pub = rospy.Publisher('SystemStatus', diagnostics, queue_size=10)
    #status_pub.publish(diag_msg)
    future_pub = rospy.Publisher('FutureState', user_prediction, queue_size=10)
    
    rospy.Subscriber("HandStates", hand_pos, hand_pos_callback)
    rospy.Subscriber("CurrentAction", current_action, current_action_callback)

    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)

        # diag_msg.Header.Stamp = rospy.get_rostime()
        # diag_msg.Diagnosticstatus.Level = 0
        # diag_msg.Diagnosticstatus.Message = "Running"
        # status_pub.publish(diag_msg)
        diag_obj.publish(0, "Running")
        rate.sleep()

if __name__ == '__main__':
    try:
        users_node()
    except rospy.ROSInterruptException:
        pass