#!/usr/bin/env python3.7

import rospy
import numpy as np
import matplotlib.pyplot as plt
from pub_classes import act_class
plt.ion()

Fs = 50  # Sampling frequency, Hz
WIN_TIME = 3  # Window length, s
WIN_LEN = round(WIN_TIME * Fs)  # Window length, samples
skel_pca_comps = 20


class perception_module:
    def __init__(self, name, id, frame_id, ACTION_CATEGORIES):
        self.name = name
        self.id = id
        self.frame_id = frame_id
        self.actions = ACTION_CATEGORIES
        self.imu_data = np.zeros((WIN_LEN, 18))
        self.imu_update_t = None
        self.skel_data = np.zeros((WIN_LEN, skel_pca_comps))
        self.skel_update_t = None

        self.screw_classifier = None
        self.allen_classifier = None
        self.hammer_classifier = None
        self.hand_classifier = None

        self.screw_pred = 0
        self.allen_pred = 0
        self.hammer_pred = 0
        self.hand_pred = 0

        self.plt_pred = False
        self.act_obj = act_class(frame_id=self.frame_id, class_count=4, user_id=self.id, user_name=self.name, queue=10)

    def predict_actions(self):
        predict_data = [self.imu_data, self.skel_data]

        self.screw_pred = self.screw_classifier.predict(predict_data)
        self.allen_pred = self.allen_classifier.predict(predict_data)
        self.hammer_pred = self.hammer_classifier.predict(predict_data)
        self.hand_pred = self.hand_classifier.predict(predict_data)

        prediction = [self.screw_pred, self.allen_pred, self.hammer_pred, self.hand_pred]
        self.act_obj.publish(prediction)

        if self.plt_pred:
            self.plot_prediction(prediction)

    def add_imu_data(self, data, time):
        self.imu_update_t = time
        self.imu_data = np.vstack((self.imu_data, data))
        self.imu_data = self.imu_data[-WIN_LEN:, :]

    def add_skel_data(self, data, time):
        self.skel_update_t = time
        data = self.process_skel_data(data)
        self.skel_data = np.vstack((self.skel_data, data))
        self.skel_data = self.skel_data[-WIN_LEN:, :]

    def process_skel_data(self, data):
        return data

    def plot_prediction(self, prediction):
        pos = np.arange(len(self.actions)-1)
        plt.figure("HAR prediction")
        ax = plt.gca()
        ax.cla()
        ax.bar(pos, prediction, align='center', alpha=0.5)
        plt.xticks(pos, self.actions[1:])
        plt.ylabel('Confidence')
        ax.set_ylim([0, 1])
        plt.pause(0.0001)
