#!/usr/bin/env python3

import sys, os
import rospy
import argparse
import traceback
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class, future_class
from sam_custom_messages.msg import user_prediction, capability
from postgresql.database_funcs import database
import pandas as pd

def test_robot_control_node():
    # ROS node setup
    rospy.init_node(f'test_robot_control_node', anonymous=True)
    frame_id = 'test_robot_control_node'
    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1)

    try:
        db = database()
        cols, data = db.query_table('assemble_box', 'all')
        task_data = pd.DataFrame(data, columns=cols)
    except Exception as e:
        raise e

    rate = rospy.Rate(1/15) # 1hz
    i = 0
    while (not rospy.is_shutdown()) and (i < len(data)):
        try:
            diag_obj.publish(0, "Running")
            print(task_data.loc[i])
            i=i+1

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