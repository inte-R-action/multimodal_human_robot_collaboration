#!/usr/bin/env python3
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

plt.ion()
CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
pos = np.arange(len(CATEGORIES))
model = load_model('IMUmodel.h5')
model.summary()


def plot_prediction(prediction):
    prediction = np.reshape(prediction, (-1))
    plt.figure(2)
    ax = plt.gca()
    ax.cla()
    ax.bar(pos, prediction, align='center', alpha=0.5)
    plt.xticks(pos, CATEGORIES)
    plt.ylabel('Confidence')
    ax.set_ylim([0, 1])
    plt.pause(0.0001)


def classify_data(new_data, graph):
    new_data = new_data[np.newaxis, ...]
    #print(new_data.shape[0], new_data.shape[1], new_data.shape[2])
    if (new_data.shape[0] == 1) & (new_data.shape[1] == 154) & (new_data.shape[2] == 18):
        prediction = model.predict(new_data)
        if np.isnan(np.max(prediction)):
            class_predict = 4
        else:
            class_predict = np.argmax(prediction)

        #print(f"Activity Pred: {CATEGORIES[class_predict]}, Raw Output: {prediction}")

        if graph:
            plot_prediction(prediction)

        return prediction

    else:
        return None
