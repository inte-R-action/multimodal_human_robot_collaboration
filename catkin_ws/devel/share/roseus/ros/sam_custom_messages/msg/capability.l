;; Auto-generated. Do not edit!


(when (boundp 'sam_custom_messages::capability)
  (if (not (find-package "SAM_CUSTOM_MESSAGES"))
    (make-package "SAM_CUSTOM_MESSAGES"))
  (shadow 'capability (find-package "SAM_CUSTOM_MESSAGES")))
(unless (find-package "SAM_CUSTOM_MESSAGES::CAPABILITY")
  (make-package "SAM_CUSTOM_MESSAGES::CAPABILITY"))

(in-package "ROS")
;;//! \htmlinclude capability.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sam_custom_messages::capability
  :super ros::object
  :slots (_header _user_id _object _pose _type _info ))

(defmethod sam_custom_messages::capability
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:user_id __user_id) 0)
    ((:object __object) (instance sam_custom_messages::Object :init))
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    ((:type __type) 0)
    ((:info __info) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _user_id (round __user_id))
   (setq _object __object)
   (setq _pose __pose)
   (setq _type (round __type))
   (setq _info __info)
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
  (:object
   (&rest __object)
   (if (keywordp (car __object))
       (send* _object __object)
     (progn
       (if __object (setq _object (car __object)))
       _object)))
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:info
   (&optional __info)
   (if __info (setq _info __info)) _info)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int8 _user_id
    1
    ;; sam_custom_messages/Object _object
    (send _object :serialization-length)
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ;; int8 _type
    1
    ;; string[] _info
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _info)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int8 _user_id
       (write-byte _user_id s)
     ;; sam_custom_messages/Object _object
       (send _object :serialize s)
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;; int8 _type
       (write-byte _type s)
     ;; string[] _info
     (write-long (length _info) s)
     (dolist (elem _info)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int8 _user_id
     (setq _user_id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _user_id 127) (setq _user_id (- _user_id 256)))
   ;; sam_custom_messages/Object _object
     (send _object :deserialize buf ptr-) (incf ptr- (send _object :serialization-length))
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;; int8 _type
     (setq _type (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _type 127) (setq _type (- _type 256)))
   ;; string[] _info
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _info (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _info i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get sam_custom_messages::capability :md5sum-) "1e2d1f854bb1612f413022281c6219c9")
(setf (get sam_custom_messages::capability :datatype-) "sam_custom_messages/capability")
(setf (get sam_custom_messages::capability :definition-)
      "## Message containing information on what capability user (robot or human) currently performing
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
## object.msg
# Information on object type and further details
# int8 id
# int8 type 
# string[] info
Object object
#
# geometry_msgs/Pose.msg
# A representation of pose in free space, composed of position and orientation. 
# Point position
# Quaternion orientation
geometry_msgs/Pose pose
#
# ID of capability type
int8 type
#
# Details on capability being performed
string[] info
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
MSG: sam_custom_messages/Object
# Message containg information on objects within environment
#
# Unique ID of object
int8 id
#
# Type of object ID
int8 type
#
# Additional information on object
string[] info
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



(provide :sam_custom_messages/capability "1e2d1f854bb1612f413022281c6219c9")


