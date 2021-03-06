#!/usr/bin/env python3.7

import sys, struct, serial, os
import numpy as np
import argparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from sklearn import preprocessing
import bluetooth
from serial.tools import list_ports
import threading
import glob
import signal
import subprocess
import rospy
from std_msgs.msg import Int8, Float64
import socket
import io
import shlex
from imu_classifier import imu_classifier
from diagnostic_msgs.msg import KeyValue
from pub_classes import diag_class, act_class
import csv
# from getpass import getpasss
import tkinter
from global_data import COMPLEX_BOX_ACTIONS, SIMPLE_BOX_ACTIONS

def get_pwd():
    out = b''
    while out == b'':
        root = tkinter.Tk() # dialog needs a root window, or will create an "ugly" one for you
        root.withdraw() # hide the root window
        password = tkinter.simpledialog.askstring("Password", "Enter password:", show='*', parent=root)#.encode('utf-8')
        root.destroy() # clean up after yourself!

        cmd1 = subprocess.Popen(['echo', password], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        var = subprocess.Popen(['sudo', '-k', '-S', '-l'], stdin=cmd1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = var.communicate()

    return password

password = get_pwd()

#cmd1 = subprocess.Popen(['echo', password], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

os.chdir(os.path.expanduser("~/catkin_ws/src/multimodal_human_robot_collaboration/"))

IMU_MSGS = ['ERROR', 'Ready', 'Unknown', 'Shutdown', 'Starting', 'Connecting', 'Initialising']
IMU_SYS_MSGS = ['ERROR', 'Ready', 'Setting Up']

# Argument parsing
parser = argparse.ArgumentParser(
    description='Base structure for connecting and streaming data from Shimmer 3 IMU sensor')

parser.add_argument('--disp', '-V',
                    help='Enable displaying of live graphs',
                    default=False,
                    action="store_true")

parser.add_argument('--task_type', '-T',
                    help='Task for users to perform, options: assemble_box (default), assemble_complex_box',
                    choices=['assemble_box', 'assemble_complex_box'],
                    default='assemble_complex_box')

parser.add_argument('--classifier_type', '-C',
                    help='Either 1v1 (one) or allvall (all) classifier',
                    choices=['none', 'one', 'all'],
                    default='one')

parser.add_argument('--bar', '-B',
                    help='Enable displaying of live prediction bar plot',
                    default=False,
                    action="store_true")

parser.add_argument('--user_name', '-N',
                    help='Set name of user, default: unknown',
                    default='unknown',
                    action="store_true")

parser.add_argument('--user_id', '-I',
                    help='Set id of user, default: None',
                    default=1,
                    action="store_true")

args = parser.parse_known_args()[0]
print(f"Shimmer settings: {args.task_type} {args.classifier_type}")
frame_id = f'shimmerBase {args.user_name} {args.user_id} node'

# Shimmer sensor connection params
serialports = ['/dev/rfcomm0', '/dev/rfcomm1', '/dev/rfcomm2']
POSITIONS = ['Hand', 'Wrist', 'Arm']
SHIM_IDs = ['F2:AF:44', 'F2:B6:ED', 'F2:C7:80']
numsensors = len(serialports)

#CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
Fs = 51.2  # Sampling frequency, Hz
WIN_TIME = 3  # Window length, s
WIN_LEN = round(WIN_TIME * Fs)  # Window length, samples

gyro_offset = [[0], [0], [0]]
gyro_sens = [[65.5, 0, 0], [0, 65.5, 0], [0, 0, 65.5]]
gyro_align = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]]
accel_offset = [[2253], [2253], [2253]]
accel_sens = [[92, 0, 0], [0, 92, 0], [0, 0, 92]]
accel_align = [[0, -1, 0], [-1, 0, 0], [0, 0, -1]]
shimmers = {}
shim_threads = {}
connect_threads = {}
quit_IMU = False
passkey = "1234"  # passkey of shimmers

