#!/usr/bin/env python3.7

import tkinter as Tk
# Implement the default Matplotlib key bindings.
import numpy as np
import time
import datetime
from PIL import Image, ImageTk
from sympy import E, EX
import rospy
from pub_classes import move_class
from std_msgs.msg import String
import os
import pandas as pd
from tkinter import ttk
import rosnode

os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/robot_blockstacking_demo/block_stacking/scripts"))


class GUI:
    def __init__(self, frame_id):
        # Create GUI
        self.root = Tk.Tk()
        # self.root = Toplevel
        self.root.wm_title("Block Stacking GUI")
        self.root.resizable(True, True)
        self.move_obj = move_class(frame_id=frame_id, queue=10)

        self.create_system_frame()

        self.root.grid_columnconfigure(0, weight=1)
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

        # Blue block
        self.new_user_button = Tk.Button(master=self.sys_frame, text="Stack Blue", command=lambda: self.stack_block("blue"), bg="blue", padx=50, pady=20)
        self.new_user_button.grid(row=1, column=0, sticky="nsew")
        # Green block
        self.new_user_button = Tk.Button(master=self.sys_frame, text="Stack Green", command=lambda: self.stack_block("green"), bg="green", padx=50, pady=20)
        self.new_user_button.grid(row=1, column=1, sticky="nsew")
        # Red block
        self.new_user_button = Tk.Button(master=self.sys_frame, text="Stack Red", command=lambda: self.stack_block("red"), bg="red", padx=50, pady=20)
        self.new_user_button.grid(row=2, column=0, sticky="nsew")
        # Yellow block
        self.new_user_button = Tk.Button(master=self.sys_frame, text="Stack Yellow", command=lambda: self.stack_block("yellow"), bg="yellow", padx=50, pady=20)
        self.new_user_button.grid(row=2, column=1, sticky="nsew")

        # Remove Stack
        self.new_user_button = Tk.Button(master=self.sys_frame, text="Remove Stack", command=self.remove_stack, bg="gray", padx=50, pady=20)
        self.new_user_button.grid(row=3, column=0, columnspan=2, sticky="nsew")

        # Quit button
        self.quit_button = Tk.Button(master=self.sys_frame, text="Quit", command=self._quit, bg="maroon", padx=50, pady=20)
        self.quit_button.grid(row=4, column=0, columnspan=2, sticky="nsew")

        # Adjust spacing of objects
        self.sys_frame.grid_columnconfigure(0, weight=1)
        self.sys_frame.grid_columnconfigure(1, weight=1)

        self.sys_frame.grid_rowconfigure(0, weight=0)
        self.sys_frame.grid_rowconfigure(1, weight=1)
        self.sys_frame.grid_rowconfigure(2, weight=1)
        self.sys_frame.grid_rowconfigure(3, weight=1)
        self.sys_frame.grid_rowconfigure(4, weight=1)

    def _quit(self):
        rospy.signal_shutdown('Quit Button')
        self.root.quit()     # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent

    def remove_stack(self):
        self.move_obj.publish('remove_stack')

    def stack_block(self, colour):
        self.move_obj.publish(f'stack_{colour}_small_block')

    def update_gui(self):
        # Update gui
        #self.root.update_idletasks()
        self.root.update()


def run_gui():
    # Run ROS node
    frame_id = 'gui_node'
    rospy.init_node(frame_id, anonymous=True)

    gui = GUI(frame_id)

    while not rospy.is_shutdown():
        try:
            gui.update_gui()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # Run GUI
    try:
        run_gui()
    except rospy.ROSInterruptException:
        pass
