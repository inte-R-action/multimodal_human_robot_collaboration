; Auto-generated. Do not edit!


(cl:in-package sam_custom_messages-msg)


;//! \htmlinclude hand_pos.msg.html

(cl:defclass <hand_pos> (roslisp-msg-protocol:ros-message)
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
   (user_name
    :reader user_name
    :initarg :user_name
    :type cl:string
    :initform "")
   (hand
    :reader hand
    :initarg :hand
    :type cl:fixnum
    :initform 0)
   (pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass hand_pos (<hand_pos>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <hand_pos>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'hand_pos)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sam_custom_messages-msg:<hand_pos> is deprecated: use sam_custom_messages-msg:hand_pos instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <hand_pos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:header-val is deprecated.  Use sam_custom_messages-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'user_id-val :lambda-list '(m))
(cl:defmethod user_id-val ((m <hand_pos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:user_id-val is deprecated.  Use sam_custom_messages-msg:user_id instead.")
  (user_id m))

(cl:ensure-generic-function 'user_name-val :lambda-list '(m))
(cl:defmethod user_name-val ((m <hand_pos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:user_name-val is deprecated.  Use sam_custom_messages-msg:user_name instead.")
  (user_name m))

(cl:ensure-generic-function 'hand-val :lambda-list '(m))
(cl:defmethod hand-val ((m <hand_pos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:hand-val is deprecated.  Use sam_custom_messages-msg:hand instead.")
  (hand m))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <hand_pos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:pose-val is deprecated.  Use sam_custom_messages-msg:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <hand_pos>) ostream)
  "Serializes a message object of type '<hand_pos>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'user_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'user_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'user_name))
  (cl:let* ((signed (cl:slot-value msg 'hand)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <hand_pos>) istream)
  "Deserializes a message object of type '<hand_pos>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'user_id) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'user_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'user_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'hand) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<hand_pos>)))
  "Returns string type for a message object of type '<hand_pos>"
  "sam_custom_messages/hand_pos")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'hand_pos)))
  "Returns string type for a message object of type 'hand_pos"
  "sam_custom_messages/hand_pos")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<hand_pos>)))
  "Returns md5sum for a message object of type '<hand_pos>"
  "1c6006785295f1dfe86ef734b697fe78")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'hand_pos)))
  "Returns md5sum for a message object of type 'hand_pos"
  "1c6006785295f1dfe86ef734b697fe78")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<hand_pos>)))
  "Returns full string definition for message of type '<hand_pos>"
  (cl:format cl:nil "## Message containing location of a users hand~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header header~%#~%## ID of user (robot or human)~%int8 user_id~%#~%## Name of user (robot or human)~%string user_name~%#~%## Which hand location is for, 0:left, 1:right~%int8 hand~%#~%# geometry_msgs/Pose.msg~%# A representation of pose in free space, composed of position and orientation. ~%# Point position~%# Quaternion orientation~%geometry_msgs/Pose pose~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'hand_pos)))
  "Returns full string definition for message of type 'hand_pos"
  (cl:format cl:nil "## Message containing location of a users hand~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header header~%#~%## ID of user (robot or human)~%int8 user_id~%#~%## Name of user (robot or human)~%string user_name~%#~%## Which hand location is for, 0:left, 1:right~%int8 hand~%#~%# geometry_msgs/Pose.msg~%# A representation of pose in free space, composed of position and orientation. ~%# Point position~%# Quaternion orientation~%geometry_msgs/Pose pose~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <hand_pos>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
     4 (cl:length (cl:slot-value msg 'user_name))
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <hand_pos>))
  "Converts a ROS message object to a list"
  (cl:list 'hand_pos
    (cl:cons ':header (header msg))
    (cl:cons ':user_id (user_id msg))
    (cl:cons ':user_name (user_name msg))
    (cl:cons ':hand (hand msg))
    (cl:cons ':pose (pose msg))
))