dir_path = os.path.dirname(os.path.realpath(__file__))

if args.classifier_type != 'none':

    if args.classifier_type == 'all':
        if args.task_type == 'assemble_box':
            scale_file = f'{dir_path}/scale_params.csv'
            CATEGORIES = SIMPLE_BOX_ACTIONS
        elif args.task_type == 'assemble_complex_box':
            # scale_file = f'{dir_path}/imu_scale_params_allvall.csv'
            scale_file = f'{dir_path}/imu_scale_params_ava_allclassesincl.csv'
            CATEGORIES = COMPLEX_BOX_ACTIONS
    elif args.classifier_type == 'one':
        if args.task_type == 'assemble_box':
            CATEGORIES = SIMPLE_BOX_ACTIONS
        elif args.task_type == 'assemble_complex_box':
            # scale_file = f'{dir_path}/imu_scale_params_1v1_2.csv'
            scale_file = f'{dir_path}/imu_scale_params_1v1_4.csv'
            CATEGORIES = COMPLEX_BOX_ACTIONS

    with open(scale_file, newline='') as f:
        reader = csv.reader(f)
        data = np.array(list(reader))
        means = data[1:, 1].astype(float)#np.float)
        scales = data[1:, -1].astype(float)#np.float)

pos = np.arange(len(CATEGORIES)-1)

if args.disp:
    plt.ion()
    fig, axs = plt.subplots(numsensors, 2)

def plot_prediction(prediction):
    prediction = np.reshape(prediction, (-1))
    global pos, CATEGORIES
    plt.figure(2)
    ax = plt.gca()
    ax.cla()
    print(pos)
    print(prediction)
    ax.bar(pos, prediction, align='center', alpha=0.5)
    plt.xticks(pos, CATEGORIES[1:])
    plt.ylabel('Confidence')
    ax.set_ylim([0, 1])
    plt.pause(0.0001)

def shutdown_imu():
    global quit_IMU
    quit_IMU = True

def plot_func(plotdata):
    if not quit_IMU:
        if numsensors == 1:
            for j in range(0, 2):
                axs[j].cla()
                axs[j].plot(plotdata[:, (j*3)])
                axs[j].plot(plotdata[:, (j*3)+1])
                axs[j].plot(plotdata[:, (j*3)+2])
                plt.gca()
                if j == 0:
                    axs[j].set_ylim([-25, 25])
                    axs[j].set_ylabel(f"m/s^2")
                    axs[j].set_title(f"{POSITIONS[0]} Sensor Accelerometer")
                else:
                    axs[j].set_ylim([-500, 500])
                    axs[j].set_ylabel(f"Deg/s")
                    axs[j].set_title(f"{POSITIONS[0]} Sensor Gyroscope")
        else:
            for i in range(0, numsensors):
                for j in range(0, 2):
                    axs[i, j].cla()
                    axs[i, j].plot(plotdata[:, (i*6)+(j*3)])
                    axs[i, j].plot(plotdata[:, (i*6)+(j*3)+1])
                    axs[i, j].plot(plotdata[:, (i*6)+(j*3)+2])
                    plt.gca()
                    if j == 0:
                        axs[i, j].set_ylim([-25, 25])
                        axs[i, j].set_ylabel(f"m/s^2")
                        axs[i, j].set_title(f"{POSITIONS[i]} Sensor Accelerometer")
                    else:
                        axs[i, j].set_ylim([-500, 500])
                        axs[i, j].set_ylabel(f"Deg/s")
                        axs[i, j].set_title(f"{POSITIONS[i]} Sensor Gyroscope")

        plt.pause(0.0001)

def scale_data(new_data):
    new_data = (new_data-means)/scales
    return new_data
    

