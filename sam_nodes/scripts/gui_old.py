#!/usr/bin/env python3

import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import time
from PIL import Image, ImageTk
import rospy
from imu_vision_interaction.msg import gui_msg
from std_msgs.msg import Int8


CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
pos = np.arange(len(CATEGORIES))

plt.ion()

fig = Figure()
axs = fig.subplots(2, 2)
k = 0
QUIT = False


class GUI:
    def __init__(self):
        self._no_completed = 0
        self._state = 0
        self._msg_timer = time.time()
        self._prt_done = False
        self._timer_flag = False
        self._sys_stat = 2
        self._state_est_final = np.zeros((1, 2))
        self._state_est_im = np.zeros((1, 2))
        self._state_est_imu = np.zeros((1, 2))
        self._imu_stat = [2, 2, 2, 2]
        self._im_stat = 2
        self._pub = rospy.Publisher('completed_parts', Int8, queue_size=10)
        self._imu_pred = np.zeros(5)
        self._im_pred = np.zeros(2)

        # Create GUI
        self.root = Tk.Tk()
        self.root.wm_title("IMU and Vision Interaction System")
        self.root.resizable(True, True)
        # Graph area for current predictions
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=4, columnspan=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        # Message object for prompts to user
        self.message_obj = Tk.Text(master=self.root, width=70, height=2, pady=20)
        self.message_obj.tag_add("center", "1.0", "end")
        self.message_obj.tag_configure("center", justify="center")
        self.message_obj.grid(row=4, column=0, columnspan=2)

        # Uni logo
        load = Image.open("logo.jpg")
        resized = load.resize((100, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resized)
        self.img = Tk.Label(self.root, image=render, width=200)
        self.img.image = render
        self.img.grid(row=0, column=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        right_width = 25
        # System status message box
        self.status_obj = Tk.Text(master=self.root, width=right_width)
        self.status_obj.grid(row=1, column=2)
        # No. completed screws/bolts/parts box
        self.counter_obj = Tk.Text(master=self.root, width=right_width, height=10)
        self.counter_obj.grid(row=2, column=2)
        # Manual next part button
        self.next_button = Tk.Button(master=self.root, text="Next Part", command=self._next_part, bg="green", padx=50, pady=20)
        self.next_button.grid(row=3, column=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)
        # Quit button
        self.quit_button = Tk.Button(master=self.root, text="Quit", command=self._quit, bg="red", padx=50, pady=20)
        self.quit_button.grid(row=4, column=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)
        # Adjust spacing of objects
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=3)
        self.root.grid_rowconfigure(2, weight=2)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

    def _quit(self):
        global QUIT
        QUIT = True
        self._state = 11
        rospy.signal_shutdown('Quit Button')
        self.root.quit()     # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def _next_part(self):
        # if 2 <= self._state <= 5:
        #     self._state = 7
        #     if self._state_est_final[-1, 1] == 1:
        #         self._state = 8
        #
        #     if self._state_est_final[-1, 0] == 3:
        #         self._state = 9
        #     self._timer_flag = True
        #     self._msg_timer = time.time()
        #
        # elif self._state == 6 | self._timer_flag:
        self._state = 2
        self._no_completed = self._no_completed + 1
        self._state_est_final = np.zeros((1, 2))
        self._state_est_im = np.zeros((1, 2))
        self._state_est_imu = np.zeros((1, 2))
        self._timer_flag = False
        self._msg_timer = time.time()
        pass

    def update_counter(self):
        counter_text = f"Screws: {self._state_est_final[-1, 0]:.0f} \n " \
                       f"Bolts: {self._state_est_final[-1, 1]:.0f} \n \n " \
                       f"Im Screws: {self._state_est_im[-1, 0]:.0f} \n " \
                       f"Im Bolts: {self._state_est_im[-1, 1]:.0f} \n \n "\
                       f"IMU Screws: {self._state_est_imu[-1, 0]:.0f} \n " \
                       f"IMU Bolts: {self._state_est_imu[-1, 1]:.0f} \n \n " \
                       f"Completed: {self._no_completed:.0f}"
        self.counter_obj.delete("1.0", Tk.END)
        self.counter_obj.insert(Tk.INSERT, counter_text)
        pass

    def update_message(self):
        state_msgs = [f'Starting',  # 0
                      f'Initialising Sensors',  # 1
                      f'Ready to begin part {self._no_completed+1}',  # 2
                      f'Part {self._no_completed+1} still requires {3-self._state_est_final[-1, 0]:.0f} screws and {1-self._state_est_final[-1, 1]:.0f} bolts',  # 3
                      f'Part {self._no_completed+1} still requires {3-self._state_est_final[-1, 0]:.0f} screws',  # 4
                      f'Part {self._no_completed+1} still requires {1-self._state_est_final[-1, 1]:.0f} bolts',  # 5
                      f'This part seems done, press next part or quit button',  # 6
                      f'Part still missing {3-self._state_est_final[-1, 0]:.0f} screws and {1-self._state_est_final[-1, 1]:.0f} bolts \n'
                      f'Press Next Part button again if you''re sure',  # 7
                      f'Part still missing {3-self._state_est_final[-1, 0]:.0f} screws \n'
                      f'Press Next Part button again if you''re sure',  # 8
                      f'Part still missing {1-self._state_est_final[-1, 1]:.0f} bolts \n'
                      f'Press Next Part button again if you''re sure',  # 9
                      f'Sensor error, see status dialogue',  # 10
                      f'Quitting ',  # 11
                      f'Message Error']  # 12

        if (self._state == 0) & ((time.time() - self._msg_timer) > 3):
            self._state = 1

        if (self._state == 2) & ((time.time() - self._msg_timer) > 3):
            self._state = 3

        if 3 <= self._state <= 9:
            if (7 <= self._state <= 9) & (time.time() - self._msg_timer > 2) & self._timer_flag:
                self._state = 3
                self._timer_flag = False

            if 3 <= self._state <= 6:

                if (self._state_est_final[-1, 1] == 1) & (self._state_est_final[-1, 0] == 3):
                    self._state = 6

                if self._state_est_final[-1, 1] == 1:
                    self._state = 4

                if self._state_est_final[-1, 0] == 3:
                    self._state = 5



        self.message_obj.delete("1.0", Tk.END)
        if self._state > len(state_msgs) - 1:
            self._state = len(state_msgs) - 1
        self.message_obj.insert("1.0", state_msgs[self._state], "center")
        pass

    def update_status(self):
        IMU_MSGS = ['ERROR', 'Ready', 'Unknown', 'Shutdown', 'Starting', 'Connecting', 'Initialising']
        KINECT_MSGS = ['ERROR', 'Ready', 'Unknown', 'Initialising']
        SYSTEM_MSGS = ['ERROR', 'Ready', 'Setting Up']
        IMU_SYS_MSGS = ['ERROR', 'Ready', 'Setting Up']

        if any((i == 0) for i in self._imu_stat) | (self._im_stat == 0):
            self._sys_stat = 0
            self._state = 10
        elif all((i == 1) for i in self._imu_stat) & (self._im_stat == 1):
            if self._sys_stat != 1:
                self._sys_stat = 1
                self._state = 2
                self._msg_timer = time.time()

        status_text = f"System Status: {SYSTEM_MSGS[self._sys_stat]} \n " \
                      f" \n " \
                      f"Vision System: {KINECT_MSGS[self._im_stat]} \n " \
                      f" \n " \
                      f"IMU System: {IMU_SYS_MSGS[self._imu_stat[3]]} \n " \
                      f" Hand: {IMU_MSGS[self._imu_stat[0]]} \n " \
                      f"Wrist: {IMU_MSGS[self._imu_stat[1]]} \n " \
                      f"  Arm: {IMU_MSGS[self._imu_stat[2]]} \n "
        self.status_obj.delete("1.0", Tk.END)
        self.status_obj.insert(Tk.INSERT, status_text)
        pass

    def update_plot(self):
        global CATEGORIES
        legend = ['Image', 'IMU', 'Final']
        Titles = ['Total No. Screws', 'Total No. Bolts']
        global axs
        for i in range(0, 2):
            ax = axs[0, i]
            ax.cla()
            ax.plot(self._state_est_im[:, i])
            ax.plot(self._state_est_imu[:, i])
            ax.plot(self._state_est_final[:, i])
            ax.set_ylabel('Estimated Number')
            ax.set_title(Titles[i])
            ax.legend(legend)
            ax.set_ylim(bottom=0)

        axs[0, 0].set_ylim(top=3)
        axs[0, 1].set_ylim(top=1)

        ax = axs[1, 0]
        ax.cla()
        ax.bar(pos, self._imu_pred, align='center', alpha=0.5)
        ax.set_xticks(pos)
        ax.set_xticklabels(CATEGORIES)
        ax.set_ylabel('Confidence')
        ax.set_ylim([0, 1])
        ax.set_title('Current IMU Prediction')

        ax = axs[1, 1]
        ax.cla()
        ax.bar([1, 2], self._im_pred, align='center', alpha=0.5)
        ax.set_xticks([1, 2])
        ax.set_xticklabels(['Screws', 'Bolts'])
        ax.set_ylabel('Number')
        ax.set_ylim([0, 4])
        ax.set_title('Current image Prediction')

        plt.pause(0.0001)

    def update_gui(self):
        self.update_plot()
        self.update_counter()
        self.update_status()
        self.update_message()
        self.canvas.draw()
        self.root.update_idletasks()
        self.root.update()

        self._pub.publish(self._no_completed)

    def update_data(self, data):
        self._state_est_final = np.vstack((self._state_est_final, [data.state_est_final[0], data.state_est_final[1]]))
        self._state_est_im = np.vstack((self._state_est_im, [data.state_est_im[0], data.state_est_im[1]]))
        self._state_est_imu = np.vstack((self._state_est_imu, [data.state_est_imu[0], data.state_est_imu[1]]))
        self._imu_stat = data.imu_stat
        self._im_stat = data.kin_stat
        self._imu_pred = data.imu_pred
        self._im_pred = data.im_pred


def listener():
    # Run GUI
    gui = GUI()
    rospy.init_node('gui_listener', anonymous=True)
    rospy.Subscriber('gui_Data', gui_msg, gui.update_data)
    while not rospy.is_shutdown():
        gui.update_gui()


if __name__ == '__main__':
    # Run ROS node
    listener()

