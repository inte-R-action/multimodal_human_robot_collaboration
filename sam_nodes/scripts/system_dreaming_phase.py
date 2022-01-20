#!/usr/bin/env python3.7

import rospy
import numpy as np
import time
import pandas as pd
from postgresql.database_funcs import database
from datetime import date, datetime
from statistics import mean
import os


os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/sam_nodes/scripts"))
db = database()


def read_episodic_memory():
    # Get predictions from user reasoning
    col_names, data = db.query_table('episodes', 'all')
    episodic_data = pd.DataFrame(data, columns=col_names)
    return episodic_data


def read_users_memory():
    # Get predictions from user reasoning
    col_names, data = db.query_table('users', 'all')
    users_data = pd.DataFrame(data, columns=col_names)
    return users_data


def update_users_meta_data(episodic_data):
    users_data = read_users_memory()
    users = episodic_data.user_id.unique()
    for user in users:
        user_name = users_data.loc[users_data["user_id"]==user]["user_name"].values[0]
        print(f"User: {user} {user_name}")
        file_name = f"User_{user}_{user_name}_metadata.csv"

        user_episodic_data = episodic_data.loc[episodic_data["user_id"]==user]
        actions = user_episodic_data.action_name.unique()
        try:
            user_df = pd.read_csv(file_name)
        except FileNotFoundError:
            print("New File")
            user_df = pd.DataFrame(columns=['date', 'time']+list(actions))

        columns = list(user_df.columns)
        new_user_df = pd.DataFrame(columns=columns)
        new_user_df = new_user_df.append({'date': date.today()}, ignore_index=True)
        for action in actions:
            new_user_df[action] = mean([t.total_seconds() for t in user_episodic_data.loc[user_episodic_data["action_name"]==action]["duration"]])

        new_user_df['time'] = datetime.now().time()
        user_df = user_df.append(new_user_df)
        user_df.to_csv(file_name, index=False)
        print(user_df)


def update_tasks_meta_data(episodic_data):
    tasks = episodic_data.task_name.unique()
    for task in tasks:
        print(f"Task: {task}")
        file_name = f"Task_{task}_metadata.csv"

        task_episodic_data = episodic_data.loc[episodic_data["task_name"]==task]
        actions = task_episodic_data.action_name.unique()
        try:
            task_df = pd.read_csv(file_name)
        except FileNotFoundError:
            print("New File")
            task_df = pd.DataFrame(columns=['date', 'time']+list(actions))

        columns = list(task_df.columns)
        new_task_df = pd.DataFrame(columns=columns)
        new_task_df = new_task_df.append({'date': date.today()}, ignore_index=True)
        for action in actions:
            new_task_df[action] = mean([t.total_seconds() for t in task_episodic_data.loc[task_episodic_data["action_name"]==action]["duration"]])

        new_task_df['time'] = datetime.now().time()
        task_df = task_df.append(new_task_df)
        task_df.to_csv(file_name, index=False)
        print(task_df)


def enter_dreaming_phase():
    print("Entering dreaming phase")
    ### Fake shutdown timer
    t = time.time()
    while (time.time()-t) < 3:
        time.sleep(0.1)

    episodic_data = read_episodic_memory()
    update_users_meta_data(episodic_data)
    update_tasks_meta_data(episodic_data)


if __name__=='__main__':
    enter_dreaming_phase()