class shimmer():
    def __init__(self, q):
        self._ready = False
        self._connect_error = True
        self._connection = None
        self._connected = False
        self._ID = SHIM_IDs[q]
        self._location = POSITIONS[q]
        self._port = serialports[q]
        self._serial = None
        self._accel = np.zeros((WIN_LEN, 3))
        self._gyro = np.zeros((WIN_LEN, 3))
        self._batt = None
        self._batt_perc = None
        self._num = q
        self._ddata = b''
        self._batt_time = time.time()
        self._numbytes = 0
        self._batt_arr = np.empty((1, 0))
        self._shutdown = True
        self._status = 4 # starting
        rospy.on_shutdown(self.shutdown)

    def wait_for_ack(self):
        ddata = b''
        ack = struct.pack('B', 0xff)
        count = 0
        timer = time.time()
        while ddata != ack:
            if time.time() - timer < 1:
                try:
                    ddata = self._serial.read(1)
                except Exception as e:
                    print(f"Error reading acknowledgment from {self._location} sensor: {e}")
                    self._connected = False
                    count = count + 1
                if count > 3:
                    print(f"###---{self._location} acknowledgement error---###")
                    return False
            #print("0x%02x" % ord(ddata))
            else:
                print(f"###---{self._location} acknowledgement timeout---###")
                return False
        return True

    def initiate(self):
        while (not self._connected) & (not self._connect_error) & (not quit_IMU):
            time.sleep(5)
            try:
                self._serial = serial.Serial(self._port, 115200, timeout=5)
                self._serial.flushInput()
                print(f"---{self._location} port opening, done.")
                # send the set sensors command
                self._serial.write(struct.pack('BBBB', 0x08, 0xC0, 0x20, 0x00))  # analogaccel, mpu gyro, batt volt
                if not self.wait_for_ack():
                    return False
                self._connected = True
                self._status = 6 # initialising
                print(f"---{self._location} sensor setting, done.")
                # send the set sampling rate command
                self._serial.write(
                    struct.pack('BBB', 0x05, 0x80,
                                0x02))  # 51.2Hz (6400 (0x1900)). Has to be done like this for alignment reasons
                if not self.wait_for_ack():
                    return False
                print(f"---{self._location} sampling rate setting, done.")
                # send start streaming command
                self._serial.write(struct.pack('B', 0x07))
                if not self.wait_for_ack():
                    return False
                print(f"---{self._location} start command sending, done.")
                #self.inquiry_response()  # Use this if you want to find the structure of data that will be streamed back

                return True

            except Exception as e:
                print(f'exception in {self._location} initiate: {e}')
                self._connected = False
        #return True

    def inquiry_response(self):
        # Outputs data structure of data to be streamed back
        self._serial.flushInput()
        # send inquiry command
        self._serial.write(struct.pack('B', 0x01))
        self.wait_for_ack()

        # read incoming data
        ddata = b''
        numbytes = 0
        framesize = 9

        print("Inquiry response:")
        while (numbytes < framesize) and (not quit_IMU):
            ddata = ddata + self._serial.read(framesize)
            print(ddata)
            numbytes = len(ddata)

        data = ddata[0:framesize]
        ddata = ddata[framesize:]
        #numbytes = len(ddata)
        (packettype) = struct.unpack('B', bytes(data[0].to_bytes(1, sys.byteorder)))
        (samplingrate, configByte0, configByte1, configByte2, configByte3, numchans, bufsize) = struct.unpack('HBBBBBB',
                                                                                                              data[1:9])
        print("          Packet type: 0x%02x" % packettype)
        print("        Sampling rate: 0x%04x" % samplingrate)
        print("  Config Setup Byte 0: 0x%02x" % configByte0)
        print("  Config Setup Byte 1: 0x%02x" % configByte1)
        print("  Config Setup Byte 2: 0x%02x" % configByte2)
        print("  Config Setup Byte 3: 0x%02x" % configByte3)
        print("   Number of channels: 0x%02x" % numchans)
        print("          Buffer size: 0x%02x" % bufsize)

        for i in range(numchans):
            data = self._serial.read(1)
            print("           Channel %2d:" % i)
            print("                        0x%02x" % (struct.unpack('B', data[0].to_bytes(1, sys.byteorder))))

        return

    def calibrate_data(self, data, sensor):
        # Calibrate readings to m/s2, deg/s. More info: http://www.shimmersensing.com/images/uploads/docs/Shimmer_9DOF_Calibration_User_Manual_rev2.10a.pdf
        if sensor == 'a':
            Ri = np.linalg.inv(accel_align)
            Ki = np.linalg.inv(accel_sens)
            offset = accel_offset
        elif sensor == 'g':
            Ri = np.linalg.inv(gyro_align)
            Ki = np.linalg.inv(gyro_sens)
            offset = gyro_offset
        else:
            print('Calibration sensor invalid, must be ''a'' or ''g'' ')
            raise ValueError
        calib_data = np.transpose(Ri @ Ki @ (np.transpose(data) - offset))
        return calib_data

    def bt_connection(self):
        count = 1
        self._status = 5 # connecting
        while self._connect_error & (not quit_IMU) & (count <= 3):
            print(f"Trying to connect {self._location}, attempt {count}/3")
            target_address = None
            try:
                print(f"Finding Devices for {self._location}...")
                nearby_devices = bluetooth.discover_devices()
                for bdaddr in nearby_devices:
                    if self._ID == bdaddr[-8:]:
                        target_address = bdaddr
                        break
            except bluetooth.btcommon.BluetoothError as e:
                print(f"Discover Devices error: {e}")

            if target_address is not None:
                print(f"found {self._location} bluetooth device with address {target_address}")

                # Start a new "bluetooth-agent" process where XXXX is the passkey
                #subprocess.call(f"bluetooth-agent {passkey}", shell=True)

                try:
                    cmd1 = subprocess.Popen(['echo', password], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    self._connection = subprocess.Popen(f"sudo -S rfcomm connect {self._port} {target_address} 1", shell=True, stdin=cmd1.stdout, stdout=subprocess.PIPE)
                    time.sleep(2)
                    self._connect_error = False
                    return True

                except Exception as e:
                    self._connect_error = True
                    self._connected = False
                    print(f"Exception in connecting {self._location}: {e}")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)

            else:
                print(f"could not find {self._location} bluetooth device nearby")
                self._connect_error = True
                self._connected = False
            count = count + 1

        return False

    def checkbattery(self):
        batt_last = self._batt_perc
        if self._batt < 3.2:
            self._batt_perc = 0.0
        elif self._batt < 3.627:
            self._batt_perc = 5.9
        elif self._batt < 3.645:
            self._batt_perc = 9.8
        elif self._batt < 3.663:
            self._batt_perc = 13.8
        elif self._batt < 3.681:
            self._batt_perc = 17.7
        elif self._batt < 3.699:
            self._batt_perc = 21.6
        elif self._batt < 3.717:
            self._batt_perc = 25.6
        elif self._batt < 3.7314:
            self._batt_perc = 29.5
        elif self._batt < 3.735:
            self._batt_perc = 33.4
        elif self._batt < 3.7386:
            self._batt_perc = 37.4
        elif self._batt < 3.7566:
            self._batt_perc = 41.3
        elif self._batt < 3.771:
            self._batt_perc = 45.2
        elif self._batt < 3.789:
            self._batt_perc = 49.2
        elif self._batt < 3.8034:
            self._batt_perc = 53.1
        elif self._batt < 3.8106:
            self._batt_perc = 57.0
        elif self._batt < 3.8394:
            self._batt_perc = 61.0
        elif self._batt < 3.861:
            self._batt_perc = 64.9
        elif self._batt < 3.8826:
            self._batt_perc = 68.9
        elif self._batt < 3.9078:
            self._batt_perc = 72.8
        elif self._batt < 3.933:
            self._batt_perc = 76.7
        elif self._batt < 3.969:
            self._batt_perc = 80.7
        elif self._batt < 4.0086:
            self._batt_perc = 84.6
        elif self._batt < 4.041:
            self._batt_perc = 88.5
        elif self._batt < 4.0734:
            self._batt_perc = 92.5
        elif self._batt < 4.113:
            self._batt_perc = 96.4
        else:
            self._batt_perc = 100

        if (self._batt_perc != batt_last) & (self._batt_perc is not None):
            print(f"{self._location} sensor battery at {self._batt_perc}%")

    def start(self):
        # Start thread for shimmer connection
        # connect_threads[num] = threading.Thread(target=shimmers[num].bt_connection, args=(num,))
        # connect_threads[num].start()
        
        if self.bt_connection():
            count = 0
            while count <= 3: 
                if self.initiate():  # Send set up commands, etc to shimmer
                    print(f'---Initiated {self._location} Sensor---')
                    return True
                else:
                    count += 1
                    print(f"Failed to initialise {self._location} sensor, attempt {count}/3")
                    return False
        else:
            print(f"Failed to connect {self._location} sensor")
            return False

    def getdata(self):
        framesize = 18  # 1byte packet type + 3byte timestamp + 3x2byte Analog Accel + 2byte Battery + 3x2byte Gyro
        while self._numbytes < framesize and (not quit_IMU):
            try:
                self._ddata = self._ddata + self._serial.read(framesize)
            except Exception as e:
                print(f"Unable to read {self._location} IMU data: {e}")
                return False
            self._numbytes = len(self._ddata)

        data = self._ddata[0:framesize]
        self._ddata = self._ddata[framesize:]
        self._numbytes = len(self._ddata)

        accel = self.calibrate_data(np.array(struct.unpack('HHH', data[4:10]), ndmin=2), 'a')
        self._accel = np.vstack((self._accel, accel))
        self._accel = self._accel[-WIN_LEN:, :]
        self._accel = np.nan_to_num(self._accel)

        batt_now = struct.unpack('H', data[10:12])[0] * 6 / 4095
        batt_now = np.nan_to_num(batt_now)
        self._batt_arr = np.append(self._batt_arr, batt_now)
        self._batt = np.mean(self._batt_arr)
        while len(self._batt_arr) > 50:
            self._batt_arr = np.delete(self._batt_arr, 0)

        if (time.time() - self._batt_time) > 1:
            self.checkbattery()
            self._batt_time = time.time()

        gyro = self.calibrate_data(np.array(struct.unpack('>hhh', data[12:framesize]), ndmin=2), 'g')
        self._gyro = np.vstack((self._gyro, gyro))
        self._gyro = self._gyro[-WIN_LEN:, :]
        self._gyro = np.nan_to_num(self._gyro)
        self._status = 1 # ready
        return True

    def shutdown(self):
        # Reset all flags/parameters
        self._connected = False
        #self._connection = None
        self._ready = False
        self._connect_error = True

        # Shut sensor down and kill serial connection
        try:
            count = 1
            sd = False
            while (not sd) and (count <= 3):
                # send stop streaming command
                self._serial.write(struct.pack('B', 0x20))
                print(f"{self._location} stop command sent, waiting for ACK_COMMAND")
                if self.wait_for_ack():
                    print(f"---{self._location} stop ACK_COMMAND received.")
                    # close serial port
                    self._serial.close()
                    sd = True
                else:
                    #self._serial.close()
                    print(f"---{self._location} stop ACK_COMMAND *NOT* received. Attempt {count}/3")
                    count += 1

        except Exception as e:
            print(f"{self._location} close down sensor error: {e}")
            pass

        #Kill bluetooth connection
        try:
            #self._connection.release()
            #self._connection.kill()
            os.kill(self._connection.pid, 1)
        except Exception as e:
            print(f"{self._location} connection not killed: {e}")
            pass

        return True

