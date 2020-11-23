; Auto-generated. Do not edit!


(cl:in-package sam_custom_messages-msg)


;//! \htmlinclude diagnostics.msg.html

(cl:defclass <diagnostics> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (user_id
    :reader user_id
    :initarg :user_id
    :type cl:fixnum
    :initform 0)
   (diagnosticstatus
    :reader diagnosticstatus
    :initarg :diagnosticstatus
    :type diagnostic_msgs-msg:DiagnosticStatus
    :initform (cl:make-instance 'diagnostic_msgs-msg:DiagnosticStatus)))
)

(cl:defclass diagnostics (<diagnostics>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <diagnostics>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'diagnostics)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sam_custom_messages-msg:<diagnostics> is deprecated: use sam_custom_messages-msg:diagnostics instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <diagnostics>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:header-val is deprecated.  Use sam_custom_messages-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'user_id-val :lambda-list '(m))
(cl:defmethod user_id-val ((m <diagnostics>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:user_id-val is deprecated.  Use sam_custom_messages-msg:user_id instead.")
  (user_id m))

(cl:ensure-generic-function 'diagnosticstatus-val :lambda-list '(m))
(cl:defmethod diagnosticstatus-val ((m <diagnostics>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:diagnosticstatus-val is deprecated.  Use sam_custom_messages-msg:diagnosticstatus instead.")
  (diagnosticstatus m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <diagnostics>) ostream)
  "Serializes a message object of type '<diagnostics>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'user_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'diagnosticstatus) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <diagnostics>) istream)
  "Deserializes a message object of type '<diagnostics>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'user_id) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'diagnosticstatus) istream)
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
  "166ea485f1a6548735c38b7c8eac661c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'diagnostics)))
  "Returns md5sum for a message object of type 'diagnostics"
  "166ea485f1a6548735c38b7c8eac661c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<diagnostics>)))
  "Returns full string definition for message of type '<diagnostics>"
  (cl:format cl:nil "## Message containing diagnostic information for sensors/devices/users within the system~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header header~%#~%## ID of user (robot or human)~%int8 user_id~%#~%## diagnostic_msgs/DiagnosticStatus.msg~%# Possible levels of operations~%# byte OK=0~%# byte WARN=1~%# byte ERROR=2~%# byte STALE=3~%# byte level # level of operation enumerated above ~%# string name # a description of the test/component reporting~%# string message # a description of the status~%# string hardware_id # a hardware unique string~%# KeyValue[] values # an array of values associated with the status~%diagnostic_msgs/DiagnosticStatus diagnosticstatus~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: diagnostic_msgs/DiagnosticStatus~%# This message holds the status of an individual component of the robot.~%# ~%~%# Possible levels of operations~%byte OK=0~%byte WARN=1~%byte ERROR=2~%byte STALE=3~%~%byte level # level of operation enumerated above ~%string name # a description of the test/component reporting~%string message # a description of the status~%string hardware_id # a hardware unique string~%KeyValue[] values # an array of values associated with the status~%~%~%================================================================================~%MSG: diagnostic_msgs/KeyValue~%string key # what to label this value when viewing~%string value # a value to track over time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'diagnostics)))
  "Returns full string definition for message of type 'diagnostics"
  (cl:format cl:nil "## Message containing diagnostic information for sensors/devices/users within the system~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header header~%#~%## ID of user (robot or human)~%int8 user_id~%#~%## diagnostic_msgs/DiagnosticStatus.msg~%# Possible levels of operations~%# byte OK=0~%# byte WARN=1~%# byte ERROR=2~%# byte STALE=3~%# byte level # level of operation enumerated above ~%# string name # a description of the test/component reporting~%# string message # a description of the status~%# string hardware_id # a hardware unique string~%# KeyValue[] values # an array of values associated with the status~%diagnostic_msgs/DiagnosticStatus diagnosticstatus~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: diagnostic_msgs/DiagnosticStatus~%# This message holds the status of an individual component of the robot.~%# ~%~%# Possible levels of operations~%byte OK=0~%byte WARN=1~%byte ERROR=2~%byte STALE=3~%~%byte level # level of operation enumerated above ~%string name # a description of the test/component reporting~%string message # a description of the status~%string hardware_id # a hardware unique string~%KeyValue[] values # an array of values associated with the status~%~%~%================================================================================~%MSG: diagnostic_msgs/KeyValue~%string key # what to label this value when viewing~%string value # a value to track over time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <diagnostics>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'diagnosticstatus))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <diagnostics>))
  "Converts a ROS message object to a list"
  (cl:list 'diagnostics
    (cl:cons ':header (header msg))
    (cl:cons ':user_id (user_id msg))
    (cl:cons ':diagnosticstatus (diagnosticstatus msg))
))
