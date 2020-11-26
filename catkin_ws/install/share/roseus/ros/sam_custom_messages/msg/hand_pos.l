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
  :slots (_Header _UserId _UserName _Hand _Pose ))

(defmethod sam_custom_messages::hand_pos
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:UserId __UserId) 0)
    ((:UserName __UserName) "")
    ((:Hand __Hand) 0)
    ((:Pose __Pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _UserId (round __UserId))
   (setq _UserName (string __UserName))
   (setq _Hand (round __Hand))
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
  (:UserName
   (&optional __UserName)
   (if __UserName (setq _UserName __UserName)) _UserName)
  (:Hand
   (&optional __Hand)
   (if __Hand (setq _Hand __Hand)) _Hand)
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
    ;; string _UserName
    4 (length _UserName)
    ;; int8 _Hand
    1
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
     ;; string _UserName
       (write-long (length _UserName) s) (princ _UserName s)
     ;; int8 _Hand
       (write-byte _Hand s)
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
   ;; string _UserName
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _UserName (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int8 _Hand
     (setq _Hand (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _Hand 127) (setq _Hand (- _Hand 256)))
   ;; geometry_msgs/Pose _Pose
     (send _Pose :deserialize buf ptr-) (incf ptr- (send _Pose :serialization-length))
   ;;
   self)
  )

(setf (get sam_custom_messages::hand_pos :md5sum-) "c3a4ac1d92f14f60ae68b389fe0ff85a")
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
Header Header
#
## ID of user (robot or human)
int8 UserId
#
## Name of user (robot or human)
string UserName
#
## Which hand location is for, 0:left, 1:right
int8 Hand
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



(provide :sam_custom_messages/hand_pos "c3a4ac1d92f14f60ae68b389fe0ff85a")


