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
    if data.Header.frame_id == 'Database node':
        database_stat = data.DiagnosticStatus.level
    elif data.Header.frame_id == 'users_node':
        user_node_stat = data.DiagnosticStatus.level

class future_predictor():
    def __init__(self):
        self.db = database()
        self.current_data = None
        self.fut_cols = ['user_id', 'user_name', 'task', 'action_id', 'est_t_remain', 'done']
        self.future_estimates = pd.DataFrame(columns=self.fut_cols)
        self.task_overview = None
        self.robot_status = 'Starting'
        self.robot_start_t = datetime.datetime.now().time()
        self.update_predictions()

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
            # get list of actions left incl current action
            tasks_left = task_data.drop(task_data.index[:task_data.loc[task_data[(task_data['action_no']==action_no)].first_valid_index()].name])
            # find index of next task for robot
            next_robo_action = tasks_left[tasks_left['user_type']=='robot'].first_valid_index()
            
            # sum est time until robot required
            row['start_time'] = row['start_time'].astimezone(pytz.timezone("UTC"))
            t_diff = max(datetime.datetime.now(tz=pytz.UTC)-row['start_time'], datetime.timedelta())
            time_to_robo = tasks_left.loc[:next_robo_action]['default_time'].sum() - t_diff - tasks_left.loc[next_robo_action]['default_time']
            print(tasks_left)

            i = self.future_estimates.loc[self.future_estimates['user_id']==row['user_id']].first_valid_index()
            if i is not None:
                # update if new action is gonna be next
                if next_robo_action != self.future_estimates.loc[i, 'action_id']:
                    self.future_estimates.loc[index, 'done'] = False
                self.future_estimates.loc[i] = [row['user_id'], row['user_name'], row['task_name'], next_robo_action, time_to_robo, self.future_estimates.loc[i]['done']]
                print(self.future_estimates.loc[i])
            else:
                new_user_data = [row['user_id'], row['user_name'], row['task_name'], next_robo_action, time_to_robo, False]
                self.future_estimates = self.future_estimates.append(pd.Series(new_user_data, index=self.fut_cols), ignore_index=True)
            
    def robot_stat_callback(self, data):

        if data != self.robot_status:
            print()
            date = datetime.date.today()
            end_t = datetime.datetime.now().time()
            dur = datetime.datetime.combine(date.min, end_t) - datetime.datetime.combine(date.min, self.robot_start_t)
            print(type(str(self.robot_status)))

            if data != "Done":
                # Can publish new episode to sql
                self.db.insert_data_list("Episodes", 
                ["date", "start_t", "end_t", "duration", "user_id", "hand", "capability", "task_id"], 
                [(date, self.robot_start_t, end_t, dur, 0, '-', str(self.robot_status), 0)])

            self.robot_start_t = datetime.datetime.now().time()
            self.robot_status = data


def robot_control_node():
    # ROS node setup
    rospy.init_node(f'robot_control_node', anonymous=True)
    frame_id = 'robot_control_node'
    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1)

    rospy.Subscriber("SystemStatus", diagnostics, sys_stat_callback)
    global database_stat
    # Wait for postgresql node to be ready
    while database_stat != 0 and not rospy.is_shutdown():
        print(f"Waiting for postgresql node status, currently {database_stat}")
        time.sleep(0.5)

    global user_node_stat
    # Wait for users node to be ready
    while user_node_stat != 0 and not rospy.is_shutdown():
        print(f"Waiting for users node status, currently {user_node_stat}")
        time.sleep(0.5)

    predictor = future_predictor()

    move_obj = move_class(frame_id=frame_id, queue=10)
    rospy.Subscriber("CurrentState", capability, predictor.user_prediction_callback)
    rospy.Subscriber("RobotStatus", String, predictor.robot_stat_callback)

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        try:
            predictor.update_predictions()

            for index, row in predictor.future_estimates.iterrows():
                if (row['est_t_remain'] < datetime.timedelta(seconds=5)):# and (row['done']==False):
                    action = predictor.task_overview.loc[row['action_id']]['action_name']
                    move_obj.publish(action)
                    predictor.future_estimates.loc[index, 'done'] = True
                else:
                    move_obj.publish('')

            diag_obj.publish(0, "Running")
            rospy.loginfo(f"{frame_id} active")

        except Exception as e:
            print(f"robot_control_node error: {e}")
            diag_obj.publish(2, f"Error: {e}")
        
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
