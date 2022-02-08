#!/usr/bin/env python3.7

import numpy as np
import time
import pandas as pd
from postgresql.database_funcs import database
from datetime import date, datetime
from statistics import StatisticsError, mean, stdev
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
    user_ids = episodic_data.user_id.unique()
    users_meta_data = {n: [[] for _ in range(len(ACTIONS))] for n in user_ids}
    user_names = {n: users_data.loc[users_data['user_id'] == n]['user_name'].values[0] for n in user_ids}

    for user in user_ids:
        user_episodic_data = episodic_data.loc[episodic_data["user_id"] == user]
        actions = user_episodic_data.action_name.unique()

        for a, action in enumerate(ACTIONS):
            total_time = sum([t.total_seconds() for t in user_episodic_data.loc[user_episodic_data["action_name"] == action]["duration"]])
            task = user_episodic_data["task_name"].values[0]
            if task == 'assemble_chair':
                ave_time = total_time/num_box_actions[action]
            elif task == 'assemble_complex_box':
                ave_time = total_time/num_chair_actions[action]

            if ave_time == 0:
                ave_time = float("nan")
            actions_meta_data[action].append(ave_time)
            users_meta_data[user][a] = ave_time

    return actions_meta_data, users_meta_data, user_names


def write_users_metadata(users_meta_data, user_names):
    for user_id in users_meta_data:
        print(f"User id: {user_id} User name: {user_names[user_id]}")
        file_name = f"models_parameters/metadata_users_{user_names[user_id]}.csv"
        try:
            user_df = pd.read_csv(file_name)
        except FileNotFoundError:
            print("New File")
            user_df = pd.DataFrame(columns=['date', 'time']+list(ACTIONS))
        columns = list(user_df.columns)
        new_user_df = pd.DataFrame(columns=columns)
        new_user_df = new_user_df.append({'date': date.today()}, ignore_index=True)

        for a in range(len(ACTIONS)):
            new_user_df[ACTIONS[a]] = users_meta_data[user_id][a]

        new_user_df['time'] = datetime.now().time()
        user_df = user_df.append(new_user_df)
        user_df.to_csv(file_name, index=False)
        print(user_df)


def get_tasks_meta_data(episodic_data, actions_meta_data):
    tasks = episodic_data.task_name.unique()
    tasks_meta_data = {n: [[] for _ in range(len(ACTIONS))] for n in set(tasks)}
    for task in tasks:
        task_episodic_data = episodic_data.loc[episodic_data["task_name"] == task]
        actions = task_episodic_data.action_name.unique()

        for a, action in enumerate(ACTIONS):
            total_time = sum([t.total_seconds() for t in task_episodic_data.loc[task_episodic_data["action_name"] == action]["duration"]])
            if task == 'assemble_chair':
                ave_time = total_time/num_box_actions[action]
            elif task == 'assemble_complex_box':
                ave_time = total_time/num_chair_actions[action]

            if ave_time == 0:
                ave_time = float("nan")
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
        for a, action in enumerate(ACTIONS):
            new_task_df[action] = tasks_meta_data[task][a]

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

    for action in ACTIONS:
        new_actions_df[action] = actions_meta_data[action]

    actions_df = actions_df.append(new_actions_df)
    actions_df.to_csv(file_name, index=False)
    print(actions_df)


def update_matedata_tables(actions_meta_data, users_meta_data, tasks_meta_data, user_names):
    print(actions_meta_data)
    for a, action in enumerate(ACTIONS):
        try:
            mean_t = mean(actions_meta_data[action])  # mean action time overall
        except StatisticsError:
            mean_t = 0
        try:
            std_t = stdev(actions_meta_data[action])  # std dev action time overall
            if std_t == 0:
                std_t = 1
        except StatisticsError:
            std_t = 1
        actions_meta_data[action] = mean_t
    write_actions_metadata(actions_meta_data)

    base_meta_data = pd.read_csv("models_parameters/base_training_meta_data.csv")

    for a, action in enumerate(ACTIONS):
        mean_t = base_meta_data.loc[base_meta_data['actions'] == 'default_timings_mean'][action].values[0]
        std_t = base_meta_data.loc[base_meta_data['actions'] == 'default_timings_std'][action].values[0]
        for user in users_meta_data:
            # users_meta_data[user][a] = mean(user[action])  # mean action time per user
            users_meta_data[user][a] = (users_meta_data[user][a]-mean_t)/std_t  # normalise data

        for task in tasks_meta_data:
            # tasks_meta_data[task][action] = mean(tasks_meta_data[task][action])  # mean action time per task
            tasks_meta_data[task][a] = (tasks_meta_data[task][a]-mean_t)/std_t  # normalise data

    write_users_metadata(users_meta_data, user_names)
    write_tasks_metadata(tasks_meta_data)


def enter_dreaming_phase():
    print("Entering dreaming phase")
    # Fake shutdown timer
    t = time.time()
    while (time.time()-t) < 3:
        time.sleep(0.1)

    episodic_data = read_episodic_memory()

    actions_meta_data = {n: [] for n in ACTIONS}
    actions_meta_data, users_meta_data, user_names = get_users_meta_data(episodic_data, actions_meta_data)
    actions_meta_data, tasks_meta_data = get_tasks_meta_data(episodic_data, actions_meta_data)
    print(users_meta_data)
    print(tasks_meta_data)
    update_matedata_tables(actions_meta_data, users_meta_data, tasks_meta_data, user_names)


if __name__ == '__main__':
    enter_dreaming_phase()
