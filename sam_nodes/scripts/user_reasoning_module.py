#!/usr/bin/env python3.7

import os
import queue
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
from datetime import datetime, date
import csv
import numpy as np
import pandas as pd
import rospy
from std_msgs.msg import String, Bool
from sam_custom_messages.msg import fastener_count
from postgresql.database_funcs import database
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Input, TimeDistributed
import tensorflow as tf
from global_data import ACTIONS, GESTURES, inclAdjParam
from fastener_tracker import FastenerTracker


gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
if len(gpus) > 0:
    tf.config.experimental.set_visible_devices(devices=gpus[0], device_type='GPU')
    tf.config.experimental.set_memory_growth(device=gpus[0], enable=True)


class reasoning_module:
    def __init__(self, name, Id, frame_id):
        self.test = False
        self.name = name
        self.id = Id
        self.frame_id = frame_id
        self.inclAdjParam = inclAdjParam
        self.task_data = None
        self.task = None
        self.models = []
        self.model_inputs = None
        self.actions_info_list = []
        self.means = None
        self.scales = None
        self.human_row_idxs = []
        self.output_override = []
        self.fut_act_pred_col_names = None
        self.stop = False
        self.handover_action = False
        self.task_started = False
        self.user_state = "initialising"
        self.tool_statuses = {"screw_in": None,
                              "allen_in": None,
                              "hammer": None}
        self.fastener_probs = {"screw_in": None,
                               "allen_in": None,
                               "hammer": None}

        self.current_gesture = np.array([0, datetime.min, datetime.min]) # class, tStart, tEnd
        self.cmd_publisher = rospy.Publisher('ProcessCommands', String, queue_size=10)
        self.usr_fdbck_pub = rospy.Publisher('UserFeedback', String, queue_size=10)
        self.handover_active_pub = rospy.Publisher('HandoverActive', Bool, queue_size=10)
        self.robot_stat_sub = rospy.Subscriber("RobotStatus", String, self.robot_stat_callback)
        self.tool_stat_sub = rospy.Subscriber("ToolStatus", String, self.tool_stat_callback)
        self.fastener_sub = rospy.Subscriber("FastenerCounts", fastener_count, self.update_fastener_count)
        self.db = database()

    def update_user_details(self, name=None, Id=None, frame_id=None):
        if name:
            self.name = name
        if Id:
            self.id = Id
        if frame_id:
            self.frame_id = frame_id

    def setup_prediction_networks(self):
        if not self.test:
            folder = './sam_nodes/scripts/models_parameters'
            MODEL_FILE = f"{folder}/lstm_future_prediction_model_inclAdjParam{self.inclAdjParam}.h5"

            old_model = load_model(MODEL_FILE)
            old_weights = old_model.get_weights()  # copy weights

        col_names, data = self.db.query_table('users', 'all')
        users_data = pd.DataFrame(data, columns=col_names)
        users_data = users_data.loc[users_data['user_name'] == self.name]
        col_names, data = self.db.query_table('tasks', 'all')
        tasks_data = pd.DataFrame(data, columns=col_names)
        tasks_data = tasks_data.loc[tasks_data['task_name'] == self.task]

        self.model_inputs = []
        prev_r_action = None
        for r, row in self.task_data.iterrows():
            if row['user_type'] == 'human':
                if not self.test:
                    if self.inclAdjParam:
                        input_size = 7
                    else:
                        input_size = 5
                    # Need to recreate model with stateful parameter set and updated input shape
                    new_model = Sequential()
                    new_model.add(Input((1, input_size), batch_size=1))
                    new_model.add(LSTM(20, return_sequences=True, stateful=True))
                    new_model.add(TimeDistributed(Dense(120, activation='relu')))
                    new_model.add(TimeDistributed(Dense(120, activation='relu')))
                    new_model.add(TimeDistributed(Dense(3)))
                    new_model.set_weights(old_weights)
                    # compile model
                    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
                    new_model.compile(loss='mse', optimizer=opt)
                    self.models.append(new_model)

                    new_inputs = [None]*input_size
                    new_inputs[0] = 0  # Action prediction prob
                    new_inputs[1] = row['default_time'].total_seconds()  # Default time
                    if self.inclAdjParam:
                        new_inputs[2] = users_data[row['action_name']].values[0]  # time adjust for user
                        new_inputs[3] = tasks_data[row['action_name']].values[0]  # time adjustment for task
                    self.model_inputs.append(new_inputs)
                    # self.actions_info_list.append([ACTIONS.index(row['action_name']), r, prev_r_action])  # Action of focus, row no in task_data, prev robot action
                    self.actions_info_list.append({"action_idx": ACTIONS.index(row['action_name']),
                                                   "action_type": row['action_name'],
                                                   "task_data_row": r,
                                                   "prev_r_action": prev_r_action})  # Action of focus, row no in task_data, prev robot action
                    # self.output_override.append(0)

                else:
                    self.models.append("fake model")
                # self.human_row_idxs.append(index)

            elif row['user_type'] == 'robot':
                prev_r_action = r

        self.model_inputs = np.array(self.model_inputs)

        # Load normalisation parameters
        file_name = f"{folder}/lstm_input_scale_params_finalTrue_inclAllNullTrue_inclAdjParam{self.inclAdjParam}.csv"
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            scale_data = np.array(list(reader))
            self.means = scale_data[1:, 1].astype(float)
            self.scales = scale_data[1:, -1].astype(float)

    def normalise_input_data(self, input_data):
        return (input_data-self.means)/self.scales

    def action_probability_reasoning(self, action_probs, model_no, episodes):
        action_type = self.actions_info_list[model_no]["action_type"]
        # Find if required robot actions completed
        req_robo_action = self.task_data.iloc[self.actions_info_list[model_no]["prev_r_action"], self.task_data.columns.get_loc("action_name")] in episodes.action_name.values
        
        try:
            tool = self.tool_statuses[action_type]
        except KeyError:
            tool = 1
        prerequistes = req_robo_action & tool

        if prerequistes:
            weights = [1, 1]  # HAR, fastener

            # Find HAR probability
            try:
                har_prob = action_probs[self.actions_info_list[model_no]["action_idx"]]
                if har_prob == None:
                    weights[0] = 0
                    har_prob = 0
            except Exception as e:
                weights[0] = 0
                har_prob = 0

            # Find tool in use probability
            # try:
            #     tool_prob = self.tool_statuses[action_type]
            #     if tool_prob == None:
            #         weights[1] = 0
            #         tool_prob = 0
            # except Exception as e:
            #     weights[1] = 0
            #     tool_prob = 0

            # Find fastener count probability
            try:
                fastener_prob = self.fastener_probs[action_type].get_probability()
                if fastener_prob == None:
                    weights[1] = 0
                    fastener_prob = 0
            except Exception as e:
                weights[1] = 0
                fastener_prob = 0

            # Find final probability
            # action_probability = np.average([har_prob, tool_prob, fastener_prob], weights=weights)
            # print([action_type, har_prob, tool_prob, fastener_prob, action_probability])
            action_probability = np.average([har_prob, fastener_prob], weights=weights)
            print([action_type, har_prob, fastener_prob, action_probability])

        else:
            # Prerequisite robot actions not complete
            action_probability = 0
            print([action_type, req_robo_action, tool, action_probability])

        return action_probability

    def predict_action_statuses(self, action_probs):
        time = 0
        started = 1
        done = 1
        # Read episodic, prob to zero if not done.
        col_names, actions_list = self.db.query_table('Episodes', 'all')
        episodes = pd.DataFrame(actions_list, columns=col_names)
        for model_no, _ in enumerate(self.models):
            if not self.test:
                # Check if override button has been used on action
                if not self.output_override[model_no]:
                    self.model_inputs[model_no, 0] = self.action_probability_reasoning(action_probs, model_no, episodes)
                    self.model_inputs[model_no, -3:] = [time, started, done]  # Previous action status

                    input_data = self.normalise_input_data(self.model_inputs[model_no, :])
                    input_data = np.nan_to_num(np.array(input_data, ndmin=3, dtype=np.float))
                    time, started, done = self.models[model_no](input_data, training=False)[0, 0, :].numpy()
                else:
                    time, started, done = [0, 1, 1]
            else:
                [time, started, done] = [datetime.now().time(), 0, 0]

            self.task_data.loc[self.human_row_idxs[model_no], 'started'] = started
            self.task_data.loc[self.human_row_idxs[model_no], 'done'] = done
            self.task_data.loc[self.human_row_idxs[model_no], 'time_left'] = time*100

        self.publish_to_database()

    def publish_to_database(self):
        # Update user current action in sql table
        time = datetime.utcnow()
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
            '{self.task_data.loc[self.human_row_idxs[i], 'time_left']}',
            '{self.model_inputs[i, 0]}')"""
        sql_cmd += ";"
        self.db.gen_cmd(sql_cmd)

    def update_task(self, task):
        self.task = task
        col_names, actions_list = self.db.query_table(self.task, 'all',order_by='action_no')
        self.task_data = pd.DataFrame(actions_list, columns=col_names)
        self.task_data["started"] = 0
        self.task_data["done"] = 0
        self.task_data["time_left"] = datetime.now().time()
        self.human_row_idxs = self.task_data.index[self.task_data['user_type'] == 'human'].tolist()
        self.output_override = [0]*len(self.human_row_idxs)

        self.fut_act_pred_col_names, _ = self.db.query_table('future_action_predictions',rows=0,order_by='user_id')

        sql_cmd = f"""DELETE FROM future_action_predictions WHERE user_id = {self.id};"""
        self.db.gen_cmd(sql_cmd)

        self.setup_prediction_networks()
        self.setup_fastener_distribution()

    def setup_fastener_distribution(self):
        col_names, actions_list = self.db.query_table('actions', 'all')
        actions_data = pd.DataFrame(actions_list, columns=col_names)
        for action in self.fastener_probs.keys():
            act_dur = actions_data.loc[actions_data['action_name'] == action, 'std_dur_s'].iloc[0].total_seconds()
            self.fastener_probs[action] = FastenerTracker(act_dur)

    def next_action_override(self):
        # Get last updated robot actions
        col_names, robot_actions = self.db.query_table('robot_action_timings', 'all')
        last_robot_stats = pd.DataFrame(robot_actions, columns=col_names)

        # Get last action not completed by robot
        try:
            last_robot_action_no = last_robot_stats.loc[last_robot_stats["user_id"]==self.id]["last_completed_action_no"].values[0]
        except (KeyError, IndexError) as e:
            # user hasn't been entered into table yet
            last_robot_action_no = -1

        # get list of actions after last completed robot action
        if last_robot_action_no != -1:
            tasks_left = self.task_data.drop(self.task_data.index[:self.task_data.loc[self.task_data['action_no']==last_robot_action_no].first_valid_index()+1])
        else:
            tasks_left = self.task_data

        next_robot_action_idx = int(tasks_left[tasks_left['user_type']=='robot'].first_valid_index())
        # print(next_robot_action_idx)
        i = 0
        for r in range(next_robot_action_idx):
            # print(self.task_data.loc[r])
            if self.task_data.loc[r]['user_type'] == 'human':
                self.output_override[i] = 1
                i += 1

        if self.task_started:
            if self.stop:
                self.usr_fdbck_pub.publish("""STOP received. FORWARD to resume \n
                                            Waiting for next action""")
            else:
                self.usr_fdbck_pub.publish("Waiting for next action")

        print(f"OUTPUT OVERRIDE: {self.output_override}")

    def pub_episode(self, start_t, end_t, action_name):
        dur = end_t - start_t
         # Can publish new episode to sql
        self.db.insert_data_list("Episodes", 
        ["date", "start_t", "end_t", "duration", "user_id", "hand", "task_name", "action_name", "action_no"],
        [(date.today(), start_t, end_t, dur, self.id, "R", self.task, action_name, 0)])

    def gesture_handler(self, ges_idx, msg_time):
        if ges_idx == self.current_gesture[0]:
            self.current_gesture[2] = msg_time
        else:
            # Publish old gesture to episodic
            gesture = GESTURES[self.current_gesture[0]]
            if (gesture != "Null") and (gesture != "null"):
                start_t = self.current_gesture[1]
                end_t = self.current_gesture[2]
                self.pub_episode(start_t, end_t, gesture)

            # Start tracking new gesture
            last_gesture = GESTURES[self.current_gesture[0]]
            self.current_gesture[0] = ges_idx
            self.current_gesture[1] = msg_time
            self.current_gesture[2] = msg_time
            gesture = GESTURES[self.current_gesture[0]]
            if (gesture != "Null") and (gesture != "null"):
                print(f"Gesture {gesture} detected")
                if self.task_started:
                    if gesture == "Left":
                        self.cmd_publisher.publish('next_action')
                        self.usr_fdbck_pub.publish("Sorry I'm behind, next action coming!")
                    elif (gesture == "Stop") and (last_gesture == "Stop"):# and (not self.handover_action):
                        self.cmd_publisher.publish('Stop')
                        self.usr_fdbck_pub.publish("STOP received. FORWARD to resume")
                        self.stop = True
                    elif (gesture == "Forward") and self.stop:
                        self.cmd_publisher.publish('next_action')
                        self.usr_fdbck_pub.publish("Resuming")
                        self.stop = False
                else:
                    if (gesture == "Wave") and (self.name == "unknown"):
                        self.cmd_publisher.publish(f'user_identification_{self.id}')
                    elif (gesture == "Forward") and (self.name != "unknown"):
                        print("Task starting")
                        self.usr_fdbck_pub.publish("Task starting")
                        self.cmd_publisher.publish('start')

    def handover_active(self):
        self.handover_active_pub.publish(True)
        return
        activate_handover = False

        # check if stop gesture
        if self.handover_action:
            if (GESTURES[self.current_gesture[0]] == "Stop"):
                activate_handover = True

            # check if no action being performed
            if (GESTURES[self.current_gesture[0]] == "Null"):
                if (self.imu_pred_hist[-1, 1:-1] < 0.5).all():
                    activate_handover = True

        self.handover_active_pub.publish(activate_handover)

    def robot_stat_callback(self, msg):
        if msg.data == "waiting_for_handover":
            self.handover_action = True
        else:
            self.handover_action = False

    def tool_stat_callback(self, msg):
        if msg.data[0:-2] == "screwdriver":
            self.tool_statuses["screw_in"] = int(msg.data[-1])
        elif msg.data[0:-2] == "allenkey":
            self.tool_statuses["allen_in"] = int(msg.data[-1])
        elif msg.data[0:-2] == "hammer":
            self.tool_statuses["hammer"] = int(msg.data[-1])
        else:
            print(f"User unrecognised tool message: {msg.data}")

    def update_fastener_count(self, data):
        if data.UserId == self.id:
            # if user.name != data.UserName:
                # print(f"ERROR: users list name {user.name} does not match fastener_count msg name {data.UserName}")
            # else:
            if data.FastenerCount < data.LastFastenerCount:
                for key in self.fastener_probs.keys():
                    try:
                        self.fastener_probs[key].reset_timer()
                    except Exception:
                        pass
