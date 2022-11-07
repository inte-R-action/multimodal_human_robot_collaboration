#!/usr/bin/env python3.7

import argparse
import os
import signal
import threading
import time
import tkinter as Tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rosnode
import rospy
from diagnostic_msgs.msg import KeyValue
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import Image, ImageTk
from sam_custom_messages.msg import current_action, diagnostics, fastener_count
from std_msgs.msg import String, Bool
from global_data import USER_PARAMETERS, ACTIONS, GESTURES, inclAdjParam
from postgresql.database_funcs import database
from pub_classes import diag_class
from system_dreaming_phase import enter_dreaming_phase
from fastener_tracker import FastenerTracker

os.chdir(os.path.expanduser(
    "~/catkin_ws/src/multimodal_human_robot_collaboration/sam_nodes/scripts"))

plt.ion()

QUIT = False


def send_shutdown_signal(diag_obj):
    print("shutdown time!")
    shutdown_window = shutting_down_window()

    x = threading.Thread(target=enter_dreaming_phase)
    x.start()

    while x.is_alive():
        shutdown_window.animate_window()

        if not x.is_alive():
            diag_obj.publish(1, "SHUTDOWN")
            time.sleep(5)

        time.sleep(0.01)

    time.sleep(1)
    shutdown_window.shutdown()
    rospy.signal_shutdown('Quit Button')


