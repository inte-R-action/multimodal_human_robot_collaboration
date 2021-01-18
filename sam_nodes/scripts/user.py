#!/usr/bin/env python3

import numpy as np
import datetime

class User:
    def __init__(self, name, id):
        self._imu_pred = np.zeros(6) #class confs, t 
        self._imu_pred_hist = np.empty(6) #class confs, t 
        self._imu_state_hist = np.array([4, 1, datetime.time.min, datetime.time.min]) #class, conf, tStart, tEnd
        self.left_h_pos = [None, None, None]
        self.left_h_rot = [None, None, None, None]
        self.right_h_pos = [None, None, None]
        self.right_h_rot = [None, None, None, None]
        self.status = None
        self.name = name
        self.id = id
        self.future_pred = None

    def state_est(self):
        return
    
    def collate_episode(self):
        return

    def future_pred(self):
        self.future_pred = None
        return
