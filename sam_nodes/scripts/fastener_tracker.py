from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
from datetime import datetime
import time


class FastenerTracker():
    def __init__(self, action_duration):
        self.action_duration = action_duration
        self.scale = action_duration/2
        self.prob_dist = norm(loc=self.action_duration, scale=self.scale)
        self.max = self.prob_dist.pdf(action_duration)
        self.reset_time = datetime.now()

    def get_probability(self):
        elapsed_t = (datetime.now()-self.reset_time).total_seconds()
        if elapsed_t > 2*self.action_duration:
            probability = 0
        else:
            probability = self.prob_dist.pdf(elapsed_t)/self.max
        return probability

    def reset_timer(self):
        self.reset_time = datetime.now()

    def test_output(self):
        self.reset_timer()
        x = [0]
        probabilities = [0.00000001]
        while probabilities[-1] > 0:
            probabilities.append(self.get_probability())
            x.append((datetime.now()-self.reset_time).total_seconds())
            time.sleep(0.01)

        _, ax = plt.subplots(1, 1)
        ax.plot(x, probabilities, 'b-', lw=2, label='frozen pdf')
        plt.show()