class user_frame:
    def __init__(self, no, id, name, root, cmd_publisher):
        self.no = no
        self.id = id
        self.name = name
        self.root = root
        self.act_pred = np.ones(4)
        self.ges_pred = np.ones(len(GESTURES))
        self.act_input_probs = None
        self.task_name = None
        self.task_data = None
        self.status = "unknown"
        self.destroy = False
        self.shimmer = [None, None, None]
        self.shimmer_info = []
        self.robot_comp_actions = set([])

        self.cmd_publisher = cmd_publisher
        self.cmd_publisher.publish(f'User:{self.name}')
        self.cmd_publisher.publish(f'Task:{self.task_name}')

        self.act_fig = Figure()
        self.act_ax = self.act_fig.subplots(1, 1)

        self.ges_fig = Figure()
        self.ges_ax = self.ges_fig.subplots(1, 1)

        self.act_input_fig = Figure()
        self.act_input_ax = self.act_input_fig.subplots(1, 1)

        self.db = database()

        self.create_user_frame()

        self.update_action_plot()
        self.update_gesture_plot()
        self.update_act_inputs_plot()

    def create_user_frame(self):
        self.user_frame = Tk.Frame(master=self.root, bg="red")
        self.user_frame.grid(row=0, column=1, sticky="nsew")

        self.create_user_details_frame()
        self.create_shimmer_frame()
        self.create_task_details_frame()
        self.create_actions_plots()

        self.buttons_frame = Tk.Frame(master=self.user_frame, bg="red")
        self.buttons_frame.grid(row=3, column=0, columnspan=2, sticky="nsew")

        # Remove User button
        self.remove_user_button = Tk.Button(
            master=self.buttons_frame, text="Remove User", command=self.remove_user, bg="red", padx=50, pady=20, height=1)
        self.remove_user_button.grid(row=0, column=0, sticky='nsew')

        # Next action button
        self.next_action_button = Tk.Button(
            master=self.buttons_frame, text="Next Action", command=self.next_action, bg="blue", padx=50, pady=20, height=1)
        self.next_action_button.grid(row=0, column=1, sticky='nsew')

        # Start Task button
        self.start_task_button = Tk.Button(
            master=self.buttons_frame, text="Start Task", command=self.start_task, bg="green", padx=50, pady=20, height=1)
        self.start_task_button.grid(row=0, column=2, sticky='nsew')

        self.buttons_frame.grid_columnconfigure(0, weight=1, uniform=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1, uniform=1)
        self.buttons_frame.grid_columnconfigure(2, weight=1, uniform=1)
        self.buttons_frame.grid_rowconfigure(0, weight=1)

        self.user_frame.grid_columnconfigure(0, weight=1, uniform=1)
        self.user_frame.grid_columnconfigure(1, weight=1, uniform=1)
        self.user_frame.grid_rowconfigure(0, weight=0)
        self.user_frame.grid_rowconfigure(1, weight=1)
        self.user_frame.grid_rowconfigure(2, weight=1)
        self.user_frame.grid_rowconfigure(3, weight=0)

    def create_user_details_frame(self):
        self.user_deets_frame = Tk.Frame(master=self.user_frame, bg="red", height=4)
        self.user_deets_frame.grid(row=0, column=0, sticky="nsew")

        # User Details
        self.user_deets = Tk.Text(master=self.user_deets_frame, width=1, height=4, font=('', 10))
        # self.user_deets.tag_configure("center", justify='center')
        self.user_deets.grid(row=0, column=0, sticky="nsew")
        self.update_user_deets()

        # LSTM network parameters
        self.lstm_params_txt = Tk.Text(master=self.user_deets_frame, width=1, height=4, font=('', 10))
        self.lstm_params_txt.tag_configure("right", justify='right')
        self.lstm_params_txt.grid(row=0, column=1, sticky="nsew")
        self.update_lstm_params_txt()

        # Adjust spacing of objects
        self.user_deets_frame.grid_columnconfigure(0, weight=1)
        self.user_deets_frame.grid_columnconfigure(1, weight=1)
        self.user_deets_frame.grid_rowconfigure(0, weight=0)

    def create_task_details_frame(self):
        # Tasks List
        self.task_frame = Tk.Frame(master=self.user_frame, bg="red")
        self.task_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.col_names = ["action_no","action_id","action_name","default_time","user_type","prev_dependent","started","done","t_left"]

        self.tasks = ttk.Treeview(self.task_frame, show=["headings"], height=38, displaycolumns="#all")
        self.tasks.grid(row=0, column=0, sticky='nsew')
        self.tasks["columns"] = self.col_names

        for i in self.col_names:
            self.tasks.column(i, anchor="center", stretch=True, width=2)
            self.tasks.heading(i, text=i, anchor='center')

        if self.task_name is not None:
            self.load_task_data()

        # Graph area for current action predictions
        self.act_input_canvas = FigureCanvasTkAgg(self.act_input_fig, master=self.task_frame)
        self.act_input_canvas.draw()
        self.act_input_canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew")

        # Adjust spacing of objects
        self.task_frame.grid_columnconfigure(0, weight=1, uniform=1)
        self.task_frame.grid_columnconfigure(1, weight=1, uniform=1)
        self.task_frame.grid_rowconfigure(0, weight=1)

    def create_shimmer_frame(self):
        # Shimmer status indicators
        self.shimmer_frame = Tk.Frame(master=self.user_frame, bg="red", height=4)
        self.shimmer_frame.grid(row=0, column=1, sticky="nsew")
        for i in range(0, 3):
            self.shimmer[i] = Tk.Text(master=self.shimmer_frame, height=4, width=2, font=('', 10))
            self.shimmer[i].tag_configure("center", justify='center')
            self.shimmer[i].grid(row=0, column=i, sticky="nsew")
            text = "\nUnknown shimmer\n" \
                   "Unknown"
            self.shimmer_info.append([text, 'Unknown'])

        self.update_shimmer_text()

        self.shimmer_frame.grid_rowconfigure(0, weight=0)
        self.shimmer_frame.grid_columnconfigure(0, weight=1, uniform=1)
        self.shimmer_frame.grid_columnconfigure(1, weight=1, uniform=1)
        self.shimmer_frame.grid_columnconfigure(2, weight=1, uniform=1)

    def create_actions_plots(self):
        # Graph area for current action predictions
        # A tk.DrawingArea.
        self.act_canvas = FigureCanvasTkAgg(self.act_fig, master=self.user_frame)
        self.act_canvas.draw()
        self.act_canvas.get_tk_widget().grid(row=2, column=0, sticky="nsew")

        # Graph area for current gesture predictions
        # A tk.DrawingArea.
        self.ges_canvas = FigureCanvasTkAgg(self.ges_fig, master=self.user_frame)
        self.ges_canvas.draw()
        self.ges_canvas.get_tk_widget().grid(row=2, column=1, sticky="nsew")

    def remove_user(self):
        self.user_frame.quit()     # stops mainloop
        self.user_frame.destroy()  # this is necessary on Windows to prevent
        self.destroy = True

    def next_action(self):
        self.cmd_publisher.publish('next_action')

    def start_task(self):
        self.cmd_publisher.publish('start')

    def update_shimmer_text(self):
        for i in range(len(self.shimmer_info)):
            IMU_MSGS = ['ERROR', 'Ready', 'Unknown', 'Shutdown', 'Starting', 'Connecting', 'Initialising']
            colour = "grey"
            if self.shimmer_info[i][1] == IMU_MSGS[1]:
                colour = "green"
            elif (self.shimmer_info[i][1] == IMU_MSGS[4]) or (self.shimmer_info[i][1] == IMU_MSGS[5]) or (self.shimmer_info[i][1] == IMU_MSGS[6]):
                colour = "yellow"
            elif self.shimmer_info[i][1] == IMU_MSGS[0]:
                colour = "red"
            elif self.shimmer_info[i][1] == IMU_MSGS[2]:
                colour = "blue"
            else:
                colour = "grey"
            self.shimmer[i].config(bg=colour)

            self.shimmer[i].delete("1.0", Tk.END)
            self.shimmer[i].insert(Tk.INSERT, self.shimmer_info[i][0])
            self.shimmer[i].tag_add("center", "1.0", "end")

    def update_lstm_params_txt(self):
        if inclAdjParam:
            col_names, data = self.db.query_table('users', 'all')
            users_data = pd.DataFrame(data, columns=col_names)
            users_data = users_data.loc[users_data['user_name']==self.name]
            col_names, data = self.db.query_table('tasks', 'all')
            tasks_data = pd.DataFrame(data, columns=col_names)
            tasks_data = tasks_data.loc[tasks_data['task_name']==self.task_name]

            user_params = users_data[ACTIONS].values[0].round(1)  # time adjust for user
            task_params = tasks_data[ACTIONS].values[0].round(1)  # time adjustment for task
        else:
            user_params = ["N/A"]*len(ACTIONS)
            task_params = ["N/A"]*len(ACTIONS)

        text = "LSTM Params:                        " \
               "User|Task \n"
        text = text+''.join([f"{action}:  {user_params[a]} |  {task_params[a]} \n" for a, action in enumerate(ACTIONS)])

        self.lstm_params_txt.delete("1.0", Tk.END)
        self.lstm_params_txt.insert(Tk.INSERT, text)
        self.lstm_params_txt.tag_add("right", "1.0", "end")

    def update_user_deets(self):
        text = f" Name: {self.name} \n" \
               f"       Id: {self.id} \n" \
               f"  Task: {self.task_name} \n" \
               f"Status: {self.status} \n"

        self.user_deets.delete("1.0", Tk.END)
        self.user_deets.insert(Tk.INSERT, text)

    def load_task_data(self):
        self.col_names, actions_list = self.db.query_table(self.task_name, 'all')
        self.task_data = pd.DataFrame(actions_list, columns=self.col_names)
        for row in self.task_data.itertuples():
            self.task_data.at[row.Index, 'default_time'] = round(row.default_time.total_seconds(), 2)
        self.task_data["started"] = 0
        self.task_data["done"] = 0
        self.task_data["t_left"] = 0
        self.col_names.extend(("started", "done", "t_left"))

        self.act_input_probs = np.zeros(self.task_data.shape[0])
        self.update_act_inputs_plot()

    def update_action_plot(self):
        self.act_ax.cla()
        pos = np.arange(len(ACTIONS))
        _ = self.act_ax.bar(pos, self.act_pred, align='center', alpha=0.5)

        try:
            self.act_ax.set_xticks(pos)
            self.act_ax.set_xticklabels(ACTIONS)
        except Exception as e:
            print(e)
        self.act_ax.set_ylabel('Confidence')
        self.act_ax.set_ylim([0, 1])
        self.act_ax.set_title('Current Action Prediction')

        plt.pause(0.00001)
        if not QUIT:
            self.act_canvas.draw_idle()

    def update_gesture_plot(self):
        self.ges_ax.cla()
        pos = np.arange(len(GESTURES))
        _ = self.ges_ax.bar(pos, self.ges_pred, align='center', alpha=0.5)

        try:
            self.ges_ax.set_xticks(pos)
            self.ges_ax.set_xticklabels(GESTURES)
        except Exception as e:
            print(e)
        self.ges_ax.set_ylabel('Confidence')
        self.ges_ax.set_ylim([0, 1])
        self.ges_ax.set_title('Current Gesture Prediction')

        plt.pause(0.00001)
        if not QUIT:
            self.ges_canvas.draw_idle()

    def update_act_inputs_plot(self):
        self.act_input_ax.cla()
        data_height = 30
        if self.task_data is not None:
            pos = np.arange(data_height)
            display_data = np.zeros(data_height)
            display_data[0:self.act_input_probs.shape[0]] = self.act_input_probs
            self.bar_list = self.act_input_ax.barh(pos, display_data, align='center', alpha=0.5, height=0.8)
            self.act_input_ax.invert_yaxis()
        else:
            pos = np.arange(data_height)
            data = pos
            self.bar_list = self.act_input_ax.barh(pos, data, align='center', alpha=0.5, height=0.8, tick_label=None)
            self.act_input_ax.invert_yaxis()

        self.act_input_ax.set_xlim([0, 1])
        self.act_input_ax.set_ylim([data_height, -0.5])
        self.act_input_ax.set_title('Action Prob Inputs', fontsize=10)

        plt.pause(0.00001)
        if not QUIT:
            self.act_input_canvas.draw_idle()

    def update_user_information(self, name):
        self.name = name
        self.task_name = USER_PARAMETERS[name]
        self.update_user_deets()
        self.load_task_data()


