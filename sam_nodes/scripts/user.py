#!/usr/bin/env python3.7

import numpy as np
import rospy
from std_msgs.msg import String, Int8, Float64
import cv2
import time, datetime
import matplotlib.pyplot as plt
from postgresql.database_funcs import database
from pub_classes import capability_class
import pandas as pd
from vision_recognition.count_screws_table import screw_counter
import argparse
from global_data import SIMPLE_BOX_ACTIONS, COMPLEX_BOX_ACTIONS
from user_perception_module import perception_module
from user_reasoning_module import reasoning_module


class User:
    def __init__(self, name, id, frame_id, use_vision=True):
        # self._imu_pred = np.zeros(6) #class confs, t 
        # self._imu_pred_hist = np.empty(6) #class confs, t 
        # self._imu_state_hist = np.array([4, 1, datetime.datetime.min, datetime.datetime.min]) #class, conf, tStart, tEnd
        
        self.left_h_pos = [None, None, None]
        self.left_h_rot = [None, None, None, None]
        self.right_h_pos = [None, None, None]
        self.right_h_rot = [None, None, None, None]
        self.status = None
        self.name = name
        self.id = id
        self.frame_id = f"{frame_id}_{self.name}"
        self.task_data = None
        self.task = None
        self.ACTION_CATEGORIES = None
        self.col_names = None
        self.db = database()
        self.shimmer_ready = 1
        self.use_vision = use_vision
        if self.use_vision:
            self.screw_counter = screw_counter(self.frame_id, self.id, self.name, type='raw_count')

        self.perception = perception_module(self.name, self.id, self.frame_id, self.ACTION_CATEGORIES)
        self.task_reasoning = reasoning_module(self.name, self.id, self.frame_id, self.ACTION_CATEGORIES)

        # self._final_state_hist = np.array([4, 1, datetime.datetime.min, datetime.datetime.min], ndmin=2) #class, conf, tStart, tEnd
        self.curr_action_no = 0
        self.curr_action_type = None

        self.capability_obj = capability_class(frame_id=self.frame_id, user_id=self.id)        

    def update_task(self, task):

        self.task = task

        if self.task == 'assemble_box':
            self.ACTION_CATEGORIES = SIMPLE_BOX_ACTIONS
            self._imu_pred = np.zeros(6) #class confs, t 
            self._imu_pred_hist = np.empty(6) #class confs, t 
            self._imu_state_hist = np.array([4, 1, datetime.datetime.min, datetime.datetime.min]) #class, conf, tStart, tEnd
            self._final_state_hist = np.array([4, 1, datetime.datetime.min, datetime.datetime.min], ndmin=2) #class, conf, tStart, tEnd
        
        elif self.task == 'assemble_complex_box':
            self.ACTION_CATEGORIES = COMPLEX_BOX_ACTIONS
            self._imu_pred = np.zeros(6) #class confs, t 
            self._imu_pred_hist = np.empty(6) #class confs, t 
            self._imu_state_hist = np.array([0, 1, datetime.datetime.min, datetime.datetime.min]) #class, conf, tStart, tEnd
            self._final_state_hist = np.array([0, 1, datetime.datetime.min, datetime.datetime.min], ndmin=2) #class, conf, tStart, tEnd

        elif self.task == 'assemble_complex_box_manual':
            self.ACTION_CATEGORIES = COMPLEX_BOX_ACTIONS
            self._imu_pred = np.zeros(6) #class confs, t 
            self._imu_pred_hist = np.empty(6) #class confs, t 
            self._imu_state_hist = np.array([0, 1, datetime.datetime.min, datetime.datetime.min]) #class, conf, tStart, tEnd
            self._final_state_hist = np.array([0, 1, datetime.datetime.min, datetime.datetime.min], ndmin=2) #class, conf, tStart, tEnd

        self.perception.actions = self.ACTION_CATEGORIES
        self.task_reasoning.update_task(self.task)
        
        col_names, actions_list = self.db.query_table(self.task, 'all')
        self.task_data = pd.DataFrame(actions_list, columns=col_names)
        self.task_data["completed"] = False

        self.col_names, act_data = self.db.query_table('current_actions',rows=0)
        self.curr_action_no = 0
        self.curr_action_type = self.task_data.iloc[0]["action_name"]
        self.update_current_action_output()

    def collate_episode(self):
        self._final_state_hist = np.vstack((self._final_state_hist, self._imu_state_hist[-3, :]))
       
        date = datetime.date.today()
        start_t = self._final_state_hist[-1, 2]
        end_t = self._final_state_hist[-1, 3]
        dur = end_t - start_t
        action_name = self.ACTION_CATEGORIES[int(self._final_state_hist[-1, 0])]

         # Can publish new episode to sql
        self.db.insert_data_list("Episodes", 
        ["date", "start_t", "end_t", "duration", "user_id", "hand", "task_name", "action_name", "action_no"], 
        [(date, start_t, end_t, dur, self.id, "R", self.task, action_name, int(self.task_data.loc[self.curr_action_no]['action_no']))])

    def update_robot_progress(self):
        action_name = self.ACTION_CATEGORIES[int(self._final_state_hist[-1, 0])]

        try:
            # Get next row where action not completed
            next_action_row_i = self.task_data[self.task_data.completed == False].index[0]
            
            if self.task_data.iloc[next_action_row_i]["user_type"] != "human":
                # Check robot actions are completed, assume other non-user actions are completed
                while self.task_data.iloc[next_action_row_i]["user_type"] != "human":
                    if self.task_data.iloc[next_action_row_i]["user_type"] == "robot":
                        col_names, actions_list = self.db.query_table('Episodes', 'all')
                        episodes = pd.DataFrame(actions_list, columns=col_names)
                        if self.task_data.iloc[next_action_row_i, self.task_data.columns.get_loc("action_name")] in episodes.action_name.values:
                            self.task_data.iloc[next_action_row_i, self.task_data.columns.get_loc("completed")] = True
                            next_action_row_i = self.task_data[self.task_data.completed == False].index[0]
                        else:
                            return "continuing"
                    else:
                        self.task_data.iloc[next_action_row_i, self.task_data.columns.get_loc("completed")] = True
                        next_action_row_i = self.task_data[self.task_data.completed == False].index[0]

                self.curr_action_no = self.task_data.iloc[next_action_row_i]["action_no"]
                self.curr_action_type = self.task_data.iloc[next_action_row_i]["action_name"]
                self.update_current_action_output()

        except IndexError:
            print(f"Looks like user {self.name} tasks are finished")
            return "finished"

    def update_progress(self):
        action_name = self.ACTION_CATEGORIES[int(self._final_state_hist[-1, 0])]

        try:
            # Get next row where action not completed
            next_action_row_i = self.task_data[self.task_data.completed == False].index[0]

        except IndexError:
            print(f"Looks like user {self.name} tasks are finished")
            return "finished"

        # Check next action for user matches action completed
        next_action_expected = self.task_data.iloc[next_action_row_i]["action_name"]
        if action_name == next_action_expected:
            ############ Vision Recognition Check Here #################
            if self.use_vision and ((action_name == 'screw_in') or (action_name == 'allen_in') or (action_name == 'hammer')):
                self.screw_counter.count_screws()
                if (self.screw_counter.screw_ave_last > self.screw_counter.screw_ave):
                    self.task_data.iloc[next_action_row_i, self.task_data.columns.get_loc("completed")] = True
                    next_action_row_i = self.task_data[self.task_data.completed == False].index[0]
                    self.screw_counter.next_screw()
                else:
                    print(f"{action_name} task correctly recognised but last screw count is {self.screw_counter.screw_ave_last} and now is {self.screw_counter.screw_ave}")
            else:
                self.task_data.iloc[next_action_row_i, self.task_data.columns.get_loc("completed")] = True
                next_action_row_i = self.task_data[self.task_data.completed == False].index[0]
        else:
            print(f"Updated user action ({action_name}) is not next expected ({next_action_expected})")

        self.curr_action_no = self.task_data.iloc[next_action_row_i]["action_no"]
        self.curr_action_type = self.task_data.iloc[next_action_row_i]["action_name"]

        return "continuing"

    def next_action_override(self):
        # Get next row where action not completed    
        next_action_row_i = self.task_data[self.task_data.completed == False].index[0]
        self.task_data.iloc[next_action_row_i, self.task_data.columns.get_loc("completed")] = True
        next_action_row_i = self.task_data[self.task_data.completed == False].index[0]
        self.curr_action_no = self.task_data.iloc[next_action_row_i]["action_no"]
        self.curr_action_type = self.task_data.iloc[next_action_row_i]["action_name"]
        if self.use_vision:
            self.screw_counter.next_screw()
        self.update_current_action_output()

    def update_current_action_output(self):
        try:
            # Update user current action in sql table
            time = datetime.datetime.utcnow()
            #data_ins = "%s" + (", %s"*(len(self.col_names)-1))
            separator = ', '
            sql_cmd = f"""INSERT INTO current_actions ({separator.join(self.col_names)})
            VALUES ({self.id}, '{self.name}', '{time}', '{self.task}', {int(self.task_data.loc[self.curr_action_no]['action_no'])}, '{time}') 
            ON CONFLICT (user_id) DO UPDATE SET updated_t='{time}', task_name='{self.task}', current_action_no={int(self.task_data.loc[self.curr_action_no]['action_no'])}, start_time='{time}';"""
            self.db.gen_cmd(sql_cmd)

            self.capability_obj.publish(self.curr_action_no, [self.task_data.loc[self.curr_action_no]['action_name']])
            print(self.task_data.loc[self.curr_action_no])

        except Exception as e:
            print(f"Users node update action output error: {e}")
            raise
        
    def collate_imu_seq(self):
        # 'Dilation' filter to remove single erroneous predictions
        #print('state hist: ', self._imu_state_hist)
        #print('pred hist: ', self._imu_pred_hist)
        if np.shape(self._imu_state_hist)[0] >= 4:
            self.update_robot_progress()

            if (self._imu_state_hist[-1, 0] == self._imu_state_hist[-3, 0]):# & (imu_state_hist[-2, 1] <= 0.00000000001): # WHAT IS THIS DOING???
                self._imu_state_hist[-2, 0] = self._imu_state_hist[-1, 0] #NEED TO CHECK CONFIDENCES HERE

            # Group predictions of same type together
            if self._imu_state_hist[-2, 0] == self._imu_state_hist[-3, 0]:
                i = np.where(self._imu_pred_hist[:, -1] == self._imu_state_hist[-3, 2])[0][0] #Get index where action starts
                self._imu_state_hist[-2, 1] = np.mean(self._imu_pred_hist[i:-1, int(self._imu_state_hist[-2, 0])].astype(float)) #Not convinced about this mean
                self._imu_state_hist[-2, 2] = self._imu_state_hist[-3, 2] # set start time
                self._imu_state_hist = np.delete(self._imu_state_hist, -3, 0)
            else:
                # New action predicted
                self.collate_episode()
                user_state = self.update_progress()
                if user_state == "continuing":
                    self.update_current_action_output()