def shimmer_thread(num):
    print(f"Setting up Sensor {num + 1}/{numsensors}")
    shimmers[num] = shimmer(num)  # Create instance of shimmer class for each device

    # read incoming data
    first_try = True
    while not quit_IMU:
        if shimmers[num]._ready and (not quit_IMU):
            if shimmers[num]._connected:
                success = shimmers[num].getdata()
                if not success:
                    shimmers[num]._ready = False
                    shimmers[num]._connected = False
            else:
                
                print(f"{shimmers[num]._location} not connected?")

        elif not quit_IMU:
            if first_try:
                # Try starting connection
                print(f"Starting {POSITIONS[num]} connection and initialisation")
                first_try = False
            else:
                # Try restarting connection
                print(f"Lost {POSITIONS[num]} connection, restarting")

            shimmers[num]._shutdown = False
            shimmers[num]._ready = shimmers[num].start()

            if shimmers[num]._ready:
                print(f"{shimmers[num]._location} sensor connected, starting data stream {num + 1}")
            else:
                print(f"{shimmers[num]._location} sensor failed to start successfully, retrying")
                shimmers[num]._shutdown = shimmers[num].shutdown()

    # quit_IMU condition
    #shutdown = shimmers[num].shutdown()


def IMUsensorsMain():
    print("-----Here we go-----")
    rospy.init_node(f'shimmerBase_{args.user_name}_{args.user_id}', anonymous=True)
    rate = rospy.Rate(2)  # Message publication rate, Hz => should be 2
    
    keyvalues = [KeyValue(key = f'Shimmer {POSITIONS[0]} {SHIM_IDs[0]}', value = IMU_MSGS[2]), 
                KeyValue(key = f'Shimmer {POSITIONS[1]} {SHIM_IDs[1]}', value = IMU_MSGS[2]),
                KeyValue(key = f'Shimmer {POSITIONS[2]} {SHIM_IDs[2]}', value = IMU_MSGS[2]),
                KeyValue(key = f'Overall', value = IMU_SYS_MSGS[2])] # [unknown, unknown, unknown, setting up]
    diag_obj = diag_class(frame_id=frame_id, user_id=args.user_id, user_name=args.user_name, queue=1, keyvalues=keyvalues)


    if args.classifier_type != 'none':
        if args.classifier_type == 'all':
            if args.task_type == 'assemble_box':
                class_count = 5
                model_file = 'basic_box_classifier.h5'
                classifier = imu_classifier(model_file, CATEGORIES, WIN_LEN)
            elif args.task_type == 'assemble_complex_box':
                class_count = 5
                # model_file = 'complex_box_classifier_allvall_1.h5'
                model_file = 'complex_box_classifier_allvall_2_allclassesincl.h5'
                classifier = imu_classifier(model_file, CATEGORIES, WIN_LEN)
        elif args.classifier_type == 'one':
            if args.task_type == 'assemble_box':
                pass
            elif args.task_type == 'assemble_complex_box':
                class_count = 4
                # classifier_screw = imu_classifier('Screw In_classifier_TrainOnAll_2.h5', ['null', 'screw_in'], WIN_LEN)
                # classifier_allen = imu_classifier('Allen In_classifier_TrainOnAll_2.h5', ['null', 'allen_in'], WIN_LEN)
                # classifier_hand = imu_classifier('Hand Screw In_classifier_TrainOnAll_2.h5', ['null', 'hand_screw_in'], WIN_LEN)
                # classifier_hammer = imu_classifier('Hammer_classifier_TrainOnAll_2.h5', ['null', 'hammer'], WIN_LEN)      
                
                classifier_screw = imu_classifier('Screw In_classifier_TrainOnAll_4_allclassesincl.h5', ['screw_in'], WIN_LEN)
                classifier_allen = imu_classifier('Allen In_classifier_TrainOnAll_4_allclassesincl.h5', ['allen_in'], WIN_LEN)
                classifier_hand = imu_classifier('Hand Screw In_classifier_TrainOnAll_4_allclassesincl.h5', ['hand_screw_in'], WIN_LEN)
                classifier_hammer = imu_classifier('Hammer_classifier_TrainOnAll_4_allclassesincl.h5', ['hammer'], WIN_LEN)      
            

        act_obj = act_class(frame_id=frame_id, class_count=class_count, user_id=args.user_id, user_name=args.user_name, queue=10)
        
        prediction = np.zeros(class_count)

    # Start separate thread for collecting data from each Shimmer
    for shimthread in range(0, numsensors):
        shim_threads[shimthread] = threading.Thread(target=shimmer_thread, args=(shimthread,))
        shim_threads[shimthread].start()
        # time.sleep(10)
        # while not shimmers[shimthread]._connected:
        #     time.sleep(5)
        #     print(shimmers[shimthread]._connected)

    ready = np.zeros((len(shim_threads)))  # Bool array for if shimmers are setup and streaming
    alive = np.zeros((len(shim_threads)))  # Bool array for if shimmer thread are active
    conn = np.zeros((len(shim_threads)))  # Bool array for if connections are successful
    s_down = np.zeros((len(shim_threads)))  # Bool array for if sensors are shutdown
    time.sleep(1)

    print("Starting main loop")
    
    class_pred = 'null'#CATEGORIES[-1]
    status = [2, 2, 2, 2] # [unknown, unknown, unknown, setting up]
    diag_level = 1 # 0:ok, 1:warning, 2:error, 3:stale
    while not quit_IMU:
        status[3] = 2 # setting up
        for s in shimmers:
            ready[s] = shimmers[s]._ready
            alive[s] = shim_threads[s].is_alive()
            conn[s] = shimmers[s]._connected
            s_down[s] = shimmers[s]._shutdown
            status[s] = shimmers[s]._status
            keyvalues = [KeyValue(key = f'Shimmer {POSITIONS[s]} {SHIM_IDs[s]}', value = IMU_MSGS[status[s]])]

        out_str = f"Sensors Ready:{ready} Threads:{alive} Connections:{conn} Shutdowns:{s_down} " \
                  f"Total Threads:{threading.active_count()} Quit:{quit_IMU} Prediction:{class_pred}"
        #out_str = threading.enumerate()
        print(out_str)
        class_pred = 'null'#CATEGORIES[-1]
        new_data = np.empty((WIN_LEN, 0), dtype=np.float64)
        if all(ready) & all(conn) & all(alive):
            for p in shimmers:
                new_data = np.hstack((new_data, shimmers[p]._accel, shimmers[p]._gyro))
            new_data = np.nan_to_num(new_data)
            #scaler = preprocessing.StandardScaler()
            # for i in range(0, X.shape[0]):
            #     scaler = preprocessing.StandardScaler()
            #     X[i, :, :] = scaler.fit_transform(X[i, :, :])
            #new_data[:, :] = scaler.fit_transform(new_data[:, :])
            new_data = scale_data(new_data)
            status[3] = 1 # Ready
            diag_level = 0 # ok
            
            if args.classifier_type != 'none':
                if args.classifier_type == 'all':
                    if args.task_type == 'assemble_box':
                        prediction = np.reshape(classifier.classify_data(new_data, args.bar), (-1)).tolist()
                    elif args.task_type == 'assemble_complex_box':
                        prediction = np.reshape(classifier.classify_data(new_data, args.bar), (-1)).tolist()
                elif args.classifier_type == 'one':
                    if args.task_type == 'assemble_box':
                        pass
                    elif args.task_type == 'assemble_complex_box':
                        prediction = []
                        prediction.append(classifier_screw.classify_data(new_data, False))#[1])
                        prediction.append(classifier_allen.classify_data(new_data, False))#[1])
                        prediction.append(classifier_hammer.classify_data(new_data, False))#[1])
                        prediction.append(classifier_hand.classify_data(new_data, False))#[1])

                        if args.bar:
                            plot_prediction(prediction)
                
                #print(prediction)
                class_pred = CATEGORIES[np.argmax(prediction)]

        else:
            diag_level = 1 # warning

        if all(ready) & all(conn) & all(alive) & (not quit_IMU) & args.disp:
            plotdata = np.empty((WIN_LEN, 0), dtype=np.float64)
            for p in shimmers:
                plotdata = np.hstack((plotdata, shimmers[p]._accel, shimmers[p]._gyro))
            plotdata = np.nan_to_num(plotdata)
            plot_func(plotdata)

        #rospy.loginfo(out_str)

        diag_msg = "Some helpful message"
        keyvalues = [KeyValue(key = f'Shimmer {POSITIONS[0]} {SHIM_IDs[0]}', value = IMU_MSGS[status[0]]), 
                KeyValue(key = f'Shimmer {POSITIONS[1]} {SHIM_IDs[1]}', value = IMU_MSGS[status[1]]),
                KeyValue(key = f'Shimmer {POSITIONS[2]} {SHIM_IDs[2]}', value = IMU_MSGS[status[2]]),
                KeyValue(key = f'Overall', value = IMU_SYS_MSGS[status[3]])]

        if args.classifier_type != 'none':
            try:
                act_obj.publish(prediction)
            except Exception as e:
                print(e)
                print(prediction)
        
        diag_obj.publish(diag_level, diag_msg, keyvalues)

        rate.sleep()


