#!/usr/bin/env python3

import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import time, datetime
from PIL import Image, ImageTk
import rospy
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class, move_class
from sam_custom_messages.msg import user_prediction, capability, diagnostics, current_action
from std_msgs.msg import String
from postgresql.database_funcs import database
import os
import pandas as pd
import ttk

os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/sam_nodes/scripts"))


CATEGORIES = ['AllenKey\nIn', 'AllenKey\nOut', 'Screwing\nIn', 'Screwing\nOut', 'Null']
pos = np.arange(len(CATEGORIES))

plt.ion()

k = 0
QUIT = False

class user_frame:
    def __init__(self, no, id, name, root):
        self.no = no
        self.id = id
        self.name = name
        self.root = root
        self.imu_pred = np.zeros(5)
        self.task_name = "assemble_box"
        self.task_data = None
        self.status = "unknown"
        self.current_action_no = None

        self.fig = Figure()
        self.ax = self.fig.subplots(1, 1)

        self.db = database()

        self.create_user_frame()

        self.update_action_plot()

    def create_user_frame(self):
        self.user_frame = Tk.Frame(master=self.root, bg="red")
        self.user_frame.grid(row=0, column=self.no, sticky=Tk.N + Tk.S)

        # User Details
        self.user_deets = Tk.Text(master=self.user_frame, height=5)
        self.user_deets.grid(row=0, column=0, columnspan=3)
        self.update_user_deets()

        # Graph area for current predictions
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.user_frame)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        # Tasks List
        self.load_task_data()
        self.tasks = ttk.Treeview(self.user_frame, show=["headings"], height=18, displaycolumns="#all")
        self.tasks.grid(row=2, column=0, columnspan=3, sticky=Tk.W + Tk.E + Tk.N + Tk.S)
        self.tasks["columns"] = self.col_names

        for i in self.col_names:
            self.tasks.column(i, anchor="center", stretch=True, width=20)
            self.tasks.heading(i, text=i, anchor='center')

        for index, row in self.task_data.iterrows():
            self.tasks.insert("", index=index, values=list(row), tags=(row['action_no'],))

        # Remove User button
        self.remove_user_button = Tk.Button(master=self.user_frame, text="Remove User", command=self.remove_user, bg="red", padx=50, pady=20, height=1)
        self.remove_user_button.grid(row=3, column=0, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        # Change Task button
        self.change_task_button = Tk.Button(master=self.user_frame, text="Change Task", command=self.change_task, bg="blue", padx=50, pady=20, height=1)
        self.change_task_button.grid(row=3, column=1, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        # Restart Task button
        self.restart_task_button = Tk.Button(master=self.user_frame, text="Restart Task", command=self.restart_task, bg="green", padx=50, pady=20, height=1)
        self.restart_task_button.grid(row=3, column=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        # Adjust spacing of objects
        self.user_frame.grid_columnconfigure(0, weight=1)
        self.user_frame.grid_columnconfigure(1, weight=1)
        self.user_frame.grid_columnconfigure(2, weight=1)

        self.user_frame.grid_rowconfigure(0, weight=0)
        self.user_frame.grid_rowconfigure(1, weight=1)
        self.user_frame.grid_rowconfigure(2, weight=0)
        self.user_frame.grid_rowconfigure(3, weight=0)

    def remove_user(self):
        pass

    def change_task(self):
        pass

    def restart_task(self):
        pass

    def update_user_deets(self):
        text = f"Name: {self.name} \n " \
               f"Id: {self.id} \n " \
               f"Task: {self.task_name} \n " \
               f"Status: {self.status} \n "

        self.user_deets.delete("1.0", Tk.END)
        self.user_deets.insert(Tk.INSERT, text)
        pass

    def load_task_data(self):
        self.col_names, actions_list = self.db.query_table(self.task_name, 'all')
        self.task_data = pd.DataFrame(actions_list, columns=self.col_names)
        self.task_data["completed"] = False
        self.col_names.append("completed")

    def update_action_plot(self):
        self.ax.cla()
        self.ax.bar(pos, self.imu_pred, align='center', alpha=0.5)
        self.ax.set_xticks(pos)
        self.ax.set_xticklabels(CATEGORIES)
        self.ax.set_ylabel('Confidence')
        self.ax.set_ylim([0, 1])
        self.ax.set_title('Current IMU Prediction')

        plt.pause(0.0001)

class node_indicator:
    def __init__(self, node_name, master, i):
        self.name = node_name
        self.status = None
        self.indicator = Tk.Label(master=master, bg="grey", text=node_name, width=1, padx=10, pady=3, borderwidth=2, relief="ridge")
        self.indicator.grid(row=i%2, column=int(i/2), sticky="nsew")
        self.update_time = None


class GUI:
    def __init__(self):
        self.db = database()
        # Create GUI
        self.root = Tk.Tk()
        self.root.wm_title("HRC Interaction System")
        self.root.resizable(True, True)

        self.create_system_frame()

        self.users_deets = [[0, "unknown"], [1, "Bill"]]
        self.users = []
        i = 0
        for user in self.users_deets:
            i = i+1
            self.users.append(user_frame(i, user[0], user[1], self.root))

        self.root.grid_columnconfigure(0, weight=1)
        for i in range(len(self.users)):
            self.root.grid_columnconfigure(i+1, weight=1)
        
        self.root.grid_rowconfigure(0, weight=1)

    def create_system_frame(self):
        self.sys_frame = Tk.Frame(master=self.root, bg="dodger blue")
        self.sys_frame.grid(row=0, column=0, sticky="nsew")
        
        # Uni logo
        load = Image.open("logo.jpg")
        imsize = 100
        resized = load.resize((imsize, imsize), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resized)
        self.img = Tk.Label(self.sys_frame, image=render)#, height=imsize+10)
        self.img.image = render
        self.img.grid(row=0, column=0, columnspan=2)

        # Nodes Stats
        #self.nodes_stat_levels = []
        self.node_stats = Tk.Frame(master=self.sys_frame)#, height=40)
        self.node_stats.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.nodes_list = [['Database_node', None], 
                            ['users_node', None], 
                            ['Realsense_node', None], 
                            ['robot_control_node', None], 
                            ['hristaticdemo', None], 
                            ['gripper', None]]
        #self.nodes_indicators = []
        i=0
        for node in self.nodes_list:
            #self.nodes_indicators.append(Tk.Label(master=self.node_stats, bg="grey", text=node, width=1, padx=10, pady=3, borderwidth=2, relief="ridge"))
            #self.nodes_indicators[i].grid(row=i%2, column=int(i/2), sticky="nsew")
            #self.nodes_stat_levels.append([None, None])
            node[1] = node_indicator(node[0], self.node_stats, i)
            i += 1

        # Adjust spacing of objects
        self.node_stats.grid_columnconfigure((0, 1, 2), weight=1)
        self.node_stats.grid_rowconfigure((0, 1), weight=1)

        # Robot Status
        self.robot_stat_text = "Robot status: unknown"
        self.robot_stats = Tk.Text(master=self.sys_frame, height=2)
        self.robot_stats.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.robot_stats.insert(Tk.INSERT, self.robot_stat_text)

        # Robot Move Command
        self.robot_move_text = f"Robot Move Cmd: unknown"
        self.robot_move = Tk.Text(master=self.sys_frame, height=2)
        self.robot_move.grid(row=3, column=0, columnspan=2, sticky="nsew")
        self.robot_move.insert(Tk.INSERT, self.robot_move_text)

        # Tasks List
        self.load_task_data()
        self.tasks = ttk.Treeview(self.sys_frame, show=["headings"], height=18, displaycolumns="#all")
        self.tasks.grid(row=4, column=0, columnspan=2, sticky="nsew")
        self.tasks["columns"] = self.col_names

        for i in self.col_names:
            self.tasks.column(i, anchor="center", stretch=True, width=20)
            self.tasks.heading(i, text=i, anchor='center')

        for index, row in self.task_data.iterrows():
            self.tasks.insert("", index=index, values=list(row), tags=(row['user_id'],))

        # New User button
        self.new_user_button = Tk.Button(master=self.sys_frame, text="New User", command=self._new_user, bg="green", padx=50, pady=20)
        self.new_user_button.grid(row=5, column=0, sticky="nsew")

        # Quit button
        self.quit_button = Tk.Button(master=self.sys_frame, text="Quit", command=self._quit, bg="red", padx=50, pady=20)
        self.quit_button.grid(row=5, column=1, sticky="nsew")

        # Adjust spacing of objects
        self.sys_frame.grid_columnconfigure(0, weight=1)
        self.sys_frame.grid_columnconfigure(1, weight=1)
        
        self.sys_frame.grid_rowconfigure(0, weight=0)
        self.sys_frame.grid_rowconfigure(1, weight=0)
        self.sys_frame.grid_rowconfigure(2, weight=0)
        self.sys_frame.grid_rowconfigure(3, weight=0)
        self.sys_frame.grid_rowconfigure(4, weight=1)
        self.sys_frame.grid_rowconfigure(5, weight=0)

    def _quit(self):
        global QUIT
        QUIT = True
        self._state = 11
        rospy.signal_shutdown('Quit Button')
        self.root.quit()     # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def _new_user(self):
        pass

    def load_task_data(self):
        self.col_names, actions_list = self.db.query_table('robot_future_estimates', 'all')
        self.task_data = pd.DataFrame(actions_list, columns=self.col_names)

    def update_gui(self):

        i= 0 
        for node in self.nodes_list:
            # Check node has had initial reading
            if node[1].update_time is not None:
                # Time out on node status
                if (time.time() - node[1].update_time) > 3:
                    node[1].status = 3
                colour = "grey"
                if node[1].status == 0:
                    colour = "green"
                elif node[1].status == 1:
                    colour = "yellow"
                elif node[1].status == 2:
                    colour = "red"
                elif node[1].status == 3:
                    colour = "blue"
                else:
                    colour = "grey"
                node[1].indicator.config(bg=colour)
            i += 1

        if [node[1].status for node in self.nodes_list if node[1].name == 'Database_node'][0] == 0:
            col_names, actions_list = self.db.query_table('current_actions', 'all')
            current_data = pd.DataFrame(actions_list, columns=col_names)
            for _, row in current_data.iterrows():
                user_id = row['user_id']
                user_i = [idx for idx, user in enumerate(self.users) if user.id == user_id][0]
                if self.users[user_i].current_action_no != row['current_action_no']:
                    self.users[user_i].tasks.tag_configure(row['current_action_no'], background = 'green')
                    if self.users[user_i].current_action_no is not None:
                        self.users[user_i].tasks.tag_configure(self.users[user_i].current_action_no, background = 'grey')
                    self.users[user_i].current_action_no = row['current_action_no']

            self.load_task_data()
            self.tasks.delete(*self.tasks.get_children())
            for index, row in self.task_data.iterrows():
                self.tasks.insert("", index=index, values=list(row), tags=(row['user_id'],))


        self.robot_stats.delete("1.0", Tk.END)
        self.robot_stats.insert(Tk.INSERT, self.robot_stat_text)

        self.robot_move.delete("1.0", Tk.END)
        self.robot_move.insert(Tk.INSERT, self.robot_move_text)

        self.root.update_idletasks()
        self.root.update()

    def update_actions(self, data):
        if self.users[data.UserId].name != data.UserName:
            print(f"ERROR: users list name {self.users[data.UserId].name} does not match current_action msg name {data.UserName}")
        else:
            self.users[data.UserId].imu_pred = data.ActionProbs
            self.users[data.UserId].update_action_plot()

    def update_sys_stat(self, data):
        try:
            i = [idx for idx, sublist in enumerate(self.nodes_list) if data.Header.frame_id in sublist[0]][0]
            self.nodes_list[i][1].status = data.DiagnosticStatus.level
            self.nodes_list[i][1].update_time = time.time()
        except IndexError as e:
            pass

    def update_robot_stat(self, data):
        self.robot_stat_text = f"Robot status: {data.data}"

    def update_robot_move(self, data):
        self.robot_move_text = f"Robot Move Cmd: {data.data}"
            
            
def run_gui():
    # Run GUI
    gui = GUI()
    rospy.init_node('gui', anonymous=True)
    rospy.Subscriber('CurrentAction', current_action, gui.update_actions)
    rospy.Subscriber('SystemStatus', diagnostics, gui.update_sys_stat)
    rospy.Subscriber('RobotStatus', String, gui.update_robot_stat)
    rospy.Subscriber('RobotMove', String, gui.update_robot_move)

    while not rospy.is_shutdown():
        gui.update_gui()
        pass


if __name__ == '__main__':
    # Run ROS node
    run_gui()

