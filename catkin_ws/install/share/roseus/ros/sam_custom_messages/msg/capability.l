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
  :slots (_Header _UserId _Object _Pose _Type _Info ))

(defmethod sam_custom_messages::capability
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:UserId __UserId) 0)
    ((:Object __Object) (instance sam_custom_messages::Object :init))
    ((:Pose __Pose) (instance geometry_msgs::Pose :init))
    ((:Type __Type) 0)
    ((:Info __Info) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _UserId (round __UserId))
   (setq _Object __Object)
   (setq _Pose __Pose)
   (setq _Type (round __Type))
   (setq _Info __Info)
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
  (:Type
   (&optional __Type)
   (if __Type (setq _Type __Type)) _Type)
  (:Info
   (&optional __Info)
   (if __Info (setq _Info __Info)) _Info)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _Header
    (send _Header :serialization-length)
    ;; int8 _UserId
    1
    ;; sam_custom_messages/Object _Object
    (send _Object :serialization-length)
    ;; geometry_msgs/Pose _Pose
    (send _Pose :serialization-length)
    ;; int8 _Type
    1
    ;; string[] _Info
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _Info)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _Header
       (send _Header :serialize s)
     ;; int8 _UserId
       (write-byte _UserId s)
     ;; sam_custom_messages/Object _Object
       (send _Object :serialize s)
     ;; geometry_msgs/Pose _Pose
       (send _Pose :serialize s)
     ;; int8 _Type
       (write-byte _Type s)
     ;; string[] _Info
     (write-long (length _Info) s)
     (dolist (elem _Info)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _Header
     (send _Header :deserialize buf ptr-) (incf ptr- (send _Header :serialization-length))
   ;; int8 _UserId
     (setq _UserId (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _UserId 127) (setq _UserId (- _UserId 256)))
   ;; sam_custom_messages/Object _Object
     (send _Object :deserialize buf ptr-) (incf ptr- (send _Object :serialization-length))
   ;; geometry_msgs/Pose _Pose
     (send _Pose :deserialize buf ptr-) (incf ptr- (send _Pose :serialization-length))
   ;; int8 _Type
     (setq _Type (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _Type 127) (setq _Type (- _Type 256)))
   ;; string[] _Info
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _Info (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _Info i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get sam_custom_messages::capability :md5sum-) "0d980a9edeb2165abe1fcce834dfe67e")
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
Header Header
#
## ID of user (robot or human)
int8 UserId
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
#
# ID of capability type
int8 Type
#
# Details on capability being performed
string[] Info
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



(provide :sam_custom_messages/capability "0d980a9edeb2165abe1fcce834dfe67e")


