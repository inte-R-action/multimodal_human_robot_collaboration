#!/usr/bin/env python3.7

import sys, struct, serial, os
import numpy as np
import argparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import rospy
from std_msgs.msg import Int8, Float64
from pub_classes import diag_class, act_class
import csv

CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/sam_nodes/scripts/"))

# Argument parsing
parser = argparse.ArgumentParser(
    description='Base structure for connecting and streaming data from Shimmer 3 IMU sensor')

parser.add_argument('--disp', '-V',
                    help='Enable displaying of live graphs',
                    default=True,
                    action="store_true")

parser.add_argument('--bar', '-B',
                    help='Enable displaying of live prediction bar plot',
                    default=True,
                    action="store_true")

args = parser.parse_known_args()[0]

def fakeIMUmain():
    print("-----Here we go-----")
    frame_id = f'fakeIMUpub_node'
    rospy.init_node(frame_id, anonymous=True)
    rate = rospy.Rate(2)  # Message publication rate, Hz => should be 2

    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name='unknown', queue=1)
    act_obj = act_class(frame_id=frame_id, user_id=0, user_name='unknown', queue=1)
    
    prediction = np.zeros(5)

    print("Starting main loop")
    
    class_pred = CATEGORIES[-1]
    diag_level = 1 # 0:ok, 1:warning, 2:error, 3:stale

    with open ('fake_imu_data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            if not rospy.is_shutdown():

                prediction = [float(i) for i in row[0:5]]
                prediction = np.reshape(prediction, (-1))
                class_pred = CATEGORIES[np.argmax(prediction)]

                try:
                    act_obj.publish(prediction.tolist())
                    diag_msg = "fake_imu_pub all good"
                    diag_level = 0 # ok
                except Exception as e:
                    print(f"Error: {e}")
                    diag_msg = "fake_imu_pub not so good"
                    diag_level = 1 # warning
                
                diag_obj.publish(diag_level, diag_msg)
                #print(f"Action: {class_pred} Probs: {prediction}")
                rate.sleep()


if __name__ == "__main__":
    try:
        fakeIMUmain()
    except rospy.ROSInterruptException:
        print("Keyboard Interrupt")
        plt.close('all')
    finally:
        if args.disp:
            plt.show()
        quit_IMU = True

        print("All done")
