#!/usr/bin/env python3.7

import numpy as np
import time
import pandas as pd
from postgresql.database_funcs import database
from datetime import date, datetime
from statistics import mean, stdev
import os
from global_data import num_chair_actions, num_box_actions, ACTIONS

os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/sam_nodes/scripts"))
db = database()


def read_episodic_memory():
    # Get session episodic data
    col_names, data = db.query_table('episodes', 'all')
    episodic_data = pd.DataFrame(data, columns=col_names)
    return episodic_data


def read_users_memory():
    # Get active users data
    col_names, data = db.query_table('users', 'all')
    users_data = pd.DataFrame(data, columns=col_names)
    return users_data


def get_users_meta_data(episodic_data, actions_meta_data):
    users_data = read_users_memory()
    users = episodic_data.user_id.unique()
    users_meta_data = dict([(n, [[] for _ in range(len(ACTIONS))]) for n in users])

    for user in users:
        user_episodic_data = episodic_data.loc[episodic_data["user_id"]==user]
        actions = user_episodic_data.action_name.unique()

        for a in range(len(actions)):
            action = actions[a]
            total_time = sum([t.total_seconds() for t in user_episodic_data.loc[user_episodic_data["action_name"]==action]["duration"]])
            task = user_episodic_data["task_name"][0]
            if task == 'assemble_chair':
                ave_time = total_time/num_box_actions[action]
            elif task == 'assemble_complex_box':
                ave_time = total_time/num_chair_actions[action]

            actions_meta_data[action].append(ave_time)
            users_meta_data[user][a] = ave_time

    return actions_meta_data, users_meta_data


def write_users_metadata(users_meta_data):
    for user_name in users_meta_data:
        print(f"User: {user_name}")
        file_name = f"models_parameters/metadata_users_{user_name}.csv"
        try:
            user_df = pd.read_csv(file_name)
        except FileNotFoundError:
            print("New File")
            user_df = pd.DataFrame(columns=['date', 'time']+list(ACTIONS))
        columns = list(user_df.columns)
        new_user_df = pd.DataFrame(columns=columns)
        new_user_df = new_user_df.append({'date': date.today()}, ignore_index=True)

        new_user_df['time'] = datetime.now().time()
        user_df = user_df.append(new_user_df)
        user_df.to_csv(file_name, index=False)
        print(user_df)


def get_tasks_meta_data(episodic_data, actions_meta_data):
    tasks = episodic_data.task_name.unique()
    tasks_meta_data = dict([(n, [[] for _ in range(len(ACTIONS))]) for n in set(tasks)])
    for task in tasks:
        task_episodic_data = episodic_data.loc[episodic_data["task_name"]==task]
        actions = task_episodic_data.action_name.unique()

        for a in range(len(actions)):
            action = actions[a]
            total_time = sum([t.total_seconds() for t in task_episodic_data.loc[task_episodic_data["action_name"]==action]["duration"]])
            task = task_episodic_data["task_name"][0]
            if task == 'assemble_chair':
                ave_time = total_time/num_box_actions[action]
            elif task == 'assemble_complex_box':
                ave_time = total_time/num_chair_actions[action]

            actions_meta_data[action].append(ave_time)
            tasks_meta_data[task][a] = ave_time

    return actions_meta_data, tasks_meta_data
        

def write_tasks_metadata(tasks_meta_data):
    for task in tasks_meta_data:
        print(f"Task: {task}")
        file_name = f"models_parameters/metadata_tasks_{task}.csv"
        try:
            task_df = pd.read_csv(file_name)
        except FileNotFoundError:
            print("New File")
            task_df = pd.DataFrame(columns=['date', 'time']+list(ACTIONS))
        columns = list(task_df.columns)
        new_task_df = pd.DataFrame(columns=columns)
        new_task_df = new_task_df.append({'date': date.today()}, ignore_index=True)

        new_task_df['time'] = datetime.now().time()
        task_df = task_df.append(new_task_df)
        task_df.to_csv(file_name, index=False)
        print(task_df)


def write_actions_metadata(actions_meta_data):
    print("Actions metadata writer")
    file_name = "models_parameters/metadata_actions.csv"
    try:
        actions_df = pd.read_csv(file_name)
    except FileNotFoundError:
        print("New File")
        actions_df = pd.DataFrame(columns=['date', 'time']+list(ACTIONS))
    columns = list(actions_df.columns)
    new_actions_df = pd.DataFrame(columns=columns)
    new_actions_df = new_actions_df.append({'date': date.today()}, ignore_index=True)

    new_actions_df['time'] = datetime.now().time()
    actions_df = actions_df.append(new_actions_df)
    actions_df.to_csv(file_name, index=False)
    print(actions_df)


def update_matedata_tables(actions_meta_data, users_meta_data, tasks_meta_data):
    for a in range(len(ACTIONS)):
        action = ACTIONS[a]
        mean_t = mean(actions_meta_data[action])  # mean action time overall
        std_t = stdev(actions_meta_data[action])  # std dev action time overall

        for user in users_meta_data:
            users_meta_data[user][action] = mean(users_meta_data[user][action])  # mean action time per user
            users_meta_data[user][action] = (users_meta_data[user][action]-mean_t)/std_t  # normalise data

        for task in tasks_meta_data:
            tasks_meta_data[task][action] = mean(tasks_meta_data[task][action])  # mean action time per task
            tasks_meta_data[task][action] = (tasks_meta_data[task][action]-mean_t)/std_t  # normalise data

        actions_meta_data[action] = mean_t

        write_users_metadata(users_meta_data)
        write_tasks_metadata(tasks_meta_data)
        write_actions_metadata(actions_meta_data)


def enter_dreaming_phase():
    print("Entering dreaming phase")
    # Fake shutdown timer
    t = time.time()
    while (time.time()-t) < 3:
        time.sleep(0.1)

    episodic_data = read_episodic_memory()

    actions_meta_data = dict([(n, []) for n in ACTIONS])
    actions_meta_data, users_meta_data = get_users_meta_data(episodic_data, actions_meta_data)
    actions_meta_data, tasks_meta_data = get_tasks_meta_data(episodic_data, actions_meta_data)

    update_matedata_tables(actions_meta_data, users_meta_data, tasks_meta_data)


if __name__=='__main__':
    enter_dreaming_phase()
