#!/usr/bin/env python3

import sys, os
import rospy
import argparse
import traceback
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class, move_class
from sam_custom_messages.msg import user_prediction, capability
from postgresql.database_funcs import database
import pandas as pd

class future_predictor():
    def __init__(self):
        self.db = database()
        self.current_data = None
        self.future_estimates = pd.DataFrame([], columns=['user_id', 'user_name', 'task', 'action_id', 'est_t_remain'])
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
            # current action id number wrt task
            action_no = row['current_action_no']
            # get list of actions left incl current action
            tasks_left = task_data.drop(task_data.index[:task_data.loc[task_data[(task_data['action_no']==action_no)].first_valid_index()].name])
            # find index of next task for robot
            next_robo_action = tasks_left.loc[tasks_left['user_type']=='robot'].first_valid_index()
            # sum est time until robot required
            time_to_robo = tasks_left['default_time'][:next_robo_action].sum()

            i = self.future_estimates.loc[self.future_estimates['user_id']==row['user_id']].first_valid_index()
            if i is not None:
                self.future_estimates.loc[i] = [row['user_id'], row['user_name'], row['task'], next_robo_action, time_to_robo]
            else:
                self.future_estimates.append([row['user_id'], row['user_name'], row['task'], next_robo_action, time_to_robo], ignore_index=True)
            

def robot_control_node():
    # ROS node setup
    rospy.init_node(f'robot_control_node', anonymous=True)
    frame_id = 'robot_control_node'
    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1)

    predictor = future_predictor()

    move_obj = move_class(frame_id=frame_id, queue=1)
    rospy.Subscriber("CurrentState", capability, predictor.user_prediction_callback)

    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        try:
            diag_obj.publish(0, "Running")
        except Exception as e:
            print(f"robot_control_node connection error: {e}")
            diag_obj.publish(2, f"Error: {e}")
        
        rate.sleep()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run robot controller ROS node')
    parser.add_argument('--test', '-T',
                        help='Send test sequence of movements',
                        default=False,
                        action="store_true")

    args = parser.parse_args()

    try:
        robot_control_node()
    except rospy.ROSInterruptException:
        print("robot_controller ROS exception")
    except Exception as e:
        print("**robot_controller Error**")
        traceback.print_exc(file=sys.stdout)
    finally:
        pass