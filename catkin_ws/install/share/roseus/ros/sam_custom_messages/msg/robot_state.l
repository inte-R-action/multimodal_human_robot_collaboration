;; Auto-generated. Do not edit!


(when (boundp 'sam_custom_messages::robot_state)
  (if (not (find-package "SAM_CUSTOM_MESSAGES"))
    (make-package "SAM_CUSTOM_MESSAGES"))
  (shadow 'robot_state (find-package "SAM_CUSTOM_MESSAGES")))
(unless (find-package "SAM_CUSTOM_MESSAGES::ROBOT_STATE")
  (make-package "SAM_CUSTOM_MESSAGES::ROBOT_STATE"))

(in-package "ROS")
;;//! \htmlinclude robot_state.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sam_custom_messages::robot_state
  :super ros::object
  :slots (_Header _UserId _JointState _Pose ))

(defmethod sam_custom_messages::robot_state
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:UserId __UserId) 0)
    ((:JointState __JointState) (instance sensor_msgs::JointState :init))
    ((:Pose __Pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _UserId (round __UserId))
   (setq _JointState __JointState)
   (setq _Pose __Pose)
   self)
  (:Header
   (&rest __Header)
   (if (keywordp (car __Header))
       (send* _Header __Header)
     (progn
       (if __Header (setq _Header (car __Header)))
       _Header)))
  (:UserId
   (&optional __UserId)
   (if __UserId (setq _UserId __UserId)) _UserId)
  (:JointState
   (&rest __JointState)
   (if (keywordp (car __JointState))
       (send* _JointState __JointState)
     (progn
       (if __JointState (setq _JointState (car __JointState)))
       _JointState)))
  (:Pose
   (&rest __Pose)
   (if (keywordp (car __Pose))
       (send* _Pose __Pose)
     (progn
       (if __Pose (setq _Pose (car __Pose)))
       _Pose)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _Header
    (send _Header :serialization-length)
    ;; int8 _UserId
    1
    ;; sensor_msgs/JointState _JointState
    (send _JointState :serialization-length)
    ;; geometry_msgs/Pose _Pose
    (send _Pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _Header
       (send _Header :serialize s)
     ;; int8 _UserId
       (write-byte _UserId s)
     ;; sensor_msgs/JointState _JointState
       (send _JointState :serialize s)
     ;; geometry_msgs/Pose _Pose
       (send _Pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _Header
     (send _Header :deserialize buf ptr-) (incf ptr- (send _Header :serialization-length))
   ;; int8 _UserId
     (setq _UserId (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _UserId 127) (setq _UserId (- _UserId 256)))
   ;; sensor_msgs/JointState _JointState
     (send _JointState :deserialize buf ptr-) (incf ptr- (send _JointState :serialization-length))
   ;; geometry_msgs/Pose _Pose
     (send _Pose :deserialize buf ptr-) (incf ptr- (send _Pose :serialization-length))
   ;;
   self)
  )

(setf (get sam_custom_messages::robot_state :md5sum-) "a83e1d499637a29726a1122a310ad6b8")
(setf (get sam_custom_messages::robot_state :datatype-) "sam_custom_messages/robot_state")
(setf (get sam_custom_messages::robot_state :definition-)
      "## Message containing id, joint states and end effector position of robot
#
## std_msgs/Header.msg
# sequence ID: consecutively increasing ID 
# uint32 seq
# Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
# time stamp
# Frame this data is associated with
# string frame_id
Header Header
#
## ID of user (robot or human)
int8 UserId
#
# sensor_msgs/JointState.msg
# This is a message that holds data to describe the state of a set of torque controlled joints. 
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and 
#  * the effort that is applied in the joint (Nm or N).
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
# This message consists of a multiple arrays, one for each part of the joint state. 
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty. 
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.
# Header header
# string[] name
# float64[] position
# float64[] velocity
# float64[] effort
sensor_msgs/JointState JointState
#
# geometry_msgs/Pose.msg
# A representation of end effector pose in free space, composed of position and orientation. 
# Point position
# Quaternion orientation
geometry_msgs/Pose Pose
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: sensor_msgs/JointState
# This is a message that holds data to describe the state of a set of torque controlled joints. 
#
# The state of each joint (revolute or prismatic) is defined by:
#  * the position of the joint (rad or m),
#  * the velocity of the joint (rad/s or m/s) and 
#  * the effort that is applied in the joint (Nm or N).
#
# Each joint is uniquely identified by its name
# The header specifies the time at which the joint states were recorded. All the joint states
# in one message have to be recorded at the same time.
#
# This message consists of a multiple arrays, one for each part of the joint state. 
# The goal is to make each of the fields optional. When e.g. your joints have no
# effort associated with them, you can leave the effort array empty. 
#
# All arrays in this message should have the same size, or be empty.
# This is the only way to uniquely associate the joint name with the correct
# states.


Header header

string[] name
float64[] position
float64[] velocity
float64[] effort

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :sam_custom_messages/robot_state "a83e1d499637a29726a1122a310ad6b8")


