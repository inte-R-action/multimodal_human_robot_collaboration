;; Auto-generated. Do not edit!


(when (boundp 'sam_custom_messages::current_action)
  (if (not (find-package "SAM_CUSTOM_MESSAGES"))
    (make-package "SAM_CUSTOM_MESSAGES"))
  (shadow 'current_action (find-package "SAM_CUSTOM_MESSAGES")))
(unless (find-package "SAM_CUSTOM_MESSAGES::CURRENT_ACTION")
  (make-package "SAM_CUSTOM_MESSAGES::CURRENT_ACTION"))

(in-package "ROS")
;;//! \htmlinclude current_action.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sam_custom_messages::current_action
  :super ros::object
  :slots (_Header _UserId _UserName _ActionProbs ))

(defmethod sam_custom_messages::current_action
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:UserId __UserId) 0)
    ((:UserName __UserName) "")
    ((:ActionProbs __ActionProbs) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _UserId (round __UserId))
   (setq _UserName (string __UserName))
   (setq _ActionProbs __ActionProbs)
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
  (:ActionProbs
   (&optional __ActionProbs)
   (if __ActionProbs (setq _ActionProbs __ActionProbs)) _ActionProbs)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _Header
    (send _Header :serialization-length)
    ;; int8 _UserId
    1
    ;; string _UserName
    4 (length _UserName)
    ;; float64[] _ActionProbs
    (* 8    (length _ActionProbs)) 4
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
     ;; float64[] _ActionProbs
     (write-long (length _ActionProbs) s)
     (dotimes (i (length _ActionProbs))
       (sys::poke (elt _ActionProbs i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
   ;; string _UserName
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _UserName (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64[] _ActionProbs
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _ActionProbs (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _ActionProbs i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get sam_custom_messages::current_action :md5sum-) "5a22afcb1583334c436419d2dee34df6")
(setf (get sam_custom_messages::current_action :datatype-) "sam_custom_messages/current_action")
(setf (get sam_custom_messages::current_action :definition-)
      "## Message containing predictions of what action user is currently performing
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
## Probabilities of curent actions
float64[] ActionProbs
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

")



(provide :sam_custom_messages/current_action "5a22afcb1583334c436419d2dee34df6")


