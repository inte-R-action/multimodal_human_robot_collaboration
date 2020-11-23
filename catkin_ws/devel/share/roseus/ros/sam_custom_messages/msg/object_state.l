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
  :slots (_header _object _pose ))

(defmethod sam_custom_messages::object_state
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:object __object) (instance sam_custom_messages::Object :init))
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _object __object)
   (setq _pose __pose)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
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
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; sam_custom_messages/Object _object
    (send _object :serialization-length)
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; sam_custom_messages/Object _object
       (send _object :serialize s)
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; sam_custom_messages/Object _object
     (send _object :deserialize buf ptr-) (incf ptr- (send _object :serialization-length))
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;;
   self)
  )

(setf (get sam_custom_messages::object_state :md5sum-) "2219f508c564a641c1ef4997ea740e7e")
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
Header header
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



(provide :sam_custom_messages/object_state "2219f508c564a641c1ef4997ea740e7e")


