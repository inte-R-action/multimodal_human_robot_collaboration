;; Auto-generated. Do not edit!


(when (boundp 'sam_custom_messages::object_state)
  (if (not (find-package "SAM_CUSTOM_MESSAGES"))
    (make-package "SAM_CUSTOM_MESSAGES"))
  (shadow 'object_state (find-package "SAM_CUSTOM_MESSAGES")))
(unless (find-package "SAM_CUSTOM_MESSAGES::OBJECT_STATE")
  (make-package "SAM_CUSTOM_MESSAGES::OBJECT_STATE"))

(in-package "ROS")
;;//! \htmlinclude object_state.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sam_custom_messages::object_state
  :super ros::object
  :slots (_Header _Object _Pose ))

(defmethod sam_custom_messages::object_state
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:Object __Object) (instance sam_custom_messages::Object :init))
    ((:Pose __Pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _Object __Object)
   (setq _Pose __Pose)
   self)
  (:Header
   (&rest __Header)
   (if (keywordp (car __Header))
       (send* _Header __Header)
     (progn
       (if __Header (setq _Header (car __Header)))
       _Header)))
  (:Object
   (&rest __Object)
   (if (keywordp (car __Object))
       (send* _Object __Object)
     (progn
       (if __Object (setq _Object (car __Object)))
       _Object)))
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
    ;; sam_custom_messages/Object _Object
    (send _Object :serialization-length)
    ;; geometry_msgs/Pose _Pose
    (send _Pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _Header
       (send _Header :serialize s)
     ;; sam_custom_messages/Object _Object
       (send _Object :serialize s)
     ;; geometry_msgs/Pose _Pose
       (send _Pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _Header
     (send _Header :deserialize buf ptr-) (incf ptr- (send _Header :serialization-length))
   ;; sam_custom_messages/Object _Object
     (send _Object :deserialize buf ptr-) (incf ptr- (send _Object :serialization-length))
   ;; geometry_msgs/Pose _Pose
     (send _Pose :deserialize buf ptr-) (incf ptr- (send _Pose :serialization-length))
   ;;
   self)
  )

(setf (get sam_custom_messages::object_state :md5sum-) "8cae51b844af17ba12968d72494305e9")
(setf (get sam_custom_messages::object_state :datatype-) "sam_custom_messages/object_state")
(setf (get sam_custom_messages::object_state :definition-)
      "## Message containing information on location, type and details about an object in the environment
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
## object.msg
# Information on object type and further details
# int8 id
# int8 type 
# string[] info
Object Object
#
# geometry_msgs/Pose.msg
# A representation of pose in free space, composed of position and orientation. 
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
MSG: sam_custom_messages/Object
# Message containg information on objects within environment
#
# Unique ID of object
int8 Id
#
# Type of object ID
int8 Type
#
# Additional information on object
string[] Info
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



(provide :sam_custom_messages/object_state "8cae51b844af17ba12968d72494305e9")