if __name__ == "__main__":
    #subprocess.call("sudo service bluetooth restart")
    cmd1 = subprocess.Popen(['echo', password], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    subprocess.call("sudo -S rfcomm release all", shell=True, stdin=cmd1.stdout)#, stdout=subprocess.PIPE)
    # kill any rfcomm connections currently active
    cmd1 = subprocess.Popen(['echo', password], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    subprocess.call("sudo -S killall rfcomm", shell=True, stdin=cmd1.stdout, stdout=subprocess.PIPE)
    # kill any "bluetooth-agent" process that is already running
    #subprocess.call("kill -9 `pidof bluetooth-agent`", shell=True)
    rospy.on_shutdown(shutdown_imu)
    try:
        IMUsensorsMain()
    except rospy.ROSInterruptException:
        quit_IMU = True
        print("Keyboard Interrupt")
        plt.close('all')
    finally:
        threads_alive = True
        while threads_alive:
            threads_alive = False
            for s in shim_threads:
                threads_alive = threads_alive | shim_threads[s].is_alive()
            time.sleep(0.01)

        if args.disp:
            plt.show()
        quit_IMU = True
        cmd1 = subprocess.Popen(['echo', password], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        subprocess.call("sudo -S rfcomm release all", shell=True, stdin=cmd1.stdout, stdout=subprocess.PIPE)
        del cmd1, password
        ready = np.zeros((len(shim_threads)))  # Bool array for if shimmers are setup and streaming
        alive = np.zeros((len(shim_threads)))  # Bool array for if shimmer thread are active
        conn = np.zeros((len(shim_threads)))  # Bool array for if connections are successful
        s_down = np.zeros((len(shim_threads)))  # Bool array for if sensors are shutdown

        for s in shimmers:
            ready[s] = shimmers[s]._ready
            alive[s] = shim_threads[s].is_alive()
            conn[s] = shimmers[s]._connected
            s_down[s] = shimmers[s]._shutdown

        print("###---End Status---###")
        print(f"Sensors Ready:{ready} Threads:{alive} Connections:{conn} Shutdowns:{s_down} "
              f"Threads:{threading.active_count()} Quit:{quit_IMU}")

        print("All done")
