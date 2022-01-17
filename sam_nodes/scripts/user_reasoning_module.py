#!/usr/bin/env python3.7

import rospy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from postgresql.database_funcs import database
from tensorflow.keras.models import load_model
import datetime
plt.ion()

MODEL_FILE = ""


class reasoning_module:
    def __init__(self, name, id, frame_id, ACTION_CATEGORIES, test):
        self.test = test
        self.name = name
        self.id = id
        self.frame_id = frame_id
        self.task_data = None
        self.task = None
        self.models = []
        self.human_row_idxs = []
        self.fut_act_pred_col_names = None
        self.db = database()

    def setup_prediction_networks(self):
        for index, row in self.task_data.iterrows():
            if row['user_type'] == 'human':
                if not self.test:
                    self.models.append(load_model(MODEL_FILE))
                else:
                    self.models.append("fake model")
                self.human_row_idxs.append(index)

    def predict_action_statuses(self):
        for i in range(len(self.models)):
            if not self.test:
                [time, started, done] = self.models[i].predict()
            else:
                [time, started, done] = [datetime.datetime.now().time(), 0, 0]
            self.task_data.loc[self.human_row_idxs[i], 'started'] = started
            self.task_data.loc[self.human_row_idxs[i], 'done'] = done
            self.task_data.loc[self.human_row_idxs[i], 'time_left'] = time

        self.publish_to_database()

    def publish_to_database(self):
        # Update user current action in sql table
        time = datetime.datetime.utcnow()
        separator = ', '

        # Delete old rows for user
        sql_cmd = f"""DELETE FROM future_action_predictions WHERE user_id = {self.id};"""
        self.db.gen_cmd(sql_cmd)

        # Insert new rows for user for each action prediciton status
        sql_cmd = f"""INSERT INTO future_action_predictions ({separator.join(self.fut_act_pred_col_names)})
        VALUES """
        for i in range(len(self.models)):
            if i != 0:
                sql_cmd += ", "
            sql_cmd += f"""({self.id}, '{self.name}', '{time}', '{self.task}',
            {int(self.task_data.loc[self.human_row_idxs[i], 'action_no'])},
            '{self.task_data.loc[self.human_row_idxs[i], 'started']}',
            '{self.task_data.loc[self.human_row_idxs[i], 'done']}',
            '{self.task_data.loc[self.human_row_idxs[i], 'time_left']}')"""
        sql_cmd += ";"
        self.db.gen_cmd(sql_cmd)

    def update_task(self, task):
        self.task = task
        col_names, actions_list = self.db.query_table(self.task, 'all')
        self.task_data = pd.DataFrame(actions_list, columns=col_names)
        self.task_data["started"] = 0
        self.task_data["done"] = 0
        self.task_data["time_left"] = datetime.datetime.now().time()

        self.fut_act_pred_col_names, act_data = self.db.query_table('future_action_predictions',rows=0)

        sql_cmd = f"""DELETE FROM future_action_predictions WHERE user_id = {self.id};"""
        self.db.gen_cmd(sql_cmd)

        self.setup_prediction_networks()
