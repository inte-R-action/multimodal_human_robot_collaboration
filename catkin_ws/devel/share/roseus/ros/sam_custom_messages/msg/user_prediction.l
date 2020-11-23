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
  :slots (_header _user_id _predictions ))

(defmethod sam_custom_messages::user_prediction
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:user_id __user_id) 0)
    ((:predictions __predictions) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _header __header)
   (setq _user_id (round __user_id))
   (setq _predictions __predictions)
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
  (:predictions
   (&optional __predictions)
   (if __predictions (setq _predictions __predictions)) _predictions)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int8 _user_id
    1
    ;; float64[] _predictions
    (* 8    (length _predictions)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int8 _user_id
       (write-byte _user_id s)
     ;; float64[] _predictions
     (write-long (length _predictions) s)
     (dotimes (i (length _predictions))
       (sys::poke (elt _predictions i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
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
   ;; float64[] _predictions
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _predictions (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _predictions i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get sam_custom_messages::user_prediction :md5sum-) "546e38fb2a5d19f634c167b97894dce3")
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
Header header
#
## ID of user (robot or human)
int8 user_id
#
## Probabilities of future capabilities being next
float64[] predictions
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



(provide :sam_custom_messages/user_prediction "546e38fb2a5d19f634c167b97894dce3")


