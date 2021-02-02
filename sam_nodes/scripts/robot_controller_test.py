#!/usr/bin/env python3

import sys, os
import rospy
import argparse
import traceback
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class, capability_class
from sam_custom_messages.msg import capability
from postgresql.database_funcs import database
import pandas as pd
import datetime

def test_robot_control_node():
    # ROS node setup
    rospy.init_node(f'test_robot_control_node', anonymous=True)
    frame_id = 'test_robot_control_node'
    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1)
    capability_obj = capability_class(frame_id=frame_id, user_id=0)

    task_name = 'assemble_box'
    try:
        db = database()
        cols, data = db.query_table(task_name, 'all')
        task_data = pd.DataFrame(data, columns=cols)
    except Exception as e:
        print(e)
        raise e

    rate = rospy.Rate(1/10) # 1hz
    i = 0

    col_names, act_data = db.query_table('current_actions',rows=0)
    while (not rospy.is_shutdown()):# and (i < len(data)):
        try:
            capability_obj.publish(i, [task_data.loc[i]['action_name']])
            time = datetime.datetime.utcnow()

            data_ins = "%s" + (", %s"*(len(col_names)-1))
            separator = ', '
            sql_cmd = f"""INSERT INTO current_actions ({separator.join(col_names)})
            VALUES (0, 'N/A', '{time}', '{task_name}', {int(task_data.loc[i]['action_no'])}, '{time}') 
            ON CONFLICT (user_id) DO UPDATE SET updated_t='{time}', task_name='{task_name}', current_action_no={int(task_data.loc[i]['action_no'])}, start_time='{time}';"""
            db.gen_cmd(sql_cmd)

            #db.insert_data_list('current_actions', col_names, 
            #    [(0, "N/A", time, task_name, int(task_data.loc[i]['action_no']), time)])
            diag_obj.publish(0, "Running")
            
            print(task_data.loc[i])
            i=i+1
            if i == len(data):
                i=0

        except Exception as e:
            print(f"test_robot_control_node connection error: {e}")
            diag_obj.publish(2, f"Error: {e}")
            raise
        
        rate.sleep()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run test robot controller ROS node')

    args = parser.parse_args()

    try:
        test_robot_control_node()
    except rospy.ROSInterruptException:
        print("test_robot_controller ROS exception")
    except Exception as e:
        print("**test_robot_controller Error**")
        traceback.print_exc(file=sys.stdout)
    finally:
        pass