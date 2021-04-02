#!/usr/bin/env python3.7

import sys, os
import rospy
import argparse
import traceback
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class, move_class
from sam_custom_messages.msg import user_prediction, capability, diagnostics
from std_msgs.msg import String
from postgresql.database_funcs import database
import pandas as pd
import datetime, time
import pytz
os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/"))

database_stat = 1
user_node_stat = 1
def sys_stat_callback(data):
    global database_stat
    global user_node_stat
    if data.Header.frame_id == 'Database_node':
        database_stat = data.DiagnosticStatus.level
    elif data.Header.frame_id == 'users_node':
        user_node_stat = data.DiagnosticStatus.level

class future_predictor():
    def __init__(self):
        self.db = database()
        self.current_data = None
        self.fut_cols = ['user_id', 'user_name', 'task_name', 'current_action_no', 'est_t_remain', 'robo_task_t', 'robot_start_t', 'done']
        self.future_estimates = pd.DataFrame(columns=self.fut_cols)
        self.task_overview = None
        self.robot_status = None
        self.robot_start_t = datetime.datetime.now().time()
        self.update_predictions()
        self.task_now = None
        self.action_no_now = None
        self.done = False

    def user_prediction_callback(self, data):
        self.update_predictions()

    def update_predictions(self):
        col_names, actions_list = self.db.query_table('current_actions', 'all')
        self.current_data = pd.DataFrame(actions_list, columns=col_names)

        for index, row in self.current_data.iterrows():
            # Get actions list for task user is doing
            task_cols, task_actions = self.db.query_table(row['task_name'], 'all')
            task_data = pd.DataFrame(task_actions, columns=task_cols)
            self.task_overview = task_data
            # current action id number wrt task
            action_no = row['current_action_no']

            while True:
                # get list of actions left incl current action
                tasks_left = task_data.drop(task_data.index[:task_data.loc[task_data[(task_data['action_no']==action_no)].first_valid_index()].name])
                # find index of next task for robot
                next_robo_action = int(tasks_left[tasks_left['user_type']=='robot'].first_valid_index())
                
                # sum est time until robot action required
                row['start_time'] = row['start_time'].astimezone(pytz.timezone("UTC"))
                t_diff = min(max(datetime.datetime.now(tz=pytz.UTC)-row['start_time'], datetime.timedelta()), tasks_left.iloc[0]['default_time'])
                time_to_robo = max(tasks_left.loc[:next_robo_action]['default_time'].sum() - t_diff - tasks_left.loc[next_robo_action]['default_time'], datetime.timedelta())
                time_to_robo = (datetime.datetime.min + time_to_robo).time()
                print(f"\nUser {row['user_name']} Tasks Left:")
                print(tasks_left,"\n")
                print(f"useraction no: {action_no}")

                # find time to when robo action can start
                date = datetime.date.today()
                time2robostart = datetime.datetime.combine(date.min, time_to_robo) - datetime.datetime.combine(date.min, (datetime.datetime.min + self.task_overview.loc[next_robo_action]['default_time']).time())
                
                #time2robostart = (datetime.datetime.min + time2robostart).time()
                
                i = self.future_estimates.loc[self.future_estimates['user_id'] == row['user_id']].first_valid_index()
                task_time = (datetime.datetime.min + self.task_overview.loc[next_robo_action]['default_time']).time()
                if i is not None:
                    # update if new action is gonna be next
                    if next_robo_action != self.future_estimates.loc[i, 'current_action_no']:
                        self.future_estimates.loc[index, 'done'] = False
                        self.future_estimates.loc[i] = [row['user_id'], row['user_name'], row['task_name'], next_robo_action, 
                                                        time_to_robo, task_time, time2robostart, self.future_estimates.loc[i]['done']]
                        print(f"\nFuture Estimates:")
                        print(self.future_estimates,"\n")
                        return
                    # elif self.future_estimates.loc[index, 'done'] == True:
                    #     action_no += 1
                    #     print("robot action number >>> ", action_no)
                    else:
                        print(f"\nFuture Estimates:")
                        print(self.future_estimates,"\n")
                        return
                    #print(self.future_estimates.loc[i])
                else:
                    new_user_data = [row['user_id'], row['user_name'], row['task_name'], next_robo_action, time_to_robo, task_time, time2robostart, False]
                    self.future_estimates = self.future_estimates.append(pd.Series(new_user_data, index=self.fut_cols), ignore_index=True)
                    return

    def robot_stat_callback(self, msg):
        print(f"######################################robot stat callback: {msg.data} {self.robot_status} {self.task_now} {self.action_no_now}")
        if msg.data == 'Done':
            self.update_episodic()
            self.done = True

        self.robot_status = msg.data

    def update_episodic(self):
        date = datetime.date.today()
        end_t = datetime.datetime.now().time()
        dur = datetime.datetime.combine(date.min, end_t) - datetime.datetime.combine(date.min, self.robot_start_t)

        if (self.robot_status != "Done") and (self.robot_status != "Waiting") and (self.robot_status != None):
            # Can publish new episode to sql
            self.db.insert_data_list("Episodes", 
            ["date", "start_t", "end_t", "duration", "user_id", "hand", "task_name", "action_name", "action_no"], 
            [(date, self.robot_start_t, end_t, dur, 0, '-', self.task_now, str(self.robot_status), self.action_no_now)])
            self.task_now = None
            self.action_no_now = None


