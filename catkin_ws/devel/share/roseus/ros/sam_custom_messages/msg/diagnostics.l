;; Auto-generated. Do not edit!


(when (boundp 'sam_custom_messages::diagnostics)
  (if (not (find-package "SAM_CUSTOM_MESSAGES"))
    (make-package "SAM_CUSTOM_MESSAGES"))
  (shadow 'diagnostics (find-package "SAM_CUSTOM_MESSAGES")))
(unless (find-package "SAM_CUSTOM_MESSAGES::DIAGNOSTICS")
  (make-package "SAM_CUSTOM_MESSAGES::DIAGNOSTICS"))

(in-package "ROS")
;;//! \htmlinclude diagnostics.msg.html
(if (not (find-package "DIAGNOSTIC_MSGS"))
  (ros::roseus-add-msgs "diagnostic_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sam_custom_messages::diagnostics
  :super ros::object
  :slots (_header _user_id _diagnosticstatus ))

(defmethod sam_custom_messages::diagnostics
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:user_id __user_id) 0)
    ((:diagnosticstatus __diagnosticstatus) (instance diagnostic_msgs::DiagnosticStatus :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _user_id (round __user_id))
   (setq _diagnosticstatus __diagnosticstatus)
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
  (:diagnosticstatus
   (&rest __diagnosticstatus)
   (if (keywordp (car __diagnosticstatus))
       (send* _diagnosticstatus __diagnosticstatus)
     (progn
       (if __diagnosticstatus (setq _diagnosticstatus (car __diagnosticstatus)))
       _diagnosticstatus)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int8 _user_id
    1
    ;; diagnostic_msgs/DiagnosticStatus _diagnosticstatus
    (send _diagnosticstatus :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int8 _user_id
       (write-byte _user_id s)
     ;; diagnostic_msgs/DiagnosticStatus _diagnosticstatus
       (send _diagnosticstatus :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int8 _user_id
     (setq _user_id (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _user_id 127) (setq _user_id (- _user_id 256)))
   ;; diagnostic_msgs/DiagnosticStatus _diagnosticstatus
     (send _diagnosticstatus :deserialize buf ptr-) (incf ptr- (send _diagnosticstatus :serialization-length))
   ;;
   self)
  )

(setf (get sam_custom_messages::diagnostics :md5sum-) "166ea485f1a6548735c38b7c8eac661c")
(setf (get sam_custom_messages::diagnostics :datatype-) "sam_custom_messages/diagnostics")
(setf (get sam_custom_messages::diagnostics :definition-)
      "## Message containing diagnostic information for sensors/devices/users within the system
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
## diagnostic_msgs/DiagnosticStatus.msg
# Possible levels of operations
# byte OK=0
# byte WARN=1
# byte ERROR=2
# byte STALE=3
# byte level # level of operation enumerated above 
# string name # a description of the test/component reporting
# string message # a description of the status
# string hardware_id # a hardware unique string
# KeyValue[] values # an array of values associated with the status
diagnostic_msgs/DiagnosticStatus diagnosticstatus
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
MSG: diagnostic_msgs/DiagnosticStatus
# This message holds the status of an individual component of the robot.
# 

# Possible levels of operations
byte OK=0
byte WARN=1
byte ERROR=2
byte STALE=3

byte level # level of operation enumerated above 
string name # a description of the test/component reporting
string message # a description of the status
string hardware_id # a hardware unique string
KeyValue[] values # an array of values associated with the status


================================================================================
MSG: diagnostic_msgs/KeyValue
string key # what to label this value when viewing
string value # a value to track over time

")



(provide :sam_custom_messages/diagnostics "166ea485f1a6548735c38b7c8eac661c")


