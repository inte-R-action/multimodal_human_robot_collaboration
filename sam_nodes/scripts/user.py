#!/usr/bin/env python3

import numpy as np


class User:
    def __init__(self, name, id):
        self.current_action = None
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
