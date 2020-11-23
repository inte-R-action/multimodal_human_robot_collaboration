;; Auto-generated. Do not edit!


(when (boundp 'sam_custom_messages::hand_pos)
  (if (not (find-package "SAM_CUSTOM_MESSAGES"))
    (make-package "SAM_CUSTOM_MESSAGES"))
  (shadow 'hand_pos (find-package "SAM_CUSTOM_MESSAGES")))
(unless (find-package "SAM_CUSTOM_MESSAGES::HAND_POS")
  (make-package "SAM_CUSTOM_MESSAGES::HAND_POS"))

(in-package "ROS")
;;//! \htmlinclude hand_pos.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sam_custom_messages::hand_pos
  :super ros::object
  :slots (_header _user_id _user_name _hand _pose ))

(defmethod sam_custom_messages::hand_pos
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:user_id __user_id) 0)
    ((:user_name __user_name) "")
    ((:hand __hand) 0)
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _user_id (round __user_id))
   (setq _user_name (string __user_name))
   (setq _hand (round __hand))
   (setq _pose __pose)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:user_id
   (&optional __user_id)
   (if __user_id (setq _user_id __user_id)) _user_id)
  (:user_name
   (&optional __user_name)
   (if __user_name (setq _user_name __user_name)) _user_name)
  (:hand
   (&optional __hand)
   (if __hand (setq _hand __hand)) _hand)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int8 _user_id
    1
    ;; string _user_name
    4 (length _user_name)
    ;; int8 _hand
    1
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int8 _user_id
       (write-byte _user_id s)
     ;; string _user_name
       (write-long (length _user_name) s) (princ _user_name s)
     ;; int8 _hand
       (write-byte _hand s)
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int8 _user_id
     (setq _user_id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _user_id 127) (setq _user_id (- _user_id 256)))
   ;; string _user_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _user_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int8 _hand
     (setq _hand (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _hand 127) (setq _hand (- _hand 256)))
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;;
   self)
  )

(setf (get sam_custom_messages::hand_pos :md5sum-) "1c6006785295f1dfe86ef734b697fe78")
(setf (get sam_custom_messages::hand_pos :datatype-) "sam_custom_messages/hand_pos")
(setf (get sam_custom_messages::hand_pos :definition-)
      "## Message containing location of a users hand
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
Header header
#
## ID of user (robot or human)
int8 user_id
#
## Name of user (robot or human)
string user_name
#
## Which hand location is for, 0:left, 1:right
int8 hand
#
# geometry_msgs/Pose.msg
# A representation of pose in free space, composed of position and orientation. 
# Point position
# Quaternion orientation
geometry_msgs/Pose pose
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



(provide :sam_custom_messages/hand_pos "1c6006785295f1dfe86ef734b697fe78")


