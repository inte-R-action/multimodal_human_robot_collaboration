#!/usr/bin/env python3

import sys, os
import rospy
from sam_custom_messages.msg import diagnostics
from diagnostic_msgs.msg import KeyValue
import argparse
import traceback
from postgresql.database_funcs import database

#Define tables: tables = [{name, [col1 cmd, col2 cmd, ...]}, ]
tables_to_make = ['tasks', 'actions', 'users']
tables = [['tasks', ["task_id SERIAL PRIMARY KEY",
                    "task_name VARCHAR(255) NOT NULL"]], 
          ['actions', ["action_id SERIAL PRIMARY KEY",
                    "action_name VARCHAR(255) NOT NULL",
                    "std_dur_s REAL"]],
          ['users', ["user_id SERIAL PRIMARY KEY",
                    "user_name VARCHAR(255) NOT NULL",
                    "last_active TIMESTAMPTZ"]]]

def define_diag():
    frame_id = 'Database node'
    # Diagnostic message definitions
    diag_msg = diagnostics()
    diag_msg.Header.stamp = rospy.get_rostime()
    diag_msg.Header.seq = 0
    diag_msg.Header.frame_id = frame_id
    diag_msg.UserId = 0
    diag_msg.UserName = "N/A"
    diag_msg.DiagnosticStatus.level = 1 # 0:ok, 1:warning, 2:error, 3:stale
    diag_msg.DiagnosticStatus.name = frame_id
    diag_msg.DiagnosticStatus.message = "Starting..."
    diag_msg.DiagnosticStatus.hardware_id = "N/A"
    diag_msg.DiagnosticStatus.values = []
    return diag_msg

def make_tables(db, del_tab = False):

    try:
        table_avail = [item[0] for item in tables]
        assert all(elem in table_avail for elem in tables_to_make), "Some tables to make not in tables list"
        curr_tables = db.table_list()
        print(f"Tables to create: {tables_to_make}")

        for name in tables_to_make:
            
            if (name in curr_tables) and not del_tab:
                print(f"Table '{name}' alredy exists, leaving as is")
            else:
                if del_tab:
                    print(f"Table '{name}' alredy exists, deleting")
                    db.remove_table(name)
                _, cmd = [i for i in tables if i[0]==name][0]
                db.create_table(name, cmd)
                print(f"Successfully created table '{name}'")

    except AssertionError as e:
        print(f"Assertion Error: {e}")
        raise
    except Exception as e:
        print(f"Make Tables Error: {e}")
        raise

def load_tables(db):
    base_dir = os.getcwd()+'/sam_nodes/scripts/postgresql/'
    
    for name in tables_to_make:
        try:
            db.csv_import(f"{base_dir}{name}.csv", tab_name=name)
            print(f"Loaded data into '{name}'")
        except FileNotFoundError:
            print(f"WARNING: Load table file not found for '{name}' at {base_dir}{name}.csv")
        except Exception as e:
            print(f"Load Table Error: {e}")
            raise

def save_tables(db, tables_to_save='all', file_path=None, verbose=True):
    if tables_to_save == 'all':
        tables_to_save = db.table_list(verbose=False)
    
    for table in tables_to_save:
        try:
            db.csv_export(table, file_path=f"{file_path}/{table}.csv", verbose=True)
        except Exception as e:
            if verbose:
                print(e)
            raise

def shutdown(db):
    #always save tables to dump on exit
    try:
        save_tables(db, tables_to_save='all', file_path=os.path.dirname(__file__)+'/postgresql/dump', verbose=False)
    except Exception as e:
        print(f"Dump tables error: {e}")
        raise

    print("Database node shutdown")


def database_run(db):
    # ROS node setup
    rospy.init_node(f'Database_main', anonymous=True)
    diag_msg = define_diag()
    diag_pub = rospy.Publisher('SystemStatus', diagnostics, queue_size=1)
    diag_msg.Header.stamp = rospy.get_rostime()
    diag_msg.Header.seq = 0
    diag_pub.publish(diag_msg)

    rate = rospy.Rate(1) # 1hz
    try:
        # Test connection
        db.connect(verbose=True)
        db.disconnect(verbose=True)
        # Make and load predefined tables
        make_tables(db)
        load_tables(db)
        diag_msg.DiagnosticStatus.level = 1 # ok
        diag_msg.DiagnosticStatus.message = "Tables loaded"
    except Exception as e:
        print(f"Database node create database error: {e}")
        diag_msg.DiagnosticStatus.level = 2 # error
        diag_msg.DiagnosticStatus.message = f"Error: {e}"
        raise

    diag_msg.Header.stamp = rospy.get_rostime()
    diag_msg.Header.seq += 1
    diag_pub.publish(diag_msg)

    
    while not rospy.is_shutdown():
        try:
            # Test database connection to ensure running smoothly
            db.connect()
            db.disconnect()
            diag_msg.DiagnosticStatus.level = 0 # ok
            diag_msg.DiagnosticStatus.message = "Running"
        except Exception as e:
            print(f"Database connection error: {e}")
            diag_msg.DiagnosticStatus.level = 2 # error
            diag_msg.DiagnosticStatus.message = f"Error: {e}"

        diag_msg.Header.stamp = rospy.get_rostime()
        diag_msg.Header.seq += 1
        diag_pub.publish(diag_msg)

        rate.sleep()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run database main ROS node')
    parser.add_argument('--disp', '-V',
                        help='Enable displaying of camera image',
                        default=False,
                        action="store_true")

    args = parser.parse_args()
    db = None
    try:
        db = database()
        database_run(db)
    except rospy.ROSInterruptException:
        print("database_run ROS exception")
    except Exception as e:
        print("**Database Error**")
        traceback.print_exc(file=sys.stdout)
    finally:
        if db is not None:
            shutdown(db)
        pass