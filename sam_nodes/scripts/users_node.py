#!/usr/bin/env python3

import rospy
import numpy as np
from std_msgs.msg import String
from user import User
from sam_custom_messages.msg import hand_pos, capability, current_action, user_prediction
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class
from IMU_collator import collate_imu_seq
import argparse
import datetime
import pandas as pd
from postgresql.database_funcs import database

# Argument parsing
parser = argparse.ArgumentParser(
    description='Base structure for connecting and streaming data from Shimmer 3 IMU sensor')

parser.add_argument('--user_names', '-N',
                    nargs='*',
                    help='Set name of user, default: unknown',
                    default='unknown',
                    type=lambda s: [str(item) for item in s.split(',')])

args = parser.parse_args()


def setup_user(users, name=None):

    id = len(users)
    if name is None:
        name = f"unknown_user_{id}"
    
    users.append(User(name, id))
    return users

def hand_pos_callback(data, users):
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
    

def current_action_callback(data, users):
    if users[data.UserId].name != data.UserName:
        print(f"ERROR: users list name {users[data.UserId].name} does not match current_action msg name {data.UserName}")
    else:
        #users[data.UserId].actions.extend([data.action_probs, data.Header.stamp])
        time = datetime.datetime.utcfromtimestamp(data.Header.stamp.to_sec())
        users[data.UserId]._imu_pred_hist = np.vstack((users[data.UserId]._imu_pred_hist, (np.hstack((data.ActionProbs, time)))))
        users[data.UserId]._imu_state_hist = np.vstack((users[data.UserId]._imu_state_hist, [np.argmax(data.ActionProbs).astype(float), 0, time, time]))

        users[data.UserId]._imu_state_hist, users[data.UserId]._imu_pred_hist = collate_imu_seq(users[data.UserId]._imu_state_hist, users[data.UserId]._imu_pred_hist)

    return

def users_node():
    
    users = []
    for name in args.user_names:
        users = setup_user(users, name)

    frame_id = "users_node"
    rospy.init_node('users_node', anonymous=True)
    keyvalues = []
    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1, keyvalues=keyvalues)
    future_pub = rospy.Publisher('FutureState', user_prediction, queue_size=10)
    
    rospy.Subscriber("HandStates", hand_pos, hand_pos_callback, (users))
    rospy.Subscriber("CurrentAction", current_action, current_action_callback, (users))

    db = database()

    task = 'assemble_box'
    col_names, actions_list = db.query_table(task, 'all')
    actions = pd.DataFrame(actions_list, columns=col_names)

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        hello_str = f"{frame_id} active"
        rospy.loginfo(hello_str)

        diag_obj.publish(0, "Running")
        rate.sleep()

if __name__ == '__main__':
    try:
        users_node()
    except rospy.ROSInterruptException:
        pass