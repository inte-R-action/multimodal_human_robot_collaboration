#!/usr/bin/env python3
# Must be run from scripts folder
# Import Statements
import pyrealsense2 as rs
import numpy as np
import traceback
import argparse
import sys
import time
import cv2
import rospy
#from image_screw_detector import ImScrewDetector  # Image screw detector class
from sam_custom_messages.msg import object_state, diagnostics
from diagnostic_msgs.msg import KeyValue
from vision_recognition.detect import classifier

sys.path.insert(0, './vision_recognition')
print(sys.path)
class rs_cam:
    def __init__(self):
        # Create a pipeline
        self.pipeline = rs.pipeline()
        #Create a config and configure the pipeline to stream
        #  different resolutions of color and depth streams
        config = rs.config()
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        if args.depth:
            config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        
        # Start streaming
        profile = self.pipeline.start(config)

        if args.depth:
            # Getting the depth sensor's depth scale (see rs-align example for explanation)
            depth_sensor = profile.get_device().first_depth_sensor()
            depth_scale = depth_sensor.get_depth_scale()
            #print("Depth Scale is: " , depth_scale)
            # We will be removing the background of objects more than
            #  clipping_distance_in_meters meters away
            clipping_distance_in_meters = 0.5 #1 meter
            clipping_distance = clipping_distance_in_meters / depth_scale
            # Create an align object
            # rs.align allows us to perform alignment of depth frames to others frames
            # The "align_to" is the stream type to which we plan to align depth frames.
            align_to = rs.stream.color
            self.align = rs.align(align_to)

    def colour_frames(self, frames):
        color_frame = frames.get_color_frame()
        # Validate that both frames are valid
        if not color_frame:
            return
        color_image = np.asanyarray(color_frame.get_data())

        return color_image

    def depth_frames(self, frames):
        #frames.get_depth_frame() is a 640x360 depth image
        # Align the depth frame to color frame
        aligned_frames = self.align.process(frames)

        # Get aligned frames
        aligned_depth_frame = aligned_frames.get_depth_frame() # aligned_depth_frame is a 640x480 depth image
        color_frame = aligned_frames.get_color_frame()

        # Validate that both frames are valid
        if not aligned_depth_frame or not color_frame:
            return
        depth_image = np.asanyarray(aligned_depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.1), cv2.COLORMAP_JET)

        return color_image, depth_colormap, depth_image

    def scale(image): # zooms on image
        height, width, channels = image.shape
        scale = 2  # x? digital zoom
        centerX, centerY = int(height / 2), int(width / 2)
        radiusX, radiusY = int(height / (scale * 2)), int(width / (scale * 2))
        minX, maxX = centerX - radiusX, centerX + radiusX
        minY, maxY = centerY - radiusY, centerY + radiusY
        image = cv2.resize(image[minX:maxX, minY:maxY], (width, height), interpolation=cv2.INTER_LINEAR)
        return image

class diag_class:
    def __init__(self):
        frame_id = 'Realsense node'
        # Diagnostic message definitions
        self.diag_msg = diagnostics()
        self.diag_msg.Header.stamp = rospy.get_rostime()
        self.diag_msg.Header.seq = None
        self.diag_msg.Header.frame_id = frame_id
        self.diag_msg.UserId = args.user_id
        self.diag_msg.UserName = args.user_name
        self.diag_msg.DiagnosticStatus.level = 1 # 0:ok, 1:warning, 2:error, 3:stale
        self.diag_msg.DiagnosticStatus.name = frame_id
        self.diag_msg.DiagnosticStatus.message = "Starting..."
        self.diag_msg.DiagnosticStatus.hardware_id = "N/A"
        self.diag_msg.DiagnosticStatus.values = []

        self.diag_pub = rospy.Publisher('SystemStatus', diagnostics, queue_size=1)
        self.publish(1, "Starting...")

    def publish(self, level, message):
        self.diag_msg.DiagnosticStatus.level = level # 0:ok, 1:warning, 2:error, 3:stale
        self.diag_msg.DiagnosticStatus.message = message
        self.diag_msg.Header.stamp = rospy.get_rostime()
        if self.diag_msg.Header.seq is None:
            self.diag_msg.Header.seq = 0
        else:
            self.diag_msg.Header.seq += 1

        self.diag_pub.publish(self.diag_msg)
    