class node_indicator:
    def __init__(self, node_name, master, i):
        self.name = node_name
        self.status = None
        self.indicator = Tk.Label(master=master, bg="grey", text=node_name, width=10,
                                   padx=10, pady=3, borderwidth=2, relief="ridge")
        self.indicator.grid(row=int(i/2), column=i%2, sticky="nsew")
        self.update_time = None


class new_user_dialogue(object):
    def __init__(self, parent):
        self.fcancel = False
        self.toplevel = Tk.Toplevel(parent)
        self.toplevel.geometry('350x150')
        self.toplevel.resizable(False, False)
        self.var = Tk.StringVar()

        db = database()
        col_names, users = db.query_table('users', 'all')
        users = pd.DataFrame(users, columns=col_names)
        self.default = "Select User"
        options = [self.default]
        for _, row in users.iterrows():
            options.append((row['user_id'], row['user_name']))

        options = tuple(options)
        label = Tk.Label(self.toplevel, text="Choose New User:", height=1, padx=50, pady=2, anchor='center')
        om = ttk.OptionMenu(self.toplevel, self.var, options[0], *options)
        ok_button = Tk.Button(self.toplevel, text="OK", command=self.toplevel.destroy, width=10, height=1, padx=30, pady=10, anchor='center')
        cancel_button = Tk.Button(self.toplevel, text="Cancel", command=self.cancel, width=10, height=1, padx=30, pady=10, anchor='center')

        label.grid(row=0, column=0, columnspan=2)#, sticky="nsew")
        om.grid(row=1, column=0, columnspan=2)#, sticky="nsew")
        ok_button.grid(row=2, column=0)#, sticky="nsew")
        cancel_button.grid(row=2, column=1)#, sticky="nsew")

        # Adjust spacing of objects
        self.toplevel.grid_columnconfigure(0, weight=1)
        self.toplevel.grid_columnconfigure(1, weight=1)
        self.toplevel.grid_rowconfigure(0, weight=1)
        self.toplevel.grid_rowconfigure(1, weight=1)
        self.toplevel.grid_rowconfigure(2, weight=1)

    def cancel(self):
        self.fcancel = True
        self.toplevel.destroy()

    def show(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        value = self.var.get()
        if self.fcancel or (value == self.default):
            return None
        else:
            return value


class shutting_down_window():
    def __init__(self):
        self.Window_Width = 800
        self.Window_Height = 600
        self.im_size = 100
        self.xinc = self.yinc = 4

        # Create GUI
        self.root = Tk.Tk()
        self.root.wm_title("Shutting Down...")
        self.root.geometry(f'{self.Window_Width}x{self.Window_Height}')

        label = Tk.Label(self.root, text="Dreaming State")
        label.config(font=("Courier", 20))
        label.pack(fill=Tk.BOTH)

        self.canvas = Tk.Canvas(self.root)
        self.canvas.configure(bg="Blue")
        self.canvas.pack(fill="both", expand=True)
        self.animate_ball()

    def shutdown(self):
        self.root.quit()
        self.root.destroy()

    def animate_ball(self):
        image = Image.open("dreaming.png")
        image = image.resize((self.im_size, self.im_size), Image.ANTIALIAS)
        self.the_image = ImageTk.PhotoImage(image)
        self.image = self.canvas.create_image(400, 300, anchor=Tk.NW, image=self.the_image)
        self.animate_window()

    def animate_window(self):
        self.canvas.move(self.image, self.xinc, self.yinc)
        self.root.update()
        ball_pos = self.canvas.coords(self.image)
        # unpack array to variables
        x, y = ball_pos
        if x < abs(self.xinc) or (x+self.im_size) > self.Window_Width-abs(self.xinc):
            self.xinc = -self.xinc
        if y < abs(self.yinc) or (y+self.im_size) > self.Window_Height-abs(self.yinc):
            self.yinc = -self.yinc


class GUI:
    def __init__(self, cmd_publisher):
        self.db = database()
        # Create GUI
        self.root = Tk.Tk()
        # self.root = Toplevel
        self.root.wm_title("HRC Interaction System")
        self.root.resizable(True, True)
        self.cmd_publisher = cmd_publisher

        self.create_system_frame()

        self.users = []
        self.users.append(user_frame(len(self.users)+1, 1, "unknown", self.root, self.cmd_publisher))

        self.root.grid_columnconfigure(0, weight=1)
        for i in range(len(self.users)):
            self.root.grid_columnconfigure(i+1, weight=1, uniform=1)

        self.root.grid_rowconfigure(0, weight=1)

    def create_system_frame(self):
        self.sys_frame = Tk.Frame(master=self.root, bg="dodger blue")
        self.sys_frame.grid(row=0, column=0, sticky="nsew")

        # Uni logo
        load = Image.open("logo.jpg")
        imsize = 100
        resized = load.resize((imsize, imsize), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image=resized)
        self.img = Tk.Label(master=self.sys_frame, image=render)
        self.img.image = render
        self.img.grid(row=0, column=0, columnspan=2)

        # Nodes Stats Indicators
        self.node_stats = Tk.Frame(master=self.sys_frame)
        self.node_stats.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.nodes_list = [['Database_node', None],
                           ['users_node', None],
                           ['skeleton_viewer', None],
                           ['robot_control_node', None],
                           ['hri_static_demo', None],
                           ['rq_gripper_2F140', None],
                           ['tool_sensor', None],
                           ['Realsense_node', None]]
        i = 0
        for node in self.nodes_list:
            node[1] = node_indicator(node[0], self.node_stats, i)
            i += 1

        # Adjust spacing of objects
        self.node_stats.grid_columnconfigure((0, 1), weight=1)
        self.node_stats.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Robot Status Text
        self.robot_stat_text = "Robot status: unknown"
        self.robot_stats = Tk.Text(master=self.sys_frame, height=2)
        self.robot_stats.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.robot_stats.insert(Tk.INSERT, self.robot_stat_text)

        # Robot Move Command Text
        self.robot_move_text = "Robot Move Cmd: unknown"
        self.robot_move = Tk.Text(master=self.sys_frame, height=2)
        self.robot_move.grid(row=3, column=0, columnspan=2, sticky="nsew")
        self.robot_move.insert(Tk.INSERT, self.robot_move_text)

        # Tasks List
        self.load_robot_actions_data()
        self.tasks = ttk.Treeview(self.sys_frame, show=[
                                  "headings"], height=18, displaycolumns="#all")
        self.tasks.grid(row=4, column=0, columnspan=2, sticky="nsew")
        self.tasks["columns"] = self.col_names

        for i in self.col_names:
            if i == "last_completed_action_no":
                txt = "prev action no"
            elif i == "user_id":
                txt = "id"
            elif i == "user_name":
                txt = "name"
            else:
                txt = i
            self.tasks.column(i, anchor="center", stretch=True, width=8*len(txt))
            self.tasks.heading(i, text=txt, anchor='center')

        for index, row in self.robot_tasks_data.iterrows():
            self.tasks.insert("", index=index, values=list(
                row), tags=(row['user_id'],))

        # Fastener counter
        self.setup_fastenercounter()

        # Handover active indicator
        self.handover_active = False
        self.handover_label = Tk.Label(master=self.sys_frame, bg="grey", text="Handover Active",
                                   padx=10, pady=3, borderwidth=2, relief="ridge")
        self.handover_label.grid(row=6, column=0, columnspan=2, sticky="nsew")

        # Tool Stats Indicators
        self.tool_statuses = {"screwdriver": None, "allenkey": None, "hammer": None}
        self.tool_stats = Tk.Frame(master=self.sys_frame)
        self.tool_stats.grid(row=7, column=0, columnspan=2, sticky="nsew")
        self.screwdriver_ind = Tk.Label(master=self.tool_stats, bg="grey", text="Screwdriver",
                                   padx=10, pady=3, borderwidth=2, relief="ridge")
        self.screwdriver_ind.grid(row=0, column=0, sticky="nsew")
        self.allen_ind = Tk.Label(master=self.tool_stats, bg="grey", text="Allen Key",
                                   padx=10, pady=3, borderwidth=2, relief="ridge")
        self.allen_ind.grid(row=0, column=1, sticky="nsew")
        self.hammer_ind = Tk.Label(master=self.tool_stats, bg="grey", text="Hammer",
                                   padx=10, pady=3, borderwidth=2, relief="ridge")
        self.hammer_ind.grid(row=0, column=2, sticky="nsew")
        # Adjust spacing of objects
        self.tool_stats.grid_columnconfigure((0, 1, 2), weight=1)
        self.tool_stats.grid_rowconfigure(0, weight=1)

        # User Feedback Text
        self.usr_feedback_text = "Please wait, system starting"
        self.usr_feedback = Tk.Text(master=self.sys_frame, font=("Courier", 14), wrap='word', height=10, width=20)
        self.usr_feedback.tag_configure("feedback_tag_center", justify='center')
        self.usr_feedback.grid(row=8, column=0, columnspan=2, sticky="nsew")
        self.usr_feedback.insert(Tk.INSERT, self.usr_feedback_text)

        # New User button
        self.new_user_button = Tk.Button(master=self.sys_frame, text="New User", command=self._new_user, bg="green", padx=50, pady=20)
        self.new_user_button.grid(row=9, column=0, sticky="nsew")

        # Quit button
        self.quit_button = Tk.Button(master=self.sys_frame, text="Quit", command=self._quit, bg="red", padx=50, pady=20)
        self.quit_button.grid(row=9, column=1, sticky="nsew")

        # Adjust spacing of objects
        self.sys_frame.grid_columnconfigure(0, weight=1, uniform=1)
        self.sys_frame.grid_columnconfigure(1, weight=1, uniform=1)

        self.sys_frame.grid_rowconfigure(0, weight=0)
        self.sys_frame.grid_rowconfigure(1, weight=0)
        self.sys_frame.grid_rowconfigure(2, weight=0)
        self.sys_frame.grid_rowconfigure(3, weight=0)
        self.sys_frame.grid_rowconfigure(4, weight=1)
        self.sys_frame.grid_rowconfigure(5, weight=1)
        self.sys_frame.grid_rowconfigure(6, weight=0)
        self.sys_frame.grid_rowconfigure(7, weight=0)
        self.sys_frame.grid_rowconfigure(8, weight=1)
        self.sys_frame.grid_rowconfigure(9, weight=0)

    def setup_fastenercounter(self):
        self.fastener_frame = Tk.Frame(master=self.sys_frame, bg="dodger blue")
        self.fastener_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")

        self.fastener_counts = [None, None]
        self.fastener_count_txt = Tk.Text(master=self.fastener_frame, height=4, width=2, font=('', 12))
        self.fastener_count_txt.tag_configure("center", justify='center')
        self.fastener_count_txt.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.fastener_probs = {"screw_in": None,
                               "allen_in": None,
                               "hammer": None}

        col_names, actions_list = self.db.query_table('actions', 'all')
        actions_data = pd.DataFrame(actions_list, columns=col_names)
        for action in self.fastener_probs.keys():
            act_dur = actions_data.loc[actions_data['action_name'] == action, 'std_dur_s'].iloc[0].total_seconds()
            self.fastener_probs[action] = FastenerTracker(act_dur)

        self.screw_prob_txt = Tk.Text(master=self.fastener_frame, height=2, width=1, font=('', 10))
        self.screw_prob_txt.tag_configure("center", justify='center')
        self.screw_prob_txt.grid(row=1, column=0, sticky="nsew")

        self.allen_prob_txt = Tk.Text(master=self.fastener_frame, height=2, width=1, font=('', 10))
        self.allen_prob_txt.tag_configure("center", justify='center')
        self.allen_prob_txt.grid(row=1, column=1, sticky="nsew")

        self.hammer_prob_txt = Tk.Text(master=self.fastener_frame, height=2, width=1, font=('', 10))
        self.hammer_prob_txt.tag_configure("center", justify='center')
        self.hammer_prob_txt.grid(row=1, column=2, sticky="nsew")

        # Adjust spacing of objects
        self.fastener_frame.grid_columnconfigure(0, weight=1, uniform=1)
        self.fastener_frame.grid_columnconfigure(1, weight=1, uniform=1)
        self.fastener_frame.grid_columnconfigure(2, weight=1, uniform=1)
        self.fastener_frame.grid_rowconfigure(0, weight=1)
        self.fastener_frame.grid_rowconfigure(1, weight=1)

        self.update_fastener_count_txt()

    def _quit(self):
        self.cmd_publisher.publish('stop')
        global QUIT
        QUIT = True
        self.root.quit()     # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent

    def _new_user(self):
        user = new_user_dialogue(self.root).show()
        if user is not None:
            user = eval(user)
            self.users.append(user_frame(len(self.users)+1, user[0], user[1], self.root, self.cmd_publisher))
            self.fig.clf()
            self.axs = np.reshape(self.fig.subplots(len(self.users)+1, 1, sharex='col'), (-1, 1))  # subplot for each user plus robot

    def load_robot_actions_data(self):
        self.col_names, actions_list = self.db.query_table('robot_action_timings', 'all')
        self.robot_tasks_data = pd.DataFrame(actions_list, columns=self.col_names)
        for row in self.robot_tasks_data.itertuples():
            self.robot_tasks_data.at[row.Index, 'robot_start_t'] = max(0.0, round(row.robot_start_t.total_seconds(), 2))

    def update_gui(self, diag_obj):
        try:
            # destroy any removed users
            for i, _ in enumerate(self.users):
                try:
                    if self.users[i].destroy:
                        del self.users[i]
                        self.fig.clf()
                        self.axs = np.reshape(self.fig.subplots(len(self.users)+1, 1, sharex='col'), (-1,1))  # subplot for each user plus robot
                except IndexError:
                    pass

            # Update node status indicators
            for node in self.nodes_list:
                # Check node has had initial reading
                if node[1].update_time is not None:
                    # Time out on node status
                    if (time.time() - node[1].update_time) > 10:
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

            # If postgresql node running
            if [node[1].status for node in self.nodes_list if node[1].name == 'Database_node'][0] == 0:
                # Update robot actions
                self.load_robot_actions_data()
                self.tasks.delete(*self.tasks.get_children())
                for index, row in self.robot_tasks_data.iterrows():
                    self.tasks.insert("", index=index, values=list(row), tags=(row['user_id'],))

                # Update future prediction user data tables
                col_names, predictions_list = self.db.query_table('future_action_predictions', 'all')
                predictions_data = pd.DataFrame(predictions_list, columns=col_names)
                for row in predictions_data.itertuples():
                    try:
                        user_id = row.user_id
                        user_i = [idx for idx, user in enumerate(self.users) if user.id == user_id]
                        if len(user_i) != 0:
                            user_i = user_i[0]
                            if self.users[user_i].task_data is not None:
                                self.users[user_i].task_data.loc[self.users[user_i].task_data['action_no'] == row.action_no, 'started'] = round(row.started, 2)
                                self.users[user_i].task_data.loc[self.users[user_i].task_data['action_no'] == row.action_no, 'done'] = round(row.done, 2)
                                self.users[user_i].task_data.loc[self.users[user_i].task_data['action_no'] == row.action_no, 't_left'] = round(row.time_left, 2)
                                self.users[user_i].act_input_probs[row.action_no] = row.act_input_prob
                    except Exception as e:
                        print(e)
                        print("gui 649")

                for _, user in enumerate(self.users):
                    user.tasks.delete(*user.tasks.get_children())
                    if user.task_data is not None:
                        for index, row in user.task_data.iterrows():
                            user.tasks.insert("", index=index, values=list(row), tags=(row['action_no'],))

                    try:
                        act_no_next = self.robot_tasks_data[self.robot_tasks_data['user_id'] == user.id]['next_r_action_no'].values[0]
                        user.tasks.tag_configure(act_no_next, background='yellow')
                        user.act_input_probs[act_no_next] = 0.5
                        act_no_done = self.robot_tasks_data[self.robot_tasks_data['user_id'] == user.id]['last_completed_action_no'].values[0]
                        user.tasks.tag_configure(act_no_done, background='green')
                        user.act_input_probs[act_no_done] = 1
                    except Exception as e:
                        pass

                    user.update_act_inputs_plot()
                    
                    try:
                        if act_no_next is not None:
                            user.bar_list[act_no_next].set_color('yellow')
                        if act_no_done is not None:
                            user.robot_comp_actions.add(act_no_done)
                        [user.bar_list[done_bar].set_color('green') for done_bar in user.robot_comp_actions]
                    except Exception as e:
                        pass

                # Update future timings plot
                # self.update_timings_plot(predictions_data)

            # Update user info and status
            for user in self.users:
                user.update_shimmer_text()
                # user.user_deets.delete("1.0", Tk.END)
                # user.user_deets.insert(Tk.INSERT, user.details_text)
                # try:
                #     user.canvas.draw_idle()
                # except:
                #     pass
                # user.user_frame.update_idletasks()
                # user.user_frame.update()

            # Update robot status text
            self.robot_stats.delete("1.0", Tk.END)
            self.robot_stats.insert(Tk.INSERT, self.robot_stat_text)

            # Update robot move cmd text
            self.robot_move.delete("1.0", Tk.END)
            self.robot_move.insert(Tk.INSERT, self.robot_move_text)

            # Update fastener count text
            self.update_fastener_count_txt()

            # Update handover active indicator
            if self.robot_stat_text == "Robot status: waiting_for_handover":
                if self.handover_active:
                    self.handover_label.config(bg='green')
                else:
                    self.handover_label.config(bg='yellow')
            else:
                self.handover_label.config(bg='red')

            # Update tools in use indicators
            try:
                if self.tool_statuses["screwdriver"] is None:
                    self.screwdriver_ind.config(bg='blue')
                elif self.tool_statuses["screwdriver"]:
                    self.screwdriver_ind.config(bg='green')
                else:
                    self.screwdriver_ind.config(bg='red')

                if self.tool_statuses["allenkey"] is None:
                    self.allen_ind.config(bg='blue')
                elif self.tool_statuses["allenkey"]:
                    self.allen_ind.config(bg='green')
                else:
                    self.allen_ind.config(bg='red')

                if self.tool_statuses["hammer"] is None:
                    self.hammer_ind.config(bg='blue')
                elif self.tool_statuses["hammer"]:
                    self.hammer_ind.config(bg='green')
                else:
                    self.hammer_ind.config(bg='red')
            except Exception as e:
                print(f"GUI tool ind error: {e}")

            # Update user feedback text
            self.usr_feedback.delete("1.0", Tk.END)
            self.usr_feedback.insert(Tk.INSERT, self.usr_feedback_text)
            self.usr_feedback.tag_add("feedback_tag_center", "1.0", "end")

            # Configure layout and update plots
            # self.root.grid_columnconfigure(0, weight=1)
            # for i in range(len(self.users)):
            #     self.root.grid_columnconfigure(i+1, weight=1)
            # self.root.grid_rowconfigure(0, weight=1)

            # Update gui
            diag_obj.publish(0, "Running")
        except Exception as e:
            print(e)
            print("gui 701")
            diag_obj.publish(2, f"Error: {e}")

        # update every 0.5 s
        if not QUIT:
            self.root.after(500, lambda: self.update_gui(diag_obj))

    def update_actions(self, data):
        for user in self.users:
            if data.UserId == user.id:
                # if user.name != data.UserName:
                #     try:
                #         print(f"ERROR: users list name {self.users[data.UserId-1].name} does not match current_action msg name {data.UserName}")
                #     except IndexError as e:
                #         print(f"ERROR with {self.users}, {data.UserId}, {data.UserName}")
                # else:
                if data.Header.frame_id[-8:] == '_actions':
                    user.act_pred = data.ActionProbs
                    user.update_action_plot()
                elif data.Header.frame_id[-9:] == '_gestures':
                    user.ges_pred = data.ActionProbs
                    user.update_gesture_plot()

    def update_sys_stat(self, data):
        try:
            i = [idx for idx, sublist in enumerate(self.nodes_list) if data.Header.frame_id in sublist[0]][0]
            self.nodes_list[i][1].status = data.DiagnosticStatus.level
            self.nodes_list[i][1].update_time = time.time()
        except IndexError:
            pass

        for user in self.users:
            if data.Header.frame_id[0:11] == f'shimmerBase':
                i = 0
                for keyval in data.DiagnosticStatus.values[:-1]:
                    text = f"\n{keyval.key}\n" \
                            f"{keyval.value}\n"
                    user.shimmer_info[i] = [text, keyval.value]
                    i += 1

    def update_robot_stat(self, data):
        self.robot_stat_text = f"Robot status: {data.data}"

    def update_robot_move(self, data):
        self.robot_move_text = f"Robot Move Cmd: {data.data}"

    def update_handover_active(self, data):
        self.handover_active = data.data

    # def update_timings_plot(self, predictions_data):
    #     active_users = self.users
    #     [ax[0].cla() for ax in self.axs]

    #     for u in range(self.axs.shape[0]-1):
    #         time_predictions = predictions_data.loc[predictions_data["user_id"]==active_users[u].id]["time_left"]
    #         for t in time_predictions:
    #             self.axs[u, 0].axvline(x=t)
    #         try:
    #             self.axs[u, 0].get_yaxis().set_ticks([])
    #         except Exception:
    #             pass
    #         self.axs[u, 0].set_ylabel(f"User: {u}")

    #     # Plot robot solo action times
    #     try:
    #         time_predictions = self.robot_tasks_data.loc[self.robot_tasks_data["user_name"]=="robot"]["robot_start_t"].values[0]
    #         self.axs[-1, 0].axvline(x=time_predictions)
    #     except (KeyError, IndexError) as e:
    #         # print("robot solo action time error")
    #         pass
    #     try:
    #         self.axs[-1, 0].get_yaxis().set_ticks([])
    #     except Exception:
    #         pass
    #     self.axs[-1, 0].set_ylabel("Robot Solo")

    #     self.fig.text(0.5, 0.02, 'Time into future, s', ha='center')
    #     self.fig.suptitle('Future Timing Predictions')

    #     plt.pause(0.00001)

    def update_usr_feedback(self, data):
        if data.data != self.usr_feedback_text:
            self.usr_feedback_text = data.data
            if data.data[0:5] == "Hello":
                self.users[0].update_user_information(data.data[6:-1])

    def tool_stat_callback(self, msg):
        try:
            i = [idx for idx, sublist in enumerate(self.nodes_list) if 'tool_sensor' in sublist[0]][0]
            self.nodes_list[i][1].status = 0
            self.nodes_list[i][1].update_time = time.time()
        
            if msg.data[0:-2] == "screwdriver":
                self.tool_statuses["screwdriver"] = int(msg.data[-1])
            elif msg.data[0:-2] == "allenkey":
                self.tool_statuses["allenkey"] = int(msg.data[-1])
            elif msg.data[0:-2] == "hammer":
                self.tool_statuses["hammer"] = int(msg.data[-1])
            else:
                self.nodes_list[i][1].status = 2
                print(f"GUI unrecognised tool message: {msg.data}")
        
        except IndexError:
            pass

    def update_fastener_count_txt(self):
        text = f"\nFastener Counts\n" \
               f"Last: {self.fastener_counts[1]}     Now: {self.fastener_counts[0]}\n" \

        self.fastener_count_txt.delete("1.0", Tk.END)
        self.fastener_count_txt.insert(Tk.INSERT, text)
        self.fastener_count_txt.tag_add("center", "1.0", "end")

        prob = self.fastener_probs['screw_in'].get_probability()
        self.screw_prob_txt.delete("1.0", Tk.END)
        self.screw_prob_txt.insert(Tk.INSERT, f"Screw: {round(prob, 2)}")
        self.screw_prob_txt.tag_add("center", "1.0", "end")

        prob = self.fastener_probs['allen_in'].get_probability()
        self.allen_prob_txt.delete("1.0", Tk.END)
        self.allen_prob_txt.insert(Tk.INSERT, f"Allen: {round(prob, 2)}")
        self.allen_prob_txt.tag_add("center", "1.0", "end")

        prob = self.fastener_probs['hammer'].get_probability()
        self.hammer_prob_txt.delete("1.0", Tk.END)
        self.hammer_prob_txt.insert(Tk.INSERT, f"Hammer: {round(prob, 2)}")
        self.hammer_prob_txt.tag_add("center", "1.0", "end")

    def update_fastener_count(self, data):
        # if data.UserId == user.id:
            # if user.name != data.UserName:
            #     print(f"ERROR: users list name {user.name} does not match fastener_count msg name {data.UserName}")
            # else:
        self.fastener_counts = [data.FastenerCount, data.LastFastenerCount]
        if data.FastenerCount < data.LastFastenerCount:
            for key in self.fastener_probs.keys():
                self.fastener_probs[key].reset_timer()


def run_gui():
    # Run ROS node
    frame_id = 'gui_node'
    rospy.init_node(frame_id, anonymous=True)

    diag_obj = diag_class(frame_id=frame_id, user_id=0, user_name="N/A", queue=1)
    cmd_publisher = rospy.Publisher('ProcessCommands', String, queue_size=10)
    diag_obj.publish(1, "Starting")

    gui = GUI(cmd_publisher)

    def handler(signum, frame):
        print('Signal handler called with signal', signum)
        gui._quit()

    signal.signal(signal.SIGINT, handler)
    rospy.Subscriber('CurrentAction', current_action, gui.update_actions)
    rospy.Subscriber('SystemStatus', diagnostics, gui.update_sys_stat)
    rospy.Subscriber('RobotStatus', String, gui.update_robot_stat)
    rospy.Subscriber('RobotMove', String, gui.update_robot_move)
    rospy.Subscriber('UserFeedback', String, gui.update_usr_feedback)
    rospy.Subscriber('HandoverActive', Bool, gui.update_handover_active)
    rospy.Subscriber('ToolStatus', String, gui.tool_stat_callback)
    rospy.Subscriber("FastenerCounts", fastener_count, gui.update_fastener_count)

    gui.update_gui(diag_obj)
    Tk.mainloop()

    if QUIT:
        send_shutdown_signal(diag_obj)


if __name__ == '__main__':
    # Run GUI
    try:
        run_gui()
    except rospy.ROSInterruptException:
        pass
