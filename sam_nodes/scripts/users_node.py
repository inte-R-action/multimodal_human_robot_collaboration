#!/usr/bin/env python3.7

import rospy
import numpy as np
from std_msgs.msg import String
from user import User
from sam_custom_messages.msg import hand_pos, capability, current_action, diagnostics
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class, capability_class
import argparse
import datetime, time
import pandas as pd
from postgresql.database_funcs import database
import os
os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/"))

# Argument parsing
parser = argparse.ArgumentParser(
    description='Base structure for connecting and streaming data from Shimmer 3 IMU sensor')

parser.add_argument('--user_names', '-N',
                    nargs='*',
                    help='Set name of user, default: unknown',
                    default='unknown',
                    type=lambda s: [str(item) for item in s.split(',')])
parser.add_argument('--task_type', '-T',
                    help='Task for users to perform, options: assemble_box (default), assemble_complex_box',
                    default='basic_box')

args = parser.parse_known_args()[0]

database_stat = 1
shimmer_stat = 1
imrecog_stat = 1

def setup_user(users, frame_id, task, name=None, use_vision=True):

    id = len(users)+1
    if name is None:
        name = "unknown"
    
    users.append(User(name, id, frame_id, use_vision))

    db = database()
    time = datetime.datetime.utcnow()
    sql_cmd = f"""DELETE FROM users WHERE user_id = {id};"""
    db.gen_cmd(sql_cmd)
    db.insert_data_list("users", ['user_id', 'user_name', 'last_active'], [(id, name, time)])

    users[id-1].update_task(task)
    return users

def hand_pos_callback(data, users):
    if users[data.UserId-1].name != data.UserName:
        print(f"ERROR: users list name {users[data.UserId-1].name} does not match hand_pos msg name {data.UserName}")
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

    i = [idx for idx, user in enumerate(users) if data.UserId==user.id]
    if i:
        i = i[0]
        if users[i].name != data.UserName:
            print(f"ERROR: users list name {users[i].name} does not match current_action msg name {data.UserName}")
        else:
            #users[i].actions.extend([data.action_probs, data.Header.stamp])
            time = datetime.datetime.utcfromtimestamp(data.Header.stamp.secs)#to_sec())
            users[i]._imu_pred_hist = np.vstack((users[i]._imu_pred_hist, (np.hstack((data.ActionProbs, time)))))
            users[i]._imu_state_hist = np.vstack((users[i]._imu_state_hist, [np.argmax(data.ActionProbs).astype(float), 0, time, time]))

            #users[i]._imu_state_hist, users[i]._imu_pred_hist = collate_imu_seq(users[i]._imu_state_hist, users[i]._imu_pred_hist)
            users[i].collate_imu_seq()
    return

def sys_stat_callback(data, users):
    global database_stat
    global shimmer_stat
    global imrecog_stat

    if data.Header.frame_id == 'Database_node':
        database_stat = data.DiagnosticStatus.level

    if data.Header.frame_id == f'Realsense_node':
        imrecog_stat = data.DiagnosticStatus.level

    if users:
        for i in range(len(users)):
            if data.Header.frame_id == f'shimmerBase {users[i].name} {users[i].id} node':
                users[i].shimmer_ready = data.DiagnosticStatus.level
            elif data.Header.frame_id == f'fakeIMUpub_node':
                users[i].shimmer_ready = data.DiagnosticStatus.level
        
        shimmer_stat = max(users[i].shimmer_ready for i in range(len(users)))

def next_action_override_callback(msg, users):
    data = msg.data
    if users:
        for i in range(len(users)):
            if data == users[i].name:
                users[i].next_action_override()
    pass

def users_node():
    
    frame_id = "users_node"
    rospy.init_node(frame_id, anonymous=True)
    keyvalues = []
    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1, keyvalues=keyvalues)
    users = []

    rospy.Subscriber("SystemStatus", diagnostics, sys_stat_callback, (users))
    rospy.Subscriber("NextActionOverride", String, next_action_override_callback, (users))
    global database_stat
    # Wait for postgresql node to be ready
    while database_stat != 0 and not rospy.is_shutdown():
        print(f"Waiting for postgresql node status, currently {database_stat}")
        diag_obj.publish(1, "Waiting for postgresql node")
        time.sleep(0.5)

    task = args.task_type #'assemble_box'
    use_vision = True
    if use_vision:
        global imrecog_stat
        # Wait for postgresql node to be ready
        while imrecog_stat != 0 and not rospy.is_shutdown():
            print(f"Waiting for imrecog_stat node status, currently {imrecog_stat}")
            diag_obj.publish(1, "Waiting for imrecog_stat node")
            time.sleep(0.5)

    for name in args.user_names:
        users = setup_user(users, frame_id, task, name, use_vision)

    timer = time.time()

    global shimmer_stat
    # Wait for postgresql node to be ready
    while shimmer_stat != 0 and not rospy.is_shutdown():
        print(f"Waiting for shimmer node status, currently {shimmer_stat}")
        diag_obj.publish(1, "Waiting for shimmer node")
        time.sleep(0.5)

    
    rospy.Subscriber("HandStates", hand_pos, hand_pos_callback, (users))
    rospy.Subscriber("CurrentAction", current_action, current_action_callback, (users))

    if use_vision:
        # Get first reading for screw counters, need to wait for good readings
        while time.time() - timer < 5:
            time.sleep(0.5)
        for user in users:
            user.screw_counter.next_screw()

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        rospy.loginfo(f"{frame_id} active")

        diag_obj.publish(0, "Running")
        rate.sleep()

if __name__ == '__main__':
    try:
        users_node()
    except rospy.ROSInterruptException:
        pass