class obj_class:
    def __init__(self, names):
        frame_id = 'Realsense node'
        # Object message definitions
        self.obj_msg = object_state()
        self.obj_msg.Header.stamp = rospy.get_rostime()
        self.obj_msg.Header.seq = None
        self.obj_msg.Header.frame_id = frame_id
        self.obj_msg.Object.Id = None
        self.obj_msg.Object.Type = None
        self.obj_msg.Object.Info = None
        self.obj_msg.Pose.orientation.x = None
        self.obj_msg.Pose.orientation.y = None
        self.obj_msg.Pose.orientation.z = None
        self.obj_msg.Pose.orientation.w = None
        self.obj_msg.Pose.position.x = None
        self.obj_msg.Pose.position.y = None
        self.obj_msg.Pose.position.z = None
        self.names = names

        self.obj_pub = rospy.Publisher('ObjectStates', object_state, queue_size=1)

    def obj_publish(self, det):
        if self.obj_msg.Header.seq is None:
            self.obj_msg.Header.seq = 0
        else:
            self.obj_msg.Header.seq += 1
        
        for *xyxy, conf, cls in det:
            print(cls)
            print(conf)
            print(xyxy)
            self.obj_msg.Object.Id = 0
            self.obj_msg.Object.Type = int(cls)
            print(self.names[int(cls)])
            self.obj_msg.Object.Info = [self.names[int(cls)]]
            self.obj_msg.Pose.orientation.x = xyxy[0]
            self.obj_msg.Pose.orientation.y = xyxy[1]
            self.obj_msg.Pose.orientation.z = xyxy[2]
            self.obj_msg.Pose.orientation.w = xyxy[3]
            self.obj_msg.Pose.position.x = 0
            self.obj_msg.Pose.position.y = 0
            self.obj_msg.Pose.position.z = 0
            self.obj_msg.Header.stamp = rospy.get_rostime()

            self.obj_pub.publish(self.obj_msg)
            

def realsense_run():
    # ROS node setup
    rospy.init_node(f'Realsense_main', anonymous=True)
    diag_obj = diag_class()

    rate = rospy.Rate(10)
    if args.classify:
        try:
            frames = cam.pipeline.wait_for_frames()
            if args.depth:
                images = cam.depth_frames(frames)
            else:
                images = cam.colour_frames(frames)

            im_classifier = classifier(args.comp_device, args.weights, args.img_size, images, args.conf_thres, args.iou_thres)
            obj_obj = obj_class(im_classifier.names)
        
        except Exception as e:
            print("**Classifier Load Error**")
            traceback.print_exc(file=sys.stdout)
            diag_obj.publish(2, f"load classifier error: {e}")
            raise

    diag_timer = time.time()
    while not rospy.is_shutdown():
        try:
            # Get frameset of color and depth
            frames = cam.pipeline.wait_for_frames()

            if args.depth:
                images = cam.depth_frames(frames)
            else:
                images = cam.colour_frames(frames)

            if args.classify:
                try:
                    images, det = im_classifier.detect(images)
                    obj_obj.obj_publish(det)
                except Exception as e:
                    print("**Classifier Detection Error**")
                    traceback.print_exc(file=sys.stdout)
                    diag_obj.publish(2, f"load classifier error: {e}")

            # Remove background - Set pixels further than clipping_distance to grey
            #grey_color = 153
            #depth_image_3d = np.dstack((depth_image,depth_image,depth_image)) #depth image is 1 channel, color is 3 channels
            #bg_removed = np.where((depth_image_3d > clipping_distance) | (depth_image_3d <= 0), grey_color, color_image)
            #image = scale(bg_removed)

            if  (time.time()-diag_timer) > 1:
                print(time.time())
                diag_obj.publish(0, f"Running")
                diag_timer = time.time()

        except TypeError as e:
            time.sleep(1)
            diag_obj.publish(2, f"TypeError")
        except Exception as e:
            print("**Get Image Error**")
            diag_obj.publish(2, f"Realsense image error: {e}")
            traceback.print_exc(file=sys.stdout)
            break

        #im_screw_states, tally = im_screw_detect.detect_screws(image, args.disp)
        #im_screw_states = im_screw_states.tolist()
        if args.disp:
            if args.depth:
                images = np.hstack((images[0], images[1]))
            cv2.namedWindow('Realsense viewer', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('Realsense viewer', images)
            key = cv2.waitKey(1)
            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
            
        rate.sleep()


## Argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Run realsense vision recognition ROS node')
    parser.add_argument('--disp', '-V',
                        help='Enable displaying of camera image',
                        default=False,
                        action="store_true")
    parser.add_argument('--depth', '-D',
                        help='Depth active',
                        default=False,
                        action="store_true")
    parser.add_argument('--user_name', '-N',
                    help='Set name of user, default: unknown',
                    default='unknown',
                    action="store_true")
    parser.add_argument('--user_id', '-I',
                    help='Set id of user, default: None',
                    default=0,
                    action="store_true")
    parser.add_argument('--classify', '-C',
                    help='Classify image',
                    default=True,
                    action="store_true")
    parser.add_argument('--comp_device', default='cpu', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--img_size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--weights', nargs='+', type=str, default='best.pt', help='model.pt path(s)')
    parser.add_argument('--conf_thres', type=float, default=0.25, help='object confidence threshold')
    parser.add_argument('--iou_thres', type=float, default=0.45, help='IOU threshold for NMS')
    
    args = parser.parse_args()

    cam = rs_cam()

    try:
        realsense_run()
    except rospy.ROSInterruptException:
        print("realsense_run ROS exception")
    except Exception as e:
        print("**Image Error**")
        traceback.print_exc(file=sys.stdout)
    finally:
        cam.pipeline.stop()
        cv2.destroyAllWindows()
