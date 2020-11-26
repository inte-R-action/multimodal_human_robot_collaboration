;; Auto-generated. Do not edit!


(when (boundp 'sam_custom_messages::user_prediction)
  (if (not (find-package "SAM_CUSTOM_MESSAGES"))
    (make-package "SAM_CUSTOM_MESSAGES"))
  (shadow 'user_prediction (find-package "SAM_CUSTOM_MESSAGES")))
(unless (find-package "SAM_CUSTOM_MESSAGES::USER_PREDICTION")
  (make-package "SAM_CUSTOM_MESSAGES::USER_PREDICTION"))

(in-package "ROS")
;;//! \htmlinclude user_prediction.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sam_custom_messages::user_prediction
  :super ros::object
  :slots (_Header _UserId _Predictions ))

(defmethod sam_custom_messages::user_prediction
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:UserId __UserId) 0)
    ((:Predictions __Predictions) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _UserId (round __UserId))
   (setq _Predictions __Predictions)
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
  (:Predictions
   (&optional __Predictions)
   (if __Predictions (setq _Predictions __Predictions)) _Predictions)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _Header
    (send _Header :serialization-length)
    ;; int8 _UserId
    1
    ;; float64[] _Predictions
    (* 8    (length _Predictions)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _Header
       (send _Header :serialize s)
     ;; int8 _UserId
       (write-byte _UserId s)
     ;; float64[] _Predictions
     (write-long (length _Predictions) s)
     (dotimes (i (length _Predictions))
       (sys::poke (elt _Predictions i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
   ;; float64[] _Predictions
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _Predictions (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _Predictions i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get sam_custom_messages::user_prediction :md5sum-) "a0a99151d0431e7e25d8e440508ac456")
(setf (get sam_custom_messages::user_prediction :datatype-) "sam_custom_messages/user_prediction")
(setf (get sam_custom_messages::user_prediction :definition-)
      "## Message containing predictions of what user capability will be performed next
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
## Probabilities of future capabilities being next
float64[] Predictions
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



(provide :sam_custom_messages/user_prediction "a0a99151d0431e7e25d8e440508ac456")


