## Make tables

## Load data into tables

## Setup ROS node

## Save table(s)

## Shutdown

## On request callbacks:
    # Retrieve episode(s)
    # Insert Episode(s)
    # Read Task memory
    # Add to task memory

import sys, os
#import rospy
#from sam_custom_messages import diagnostics
#from diagnostic_msgs.msg import KeyValue
import argparse
import traceback
from postgresql.database_funcs import database

#Define tables: tables = [{name, [col1 cmd, col2 cmd, ...]}, ]
tables_to_make = ['Tasks', 'Actions', 'Users', "Hi"]
tables = [['Tasks', ["task_id SERIAL PRIMARY KEY",
                    "task_name VARCHAR(255) NOT NULL"]], 
          ['Actions', ["action_id SERIAL PRIMARY KEY",
                    "action_name VARCHAR(255) NOT NULL",
                    "std_dur_(s) REAL"]],
          ['Users', ["user_id SERIAL PRIMARY KEY",
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
        table_avail = [item[0] for item in tables_to_make]
        assert all(elem in tables for elem in table_avail), "Some tables to make not in tables list"
        curr_tables = db.table_list()
        print(f"Tables to create: {tables_to_make}")

        for name in tables_to_make:
            
            if (name in curr_tables) and not del_tab:
                print(f"Table {name} alredy exists, leaving as is")
            else:
                if del_tab:
                    print(f"Table {name} alredy exists, deleting")
                    db.remove_table(name)
                _, cmd = [i for i in tables if i[0]==name][0]
                db.create_table(name, cmd)
                print(f"Successfully created table {name}")

    except AssertionError as e:
        print(e)
    except Exception as e:
        print(e)
        pass

def load_tables(db):
    base_dir = os.getcwd()+'/sam_nodes/scripts/postgresql/'
    
    for name in tables_to_make:
        try:
            bd.csv_import(f"{base_dir}{name}.csv", tab_name=name)
            print(f"Loaded data into {name}")
        except Exception as e:
            print(e)

def save_tables(db, tables_to_save='all', file_path=None):
    if tables_to_save == 'all':
        tables_to_save = db.table_list()
    
    for table in tables_to_save:
        try:
            db.csv_export(table, file_path=f"{file_path}/{table}.csv")
        except Exception as e:
            print(e)

    pass

def shutdown(db):
    #always save tables to dump on exit
    try:
        save_tables(db, tables_to_save='all', file_path=os.getcwd()+'/sam_nodes/scripts/postgresql/dump')
    except Exception as e:
        print(f"Dump tables error: {e}")

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
        make_tables(db)
        load_tables(db)
    except Exception as e:
        print(f"Database node create database error: {e}")

    
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

    try:
        db = database()
        database_run(db)
    #except rospy.ROSInterruptException:
    #    print("database_run ROS exception")
    except Exception as e:
        print("**Database Error**")
        traceback.print_exc(file=sys.stdout)
    finally:
        shutdown(db)
        pass