#!/usr/bin/env python3.7

import rospy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from postgresql.database_funcs import database
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, \
    Input, TimeDistributed
import tensorflow as tf
import datetime
from global_data import ACTIONS
import csv
import os

gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
tf.config.experimental.set_visible_devices(devices=gpus[0], device_type='GPU')
tf.config.experimental.set_memory_growth(device=gpus[0], enable=True)

plt.ion()
MODEL_FILE = "./sam_nodes/scripts/models_parameters/lstm_future_prediction_model_20220125-164357.h5"


class reasoning_module:
    def __init__(self, name, Id, frame_id):
        self.test = False
        self.name = name
        self.id = Id
        self.frame_id = frame_id
        self.task_data = None
        self.task = None
        self.models = []
        self.model_inputs = None
        self.means = None
        self.scales = None
        self.human_row_idxs = []
        self.fut_act_pred_col_names = None
        self.db = database()

    def setup_prediction_networks(self):
        if not self.test:
            old_model = load_model(MODEL_FILE)
            old_weights = old_model.get_weights()  # copy weights

        col_names, data = self.db.query_table('users', 'all')
        users_data = pd.DataFrame(data, columns=col_names)
        users_data = users_data.loc[users_data['user_name']==self.name]
        col_names, data = self.db.query_table('tasks', 'all')
        tasks_data = pd.DataFrame(data, columns=col_names)
        tasks_data = tasks_data.loc[tasks_data['task_name']==self.task]

        self.model_inputs = []
        for index, row in self.task_data.iterrows():
            if row['user_type'] == 'human':
                if not self.test:
                    # Need to recreate model with stateful parameter set and updated input shape
                    new_model = Sequential()
                    new_model.add(Input((1, 8), batch_size=1))
                    new_model.add(LSTM(20, return_sequences=True, stateful=True))
                    new_model.add(TimeDistributed(Dense(120, activation='relu')))
                    new_model.add(TimeDistributed(Dense(120, activation='relu')))
                    new_model.add(TimeDistributed(Dense(3)))
                    new_model.set_weights(old_weights)
                    # compile model
                    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
                    new_model.compile(loss='mse', optimizer=opt)
                    self.models.append(new_model)

                    new_inputs = [None]*8
                    new_inputs[1] = ACTIONS.index(row['action_name'])  # Action of focus
                    new_inputs[2] = row['default_time'].total_seconds()  # Default time
                    new_inputs[3] = users_data[row['action_name']].values[0]  # time adjust for user
                    new_inputs[4] = tasks_data[row['action_name']].values[0]  # time adjustment for task
                    self.model_inputs.append(new_inputs)

                else:
                    self.models.append("fake model")
                self.human_row_idxs.append(index)

        self.model_inputs = np.array(self.model_inputs)

        # Load normalisation parameters
        file_name = "./sam_nodes/scripts/models_parameters/lstm_input_scale_params.csv"
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            scale_data = np.array(list(reader))
            self.means = scale_data[1:, 1].astype(float)
            self.scales = scale_data[1:, -1].astype(float)

    def normalise_input_data(self, input_data):
        return (input_data-self.means)/self.scales

    def predict_action_statuses(self, action_probs):
        time = 0
        started = 1
        done = 1
        for i in range(len(self.models)):
            if not self.test:
                self.model_inputs[i, 0] = action_probs[self.model_inputs[i, 1]]  # Action prediction
                self.model_inputs[i, -3:] = [time, started, done] # Previous action status

                input_data = self.normalise_input_data(self.model_inputs[i, :])
                input_data = np.nan_to_num(np.array(input_data, ndmin=3, dtype=np.float))
                time, started, done = self.models[i](input_data, training=False)[0, 0, :].numpy()
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
