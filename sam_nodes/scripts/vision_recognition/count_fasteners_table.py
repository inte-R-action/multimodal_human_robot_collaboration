#!/usr/bin/env python3

import inspect
import os
import sys
import time
from decimal import ROUND_HALF_UP, Decimal
from statistics import mean
import rospy
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from pub_classes import fastener_count_class
from std_msgs.msg import Int8
from sam_custom_messages.msg import object_state



class fastener_counter():
    def __init__(self, frame_id, u_id, u_name):  #, type='raw_count'):
        # if type == 'raw_count':
        rospy.Subscriber('RawFastenerCount', Int8, self.raw_count_callback)
        # elif type == 'obj_msg_count':
            # rospy.Subscriber('ObjectStates', object_state, self.obj_msg_count_callback)

        self.fastener_pub_obj = fastener_count_class(frame_id=frame_id, user_id=u_id, user_name=u_name)
        self.seq = None
        self.fasteners = []
        self.fastener_totals = []
        self.fastener_ave = 0
        self.fastener_ave_last = 0
        self.discard = False

    # def obj_msg_count_callback(self, data):
    #     # Use this when counting fasteners from custom ros message
    #     if data.Header.seq == self.seq:
    #         if data.Object.Info[0] == 'fastener':
    #             self.fasteners.append([data.Pose.position.x, data.Pose.position.y])
    #         if data.Object.Info[0] == 'hand':
    #             self.discard = True
    #     else:
    #         if not self.discard:
    #             self.count_fasteners()
    #         self.discard = False
    #         self.seq = data.Header.seq
    #         self.fasteners = []
    #         if data.Object.Info[0] == 'fastener':
    #             self.fasteners.append([data.Pose.position.x, data.Pose.position.y])

    def raw_count_callback(self, msg):
        # Use this when counting fasteners direct
        self.fasteners = range(msg.data)
        self.count_fasteners()

    def count_fasteners(self):
        self.fastener_totals.append([time.time(), len(self.fasteners)])  # Append new count to history
        self.fastener_totals = [count for count in self.fastener_totals if time.time()-count[0] < 1]  # Get last 1 s worth of fastener counts
        self.fastener_ave = int(Decimal(mean(list(zip(*self.fastener_totals))[1])).to_integral_value(rounding=ROUND_HALF_UP))
        # print(f"Current number fasteners: {self.fastener_ave}, last: {self.fastener_ave_last}")
        self.fastener_pub_obj.publish(self.fastener_ave, self.fastener_ave_last)

        self.fastener_ave_last = self.fastener_ave

    # def next_fastener(self):
    #     print("next fastener")
    #     self.fastener_ave_last = self.fastener_ave
    #     self.fastener_totals = []
    #     self.fastener_ave = 0


def run():
    # ROS node setup
    frame_id = 'fastener_counter'
    rospy.init_node(frame_id, anonymous=True)

    counter = fastener_counter(frame_id, 1, 'unknown')

    rate = rospy.Rate(5)  # 1hz
    while not rospy.is_shutdown():
        #counter.next_fastener()
        print(counter.fastener_ave)
        rate.sleep()


if __name__ == '__main__':
    run()
