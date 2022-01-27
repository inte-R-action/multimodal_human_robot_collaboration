#!/usr/bin/env python3.7

import numpy as np
from global_data import JOINTS_U, JOINT_LINKS, PCA_COMPS
import matplotlib.pyplot as plt
from math import acos
import pickle


NUM_JOINTS = len(JOINTS_U)
NUM_LINKS = len(JOINT_LINKS[0])
infile = open('models_parameters/pca_winlen3_transitionsTrue_1v1', 'rb')
pca = pickle.load(infile)
infile.close()


def scale_skeleton_data(skeleton_seq, plot):
    # Get positions relative to center joint
    center_joint = 'torso'
    idx = JOINTS_U.index(center_joint)
    for i in range(np.shape(skeleton_seq)[0]):
        skeleton_seq[i, :, :] = skeleton_seq[i, :, :] - skeleton_seq[i, idx, :]

    # Scale relative to torso length
    for i in range(np.shape(skeleton_seq)[0]):
        scale_dist = np.linalg.norm(skeleton_seq[i, JOINTS_U.index('neck'), :])
        skeleton_seq[i, :, :] = skeleton_seq[i, :, :]/scale_dist

    if plot:
        fig = plt.figure()
        skel_ax = fig.add_subplot(projection='3d')

        skel_frames = np.shape(skeleton_seq)[0]
        for i in range(0, skel_frames, 100):
            skel_ax.clear()
            skeleton = skeleton_seq[i, :, :]

            xs = skeleton[:, 0]
            ys = skeleton[:, 1]
            zs = skeleton[:, 2]
            skel_ax.scatter(xs, ys, zs)

            for j in range(len(JOINT_LINKS[0])):
                #point1 = skeleton[JOINT_LINKS[0][j]-1, :]
                #point2 = skeleton[JOINT_LINKS[1][j]-1, :]
                point1 = skeleton[JOINT_LINKS[0][j], :]
                point2 = skeleton[JOINT_LINKS[1][j], :]
                skel_ax.plot([point1[0], point2[0]], [point1[1], point2[1]],
                            [point1[2], point2[2]])  # , 'LineWidth',2)

            skel_ax.set_box_aspect((np.ptp(skeleton_seq[:, :, 0]), np.ptp(
                skeleton_seq[:, :, 1]), np.ptp(skeleton_seq[:, :, 2])))
            skel_ax.set_xlabel('X Label')
            skel_ax.set_ylabel('Y Label')
            skel_ax.set_zlabel('Z Label')

            skel_ax.set_xlim(np.min(skeleton_seq[:, :, 0]), np.max(
                skeleton_seq[:, :, 0]))
            skel_ax.set_ylim(np.min(skeleton_seq[:, :, 1]), np.max(
                skeleton_seq[:, :, 1]))
            skel_ax.set_zlim(np.min(skeleton_seq[:, :, 2]), np.max(
                skeleton_seq[:, :, 2]))

            skel_ax.view_init(elev=-90, azim=-90)

            plt.draw()
            plt.pause(0.0000001)

    return skeleton_seq


def find_skeleton_features(skeleton_seq):
    displacements = []
    distances = []
    temp_seq = []
    for frame in range(np.shape(skeleton_seq)[0]):
        window_data = np.zeros((88))
        if frame == 0:
            displacements = np.zeros(np.shape(skeleton_seq[frame, :, :]))
        else:
            displacements = skeleton_seq[frame, :, :] - skeleton_seq[frame-1, :, :]

        distances = [np.linalg.norm(skeleton_seq[frame, i, :]) for i in range(NUM_JOINTS)]

        frame_angles = []
        for j in range(NUM_LINKS):
            vec1 = skeleton_seq[frame, JOINT_LINKS[1][j], :] - skeleton_seq[frame, JOINT_LINKS[0][j], :]
            for k in range(NUM_LINKS):
                if JOINT_LINKS[0][k] == JOINT_LINKS[1][j]:
                    vec2 = skeleton_seq[frame, JOINT_LINKS[1][k], :]-skeleton_seq[frame, JOINT_LINKS[0][k], :]
                    frame_angles.append(acos((vec1 @ vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))))

        angles = frame_angles

        window_data[0:NUM_JOINTS] = skeleton_seq[frame, :, 0].T
        window_data[NUM_JOINTS:2*NUM_JOINTS] = skeleton_seq[frame, :, 1].T
        window_data[2*NUM_JOINTS:3*NUM_JOINTS] = skeleton_seq[frame, :, 2].T
        window_data[3*NUM_JOINTS:4*NUM_JOINTS] = displacements[:, 0].T
        window_data[4*NUM_JOINTS:5*NUM_JOINTS] = displacements[:, 1].T
        window_data[5*NUM_JOINTS:6*NUM_JOINTS] = displacements[:, 2].T
        window_data[6*NUM_JOINTS:6*NUM_JOINTS+len(distances)] = distances
        window_data[6*NUM_JOINTS+len(distances):] = angles

        temp_seq.append(window_data)

    skeleton_seq = np.asarray(temp_seq)
    return skeleton_seq


def process_skel_data(skeleton_seq):
    print(f"skeleton seq shape: {skeleton_seq.shape}")
    u_body_joints = [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12]
    u_body_skel = np.empty((skeleton_seq.shape[0], len(u_body_joints), 3))

    # select data from upper body joints
    for i in range(len(u_body_joints)):
        u_body_skel[:, i, 0] = skeleton_seq[:, u_body_joints[i]*7] # x's
        u_body_skel[:, i, 1] = skeleton_seq[:, 1+(u_body_joints[i]*7)] # y's
        u_body_skel[:, i, 2] = skeleton_seq[:, 2+(u_body_joints[i]*7)] # z's

    skeleton_seq = u_body_skel
    skeleton_seq = scale_skeleton_data(skeleton_seq, plot=False)
    skeleton_seq = find_skeleton_features(skeleton_seq)
    skeleton_seq = pca.transform(np.nan_to_num(skeleton_seq))[:, 0:PCA_COMPS]
    return skeleton_seq
