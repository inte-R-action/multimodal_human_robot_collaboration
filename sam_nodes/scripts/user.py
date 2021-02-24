#!/usr/bin/env python3

import numpy as np
import rospy
from std_msgs.msg import String, Int8, Float64
import cv2
import time, datetime
import matplotlib.pyplot as plt
from postgresql.database_funcs import database
from pub_classes import capability_class


ACTION_CATEGORIES = ['allen_in', 'allen_out', 'screw_in', 'screw_out', 'null']

class User:
    def __init__(self, name, id, frame_id):
        self._imu_pred = np.zeros(6) #class confs, t 
        self._imu_pred_hist = np.empty(6) #class confs, t 
        self._imu_state_hist = np.array([4, 1, datetime.datetime.min, datetime.datetime.min]) #class, conf, tStart, tEnd
        self.left_h_pos = [None, None, None]
        self.left_h_rot = [None, None, None, None]
        self.right_h_pos = [None, None, None]
        self.right_h_rot = [None, None, None, None]
        self.status = None
        self.name = name
        self.id = id
        self.task_data = None
        self.task = None
        self.col_names = None

        self._final_state_hist = np.array([4, 1, datetime.datetime.min, datetime.datetime.min]) #class, conf, tStart, tEnd
        self.curr_task_no = None

        self.capability_obj = capability_class(frame_id=f"{frame_id}_{self.name}", user_id=self.id)

    def update_task(self, task):

        self.task = task
        db = database()
        col_names, actions_list = db.query_table(self.task, 'all')
        self.task_data = pd.DataFrame(actions_list, columns=col_names)
        self.task_data["completed"] = False

        self.col_names, act_data = db.query_table('current_actions',rows=0)


    def update_progress(self):

        self._final_state_hist = np.vstack((self._final_state_hist, self.imu_state_hist[-3, :]))
       
        date = datetime.date.today()
        start_t = self._final_state_hist[-1, 2]
        end_t = self._final_state_hist[-1, 3]
        dur = end_t - start_t
        capability = ACTION_CATEGORIES[int(self._final_state_hist[-1, 0])]

         # Can publish new episode to sql
        db = database()
        db.insert_data_list("Episodes", 
        ["date", "start_t", "end_t", "duration", "user_id", "hand", "capability", "task_id"], 
        [(date, start_t, end_t, dur, 0, "R", capability, 0)])

        # Get next row where action not completed
        next_action_row_i = self.task_data[self.task_data.completed == False].index[0]

        # Assume non-user actions are completed
        while self.task_data.iloc[next_action_row_i]["user_type"] != "human":
            self.task_data.iloc[next_action_row_i]["completed"] = True
            next_action_row_i = self.task_data[self.task_data.completed == False].index[0]

        # Check next action for user matches action completed
        next_action_expected = self.task_data.iloc[next_action_row_i]["action_name"]
        if capability == next_action_expected:
            self.task_data.iloc[next_action_row_i]["completed"] = True
            next_action_row_i = self.task_data[self.task_data.completed == False].index[0]

            self.curr_task_no = self.task_data.iloc[next_action_row_i]["action_no"]
            update_current_action_output()

        else:
            print(f"Updated user capability ({capability}) is not next expected ({next_action_expected})")

        return
    
    def collate_episode(self):
        return

    def update_current_action_output(self):
        try:

            # Update user current action in sql table
            time = datetime.datetime.utcnow()
            data_ins = "%s" + (", %s"*(len(self.col_names)-1))
            separator = ', '
            sql_cmd = f"""INSERT INTO current_actions ({separator.join(self.col_names)})
            VALUES (0, 'N/A', '{time}', '{task_name}', {int(self.task_data.loc[self.curr_task_no]['action_no'])}, '{time}') 
            ON CONFLICT (user_id) DO UPDATE SET updated_t='{time}', task_name='{task_name}', current_action_no={int(self.task_data.loc[self.curr_task_no]['action_no'])}, start_time='{time}';"""
            db.gen_cmd(sql_cmd)

            #db.insert_data_list('current_actions', col_names, 
            #    [(0, "N/A", time, task_name, int(task_data.loc[i]['action_no']), time)])

            self.capability_obj.publish(self.curr_task_no, [self.task_data.loc[self.curr_task_no]['action_name']])
            print(self.task_data.loc[self.curr_task_no])

        except Exception as e:
            print(f"test_robot_control_node connection error: {e}")
            raise
        
        return

    def collate_imu_seq(self):
        # 'Dilation' filter to remove single erroneous predictions
        if np.shape(imu_state_hist)[0] >= 4:
            if (self.imu_state_hist[-1, 0] == self.imu_state_hist[-3, 0]):# & (imu_state_hist[-2, 1] <= 0.00000000001): # WHAT IS THIS DOING???
                self.imu_state_hist[-2, 0] = self.imu_state_hist[-1, 0] #NEED TO CHECK CONFIDENCES HERE

            # Group predictions of same type together
            if self.imu_state_hist[-2, 0] == self.imu_state_hist[-3, 0]:
                i = np.where(self.imu_pred_hist[:, -1]==self.imu_state_hist[-3, 2])[0][0] #Get index where action starts
                self.imu_state_hist[-2, 1] = np.mean(self.imu_pred_hist[i:-1, int(self.imu_state_hist[-2, 0])].astype(float)) #Not convinced about this mean
                self.imu_state_hist[-2, 2] = self.imu_state_hist[-3, 2] # set start time
                self.imu_state_hist = np.delete(self.imu_state_hist, -3, 0)
            else:
                # New action predicted
                self.update_progress()

                

    
