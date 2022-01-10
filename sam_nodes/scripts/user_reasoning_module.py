#!/usr/bin/env python3.7

#import rospy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from postgresql.database_funcs import database
from tensorflow.keras.models import load_model
plt.ion()

MODEL_FILE = ""


class reasoning_module:
    def __init__(self, name, id, frame_id, ACTION_CATEGORIES):
        self.name = name
        self.id = id
        self.frame_id = frame_id
        self.task_data = None
        self.task = None
        self.models = []
        self.human_row_idxs = []
        self.db = database()

        pass

    def setup_prediction_networks(self):
        for index, row in self.task_data.iterrows():
            if row['user_type'] == 'human':
                self.models.append(load_model(MODEL_FILE))
                self.human_row_idxs.append(index)
        pass

    def predict_action_statuses(self):
        for i in range(len(self.models)):
            [time, started, done] = self.models[i].predict()
            self.task_data.loc[self.human_row_idxs[i], 'started'] = started
            self.task_data.loc[self.human_row_idxs[i], 'done'] = done
            self.task_data.loc[self.human_row_idxs[i], 'time_left'] = time
        
        self.publish_to_database()
        pass

    def publish_to_database(self):
        # Update user current action in sql table
        time = datetime.datetime.utcnow()
        #data_ins = "%s" + (", %s"*(len(self.col_names)-1))
        separator = ', '
        sql_cmd = f"""INSERT INTO current_actions ({separator.join(self.col_names)})
        VALUES ({self.id}, '{self.name}', '{time}', '{self.task}', {int(self.task_data.loc[self.curr_action_no]['action_no'])}, '{time}') 
        ON CONFLICT (user_id) DO UPDATE SET updated_t='{time}', task_name='{self.task}', current_action_no={int(self.task_data.loc[self.curr_action_no]['action_no'])}, start_time='{time}';"""
        self.db.gen_cmd(sql_cmd)
        pass

    def update_task(self, task):
        self.task = task
        col_names, actions_list = self.db.query_table(self.task, 'all')
        self.task_data = pd.DataFrame(actions_list, columns=col_names)
        self.task_data["started"] = 0
        self.task_data["done"] = 0
        self.task_data["time_left"] = 0
        
        self.setup_prediction_networks()

