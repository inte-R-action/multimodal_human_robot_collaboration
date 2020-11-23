; Auto-generated. Do not edit!


(cl:in-package sam_custom_messages-msg)


;//! \htmlinclude current_action.msg.html

(cl:defclass <current_action> (roslisp-msg-protocol:ros-message)
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
   (action_probs
    :reader action_probs
    :initarg :action_probs
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass current_action (<current_action>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <current_action>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'current_action)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sam_custom_messages-msg:<current_action> is deprecated: use sam_custom_messages-msg:current_action instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <current_action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:header-val is deprecated.  Use sam_custom_messages-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'user_id-val :lambda-list '(m))
(cl:defmethod user_id-val ((m <current_action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:user_id-val is deprecated.  Use sam_custom_messages-msg:user_id instead.")
  (user_id m))

(cl:ensure-generic-function 'action_probs-val :lambda-list '(m))
(cl:defmethod action_probs-val ((m <current_action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:action_probs-val is deprecated.  Use sam_custom_messages-msg:action_probs instead.")
  (action_probs m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <current_action>) ostream)
  "Serializes a message object of type '<current_action>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'user_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'action_probs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'action_probs))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <current_action>) istream)
  "Deserializes a message object of type '<current_action>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'user_id) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'action_probs) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'action_probs)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<current_action>)))
  "Returns string type for a message object of type '<current_action>"
  "sam_custom_messages/current_action")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'current_action)))
  "Returns string type for a message object of type 'current_action"
  "sam_custom_messages/current_action")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<current_action>)))
  "Returns md5sum for a message object of type '<current_action>"
  "799d6ed84a84e9c791e69aeaf9e13c8a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'current_action)))
  "Returns md5sum for a message object of type 'current_action"
  "799d6ed84a84e9c791e69aeaf9e13c8a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<current_action>)))
  "Returns full string definition for message of type '<current_action>"
  (cl:format cl:nil "## Message containing predictions of what action user is currently performing~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header header~%#~%## ID of user (robot or human)~%int8 user_id~%#~%## Probabilities of curent actions~%float64[] action_probs~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'current_action)))
  "Returns full string definition for message of type 'current_action"
  (cl:format cl:nil "## Message containing predictions of what action user is currently performing~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header header~%#~%## ID of user (robot or human)~%int8 user_id~%#~%## Probabilities of curent actions~%float64[] action_probs~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <current_action>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'action_probs) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <current_action>))
  "Converts a ROS message object to a list"
  (cl:list 'current_action
    (cl:cons ':header (header msg))
    (cl:cons ':user_id (user_id msg))
    (cl:cons ':action_probs (action_probs msg))
))