class robot_solo_task():
    def __init__(self):
        self.db = database()
        self.task_name = "stack_tower"
        self.task_overview = None
        self.next_action_id = 0
        self.next_action = None
        self.next_task_time = None
        self.finished = False
        
        self.update_task_data()

    def update_task_data(self):
        task_cols, task_actions = self.db.query_table(self.task_name, 'all')
        self.task_overview = pd.DataFrame(task_actions, columns=task_cols)

        self.next_action_id = 0
        self.next_action = self.task_overview.loc[self.task_overview['action_no']==self.next_action_id, ['action_name']].values[0][0]
        self.next_task_time = pd.Timedelta(self.task_overview.loc[self.task_overview['action_no']==self.next_action_id, ['default_time']].values[0][0])

    def update_progress(self):
        try:
            self.next_action_id += 1
            self.next_action = self.task_overview.loc[self.task_overview['action_no']==self.next_action_id, ['action_name']].values[0][0]
            self.next_task_time = pd.Timedelta(self.task_overview.loc[self.task_overview['action_no']==self.next_action_id, ['default_time']].values[0][0])
        except IndexError:
            print(f"Looks like user robot task is finished")
            self.finished = True

def robot_control_node():
    # ROS node setup
    frame_id = 'robot_control_node'
    rospy.init_node(frame_id, anonymous=True)
    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="robot", queue=1)
    diag_obj.publish(1, "Starting")

    rospy.Subscriber("SystemStatus", diagnostics, sys_stat_callback)
    global database_stat
    # Wait for postgresql node to be ready
    while database_stat != 0 and not rospy.is_shutdown():
        print(f"Waiting for postgresql node status, currently {database_stat}")
        diag_obj.publish(1, "Waiting for postgresql node")
        time.sleep(0.5)

    global user_node_stat
    # Wait for users node to be ready
    while user_node_stat != 0 and not rospy.is_shutdown():
        print(f"Waiting for users node status, currently {user_node_stat}")
        diag_obj.publish(1, "Waiting for users node")
        time.sleep(0.5)

    predictor = future_predictor()
    robot_task = robot_solo_task()

    move_obj = move_class(frame_id=frame_id, queue=10)
    rospy.Subscriber("CurrentState", capability, predictor.user_prediction_callback)
    rospy.Subscriber("RobotStatus", String, predictor.robot_stat_callback)

    rate = rospy.Rate(1) # 1hz
    db = database()
    home = False
    while not rospy.is_shutdown():
        try:
            predictor.update_predictions()

            # Update future prediction in sql table
            for _, row in predictor.future_estimates.iterrows():
                sql_cmd = f"""DELETE FROM robot_future_estimates WHERE user_id = {row['user_id']};"""
                db.gen_cmd(sql_cmd)
                db.insert_data_list("robot_future_estimates", predictor.fut_cols, [tuple(row.tolist())])

            # Select row with minimum time until robot required
            row = predictor.future_estimates[predictor.future_estimates.robot_start_t == predictor.future_estimates.robot_start_t.min()]

            if (row['robot_start_t'][0] < pd.Timedelta(0)) and (row['done'][0]==False):
                home = False
                # if time to next colab < action time start colab action
                action = predictor.task_overview.loc[row['current_action_no']]['action_name'].values[0]
                predictor.task_now = row['task_name'][0]
                predictor.action_no_now = row['current_action_no'][0]
                print(f"action: {action}")
                while predictor.robot_status != action:
                    move_obj.publish(action)
                predictor.robot_start_t = datetime.datetime.now().time()
                predictor.done = False
                while not predictor.done:
                    time.sleep(0.01)
                predictor.future_estimates.loc[predictor.future_estimates['user_id']==row['user_id'].values[0], 'done'] = True

            elif ((row['robot_start_t'][0] > robot_task.next_task_time) and (not robot_task.finished)) or (row['done'][0]==True):
                home = False
                # if time to colb action > time to do solo action
                predictor.task_now = robot_task.task_name
                predictor.action_no_now = robot_task.next_action_id
                print(f"Robot solo task {robot_task.next_action}")
                while predictor.robot_status != robot_task.next_action:
                    move_obj.publish(robot_task.next_action)
                predictor.robot_start_t = datetime.datetime.now().time()
                predictor.done = False
                while not predictor.done:
                    time.sleep(0.01)
                robot_task.update_progress()
                
            elif not home:
                # else wait for next colab action
                predictor.task_now = None
                predictor.action_no_now = None
                print(f"Sending robot home")
                while predictor.robot_status != 'home':
                    move_obj.publish('home')
                predictor.robot_start_t = datetime.datetime.now().time()
                predictor.done = False
                while not predictor.done:
                    time.sleep(0.01)
                # move_obj.publish('')
                home = True

            diag_obj.publish(0, "Running")
            rospy.loginfo(f"{frame_id} active")

        except Exception as e:
            print(f"robot_control_node error: {e}")
            diag_obj.publish(2, f"Error: {e}")
            traceback.print_exc(file=sys.stdout)
        
        rate.sleep()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run robot controller ROS node')
    parser.add_argument('--test', '-T',
                        help='Send test sequence of movements',
                        default=False,
                        action="store_true")

    args = parser.parse_known_args()[0]

    try:
        robot_control_node()
    except rospy.ROSInterruptException:
        print("robot_controller ROS exception")
    except Exception as e:
        print("**robot_controller Error**")
        traceback.print_exc(file=sys.stdout)
    finally:
        pass
