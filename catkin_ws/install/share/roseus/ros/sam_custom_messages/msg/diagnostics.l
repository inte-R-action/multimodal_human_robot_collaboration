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
  :slots (_Header _UserId _UserName _DiagnosticStatus ))

(defmethod sam_custom_messages::diagnostics
  (:init
   (&key
    ((:Header __Header) (instance std_msgs::Header :init))
    ((:UserId __UserId) 0)
    ((:UserName __UserName) "")
    ((:DiagnosticStatus __DiagnosticStatus) (instance diagnostic_msgs::DiagnosticStatus :init))
    )
   (send-super :init)
   (setq _Header __Header)
   (setq _UserId (round __UserId))
   (setq _UserName (string __UserName))
   (setq _DiagnosticStatus __DiagnosticStatus)
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
  (:DiagnosticStatus
   (&rest __DiagnosticStatus)
   (if (keywordp (car __DiagnosticStatus))
       (send* _DiagnosticStatus __DiagnosticStatus)
     (progn
       (if __DiagnosticStatus (setq _DiagnosticStatus (car __DiagnosticStatus)))
       _DiagnosticStatus)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _Header
    (send _Header :serialization-length)
    ;; int8 _UserId
    1
    ;; string _UserName
    4 (length _UserName)
    ;; diagnostic_msgs/DiagnosticStatus _DiagnosticStatus
    (send _DiagnosticStatus :serialization-length)
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
     ;; diagnostic_msgs/DiagnosticStatus _DiagnosticStatus
       (send _DiagnosticStatus :serialize s)
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
   ;; diagnostic_msgs/DiagnosticStatus _DiagnosticStatus
     (send _DiagnosticStatus :deserialize buf ptr-) (incf ptr- (send _DiagnosticStatus :serialization-length))
   ;;
   self)
  )

(setf (get sam_custom_messages::diagnostics :md5sum-) "d697c2568ce7a485465d81f6f70b8306")
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
Header Header
#
## ID of user (robot or human)
int8 UserId
#
## Name of user (robot or human)
string UserName
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
diagnostic_msgs/DiagnosticStatus DiagnosticStatus
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



(provide :sam_custom_messages/diagnostics "d697c2568ce7a485465d81f6f70b8306")


