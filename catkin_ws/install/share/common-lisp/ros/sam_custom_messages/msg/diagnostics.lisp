; Auto-generated. Do not edit!


(cl:in-package sam_custom_messages-msg)


;//! \htmlinclude diagnostics.msg.html

(cl:defclass <diagnostics> (roslisp-msg-protocol:ros-message)
  ((Header
    :reader Header
    :initarg :Header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (UserId
    :reader UserId
    :initarg :UserId
    :type cl:fixnum
    :initform 0)
   (UserName
    :reader UserName
    :initarg :UserName
    :type cl:string
    :initform "")
   (DiagnosticStatus
    :reader DiagnosticStatus
    :initarg :DiagnosticStatus
    :type diagnostic_msgs-msg:DiagnosticStatus
    :initform (cl:make-instance 'diagnostic_msgs-msg:DiagnosticStatus)))
)

(cl:defclass diagnostics (<diagnostics>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <diagnostics>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'diagnostics)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sam_custom_messages-msg:<diagnostics> is deprecated: use sam_custom_messages-msg:diagnostics instead.")))

(cl:ensure-generic-function 'Header-val :lambda-list '(m))
(cl:defmethod Header-val ((m <diagnostics>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:Header-val is deprecated.  Use sam_custom_messages-msg:Header instead.")
  (Header m))

(cl:ensure-generic-function 'UserId-val :lambda-list '(m))
(cl:defmethod UserId-val ((m <diagnostics>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:UserId-val is deprecated.  Use sam_custom_messages-msg:UserId instead.")
  (UserId m))

(cl:ensure-generic-function 'UserName-val :lambda-list '(m))
(cl:defmethod UserName-val ((m <diagnostics>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:UserName-val is deprecated.  Use sam_custom_messages-msg:UserName instead.")
  (UserName m))

(cl:ensure-generic-function 'DiagnosticStatus-val :lambda-list '(m))
(cl:defmethod DiagnosticStatus-val ((m <diagnostics>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:DiagnosticStatus-val is deprecated.  Use sam_custom_messages-msg:DiagnosticStatus instead.")
  (DiagnosticStatus m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <diagnostics>) ostream)
  "Serializes a message object of type '<diagnostics>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'UserId)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'UserName))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'UserName))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'DiagnosticStatus) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <diagnostics>) istream)
  "Deserializes a message object of type '<diagnostics>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'UserId) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'UserName) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'UserName) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'DiagnosticStatus) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<diagnostics>)))
  "Returns string type for a message object of type '<diagnostics>"
  "sam_custom_messages/diagnostics")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'diagnostics)))
  "Returns string type for a message object of type 'diagnostics"
  "sam_custom_messages/diagnostics")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<diagnostics>)))
  "Returns md5sum for a message object of type '<diagnostics>"
  "d697c2568ce7a485465d81f6f70b8306")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'diagnostics)))
  "Returns md5sum for a message object of type 'diagnostics"
  "d697c2568ce7a485465d81f6f70b8306")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<diagnostics>)))
  "Returns full string definition for message of type '<diagnostics>"
  (cl:format cl:nil "## Message containing diagnostic information for sensors/devices/users within the system~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header Header~%#~%## ID of user (robot or human)~%int8 UserId~%#~%## Name of user (robot or human)~%string UserName~%#~%## diagnostic_msgs/DiagnosticStatus.msg~%# Possible levels of operations~%# byte OK=0~%# byte WARN=1~%# byte ERROR=2~%# byte STALE=3~%# byte level # level of operation enumerated above ~%# string name # a description of the test/component reporting~%# string message # a description of the status~%# string hardware_id # a hardware unique string~%# KeyValue[] values # an array of values associated with the status~%diagnostic_msgs/DiagnosticStatus DiagnosticStatus~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: diagnostic_msgs/DiagnosticStatus~%# This message holds the status of an individual component of the robot.~%# ~%~%# Possible levels of operations~%byte OK=0~%byte WARN=1~%byte ERROR=2~%byte STALE=3~%~%byte level # level of operation enumerated above ~%string name # a description of the test/component reporting~%string message # a description of the status~%string hardware_id # a hardware unique string~%KeyValue[] values # an array of values associated with the status~%~%~%================================================================================~%MSG: diagnostic_msgs/KeyValue~%string key # what to label this value when viewing~%string value # a value to track over time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'diagnostics)))
  "Returns full string definition for message of type 'diagnostics"
  (cl:format cl:nil "## Message containing diagnostic information for sensors/devices/users within the system~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header Header~%#~%## ID of user (robot or human)~%int8 UserId~%#~%## Name of user (robot or human)~%string UserName~%#~%## diagnostic_msgs/DiagnosticStatus.msg~%# Possible levels of operations~%# byte OK=0~%# byte WARN=1~%# byte ERROR=2~%# byte STALE=3~%# byte level # level of operation enumerated above ~%# string name # a description of the test/component reporting~%# string message # a description of the status~%# string hardware_id # a hardware unique string~%# KeyValue[] values # an array of values associated with the status~%diagnostic_msgs/DiagnosticStatus DiagnosticStatus~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: diagnostic_msgs/DiagnosticStatus~%# This message holds the status of an individual component of the robot.~%# ~%~%# Possible levels of operations~%byte OK=0~%byte WARN=1~%byte ERROR=2~%byte STALE=3~%~%byte level # level of operation enumerated above ~%string name # a description of the test/component reporting~%string message # a description of the status~%string hardware_id # a hardware unique string~%KeyValue[] values # an array of values associated with the status~%~%~%================================================================================~%MSG: diagnostic_msgs/KeyValue~%string key # what to label this value when viewing~%string value # a value to track over time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <diagnostics>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Header))
     1
     4 (cl:length (cl:slot-value msg 'UserName))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'DiagnosticStatus))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <diagnostics>))
  "Converts a ROS message object to a list"
  (cl:list 'diagnostics
    (cl:cons ':Header (Header msg))
    (cl:cons ':UserId (UserId msg))
    (cl:cons ':UserName (UserName msg))
    (cl:cons ':DiagnosticStatus (DiagnosticStatus msg))
))
