#!/usr/bin/env python3.7

import csv
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import numpy as np
import matplotlib.pyplot as plt
from pub_classes import act_class
from process_skel_data import process_skel_data
from tensorflow.keras.models import load_model
from global_data import GESTURES
import tensorflow as tf
import tensorflow_addons as tfa
from vision_recognition.count_fasteners_table import fastener_counter

import sys
print(sys.version)
print(tf.__version__)

plt.ion()
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
if len(gpus) > 0:
    tf.config.experimental.set_visible_devices(devices=gpus[0], device_type='GPU')
    tf.config.experimental.set_memory_growth(device=gpus[0], enable=True)
Fs = 50  # Sampling frequency, Hz
WIN_TIME = 3  # Window length, s
WIN_LEN = round(WIN_TIME * Fs)  # Window length, samples
use_GRU = True
timesteps = 15


class perception_module:
    def __init__(self, name, u_id, frame_id, ACTION_CATEGORIES):
        self.name = name
        self.id = u_id
        self.frame_id = frame_id
        self.actions = ACTION_CATEGORIES
        self.new_imu_data = np.zeros((1, 18))
        self.imu_data = np.zeros((WIN_LEN, 18))
        self.tstep_imu_data = []
        self.imu_update_t = None
        self.imu_means = None
        self.imu_scales = None
        self.new_skel_data = np.zeros((1, 15*7))
        self.skel_data = np.zeros((WIN_LEN, 15*7))
        self.tstep_skel_data = []
        self.skel_update_t = None
        self.predict_data = []

        folder = './sam_nodes/scripts/models_parameters/'
        if use_GRU:
            self.gesture_classifier = load_model(folder+'gestures_(-4)(bn)Dd(Gd)D)_timesteps15_20221027.h5')
            self.screw_classifier = load_model(folder+'Screw In_(-4)(bn)Dd(Gd)D)_timesteps15_20221003.h5')
            self.allen_classifier = load_model(folder+'Allen In_(-4)(bn)Dd(Gd)D)_timesteps15_20221003.h5')
            self.hammer_classifier = load_model(folder+'Hammer_(-4)(bn)Dd(Gd)D)_timesteps15_20221003.h5')
            self.hand_classifier = load_model(folder+'Hand Screw In_(-4)(bn)Dd(Gd)D)_timesteps15_20221003.h5')
        else:
            self.gesture_classifier = load_model(folder+'gestures_imuskel_classifier_2str_i(CCPCCP)s(CCPCCP)c(HHHD)_inclAllNull.h5')
            self.screw_classifier = load_model(folder+'Screw In_model_1_2str_i(CCPCCP)s(CCPCCP)c(HHHD)_inclAllNull.h5')
            self.allen_classifier = load_model(folder+'Allen In_model_1_2str_i(CCPCCP)s(CCPCCP)c(HHHD)_inclAllNull.h5')
            self.hammer_classifier = load_model(folder+'Hammer_model_1_2str_i(CCPCCP)s(CCPCCP)c(HHHD)_inclAllNull.h5')
            self.hand_classifier = load_model(folder+'Hand Screw In_model_1_2str_i(CCPCCP)s(CCPCCP)c(HHHD)_inclAllNull.h5')
        
        # print(self.gesture_classifier.summary())
        # print(self.screw_classifier.summary())
        # print(self.allen_classifier.summary())
        # print(self.hammer_classifier.summary())
        # print(self.hand_classifier.summary())

        self.screw_pred = 0
        self.allen_pred = 0
        self.hammer_pred = 0
        self.hand_pred = 0
        self.load_imu_scale_parameters(folder)

        self.plt_pred = False
        self.act_obj = act_class(frame_id=self.frame_id+'_actions', class_count=4, user_id=self.id, user_name=self.name, queue=10)
        self.ges_obj = act_class(frame_id=self.frame_id+'_gestures', class_count=len(GESTURES), user_id=self.id, user_name=self.name, queue=10)

        self.fastener_counter = fastener_counter(self.frame_id, self.id, self.name)

    def update_user_details(self, name=None, Id=None, frame_id=None):
        if name:
            self.name = name
            self.act_obj.act_msg.UserName = self.name
            self.ges_obj.act_msg.UserName = self.name
        if Id:
            self.id = Id
            self.act_obj.act_msg.UserId = self.id
            self.ges_obj.act_msg.UserId = self.id
        if frame_id:
            self.frame_id = frame_id
            self.act_obj.act_msg.Header.frame_id = self.frame_id+'_actions'
            self.ges_obj.act_msg.Header.frame_id = self.frame_id+'_gestures'

    def load_imu_scale_parameters(self, folder):
        # load scaling parameters
        scale_file = folder+"imu_scale_params_winlen3_transitionsTrue_1v1_inclAllNull.csv"  # file with normalisation parameters
        with open(scale_file, newline='') as f:
            reader = csv.reader(f)
            data = np.array(list(reader))
            self.means = data[1:, 1].astype(float)
            self.scales = data[1:, -1].astype(float)

    def predict(self):
        new_skel_data = process_skel_data(self.skel_data)

        try:
            if use_GRU:
                self.tstep_imu_data.append(self.imu_data)
                self.tstep_skel_data.append(new_skel_data)
                
                if (len(self.tstep_imu_data) >= timesteps):
                    self.tstep_imu_data = self.tstep_imu_data[-timesteps:]
                    self.tstep_skel_data = self.tstep_skel_data[-timesteps:]

                    self.predict_data = [np.asarray(self.tstep_imu_data)[np.newaxis, ...], np.asarray(self.tstep_skel_data)[np.newaxis, ...]]
                    self.predict_actions()
                    self.predict_gestures()
            else:
                self.predict_data = [self.imu_data[np.newaxis, ...], new_skel_data[np.newaxis, ...]]
                self.predict_actions()
                self.predict_gestures()
        except Exception as e:
            print(e)

    def predict_actions(self):
        self.screw_pred = self.screw_classifier.predict(self.predict_data)[0][0]
        self.allen_pred = self.allen_classifier.predict(self.predict_data)[0][0]
        self.hammer_pred = self.hammer_classifier.predict(self.predict_data)[0][0]
        self.hand_pred = self.hand_classifier.predict(self.predict_data)[0][0]

        prediction = [self.screw_pred, self.allen_pred, self.hammer_pred, self.hand_pred]
        self.act_obj.publish(prediction)

        if self.plt_pred:
            self.plot_prediction(prediction)

    def predict_gestures(self):
        gesture_pred = self.gesture_classifier.predict(self.predict_data)[0]
        self.ges_obj.publish(gesture_pred)

    def add_imu_data(self, data, time):
        self.imu_update_t = time
        self.new_imu_data = (data-self.means)/self.scales

    def add_skel_data(self, data, time):
        self.skel_update_t = time
        self.new_skel_data = data

    def update_data_window(self):
        self.imu_data = np.vstack((self.imu_data, self.new_imu_data))
        self.imu_data = self.imu_data[-WIN_LEN:, :]
        self.skel_data = np.vstack((self.skel_data, self.new_skel_data))
        self.skel_data = self.skel_data[-WIN_LEN:, :]

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
