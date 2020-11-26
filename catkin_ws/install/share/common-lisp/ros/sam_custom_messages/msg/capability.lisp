; Auto-generated. Do not edit!


(cl:in-package sam_custom_messages-msg)


;//! \htmlinclude capability.msg.html

(cl:defclass <capability> (roslisp-msg-protocol:ros-message)
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
   (Object
    :reader Object
    :initarg :Object
    :type sam_custom_messages-msg:Object
    :initform (cl:make-instance 'sam_custom_messages-msg:Object))
   (Pose
    :reader Pose
    :initarg :Pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (Type
    :reader Type
    :initarg :Type
    :type cl:fixnum
    :initform 0)
   (Info
    :reader Info
    :initarg :Info
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass capability (<capability>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <capability>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'capability)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sam_custom_messages-msg:<capability> is deprecated: use sam_custom_messages-msg:capability instead.")))

(cl:ensure-generic-function 'Header-val :lambda-list '(m))
(cl:defmethod Header-val ((m <capability>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:Header-val is deprecated.  Use sam_custom_messages-msg:Header instead.")
  (Header m))

(cl:ensure-generic-function 'UserId-val :lambda-list '(m))
(cl:defmethod UserId-val ((m <capability>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:UserId-val is deprecated.  Use sam_custom_messages-msg:UserId instead.")
  (UserId m))

(cl:ensure-generic-function 'Object-val :lambda-list '(m))
(cl:defmethod Object-val ((m <capability>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:Object-val is deprecated.  Use sam_custom_messages-msg:Object instead.")
  (Object m))

(cl:ensure-generic-function 'Pose-val :lambda-list '(m))
(cl:defmethod Pose-val ((m <capability>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:Pose-val is deprecated.  Use sam_custom_messages-msg:Pose instead.")
  (Pose m))

(cl:ensure-generic-function 'Type-val :lambda-list '(m))
(cl:defmethod Type-val ((m <capability>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:Type-val is deprecated.  Use sam_custom_messages-msg:Type instead.")
  (Type m))

(cl:ensure-generic-function 'Info-val :lambda-list '(m))
(cl:defmethod Info-val ((m <capability>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:Info-val is deprecated.  Use sam_custom_messages-msg:Info instead.")
  (Info m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <capability>) ostream)
  "Serializes a message object of type '<capability>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'UserId)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Object) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'Pose) ostream)
  (cl:let* ((signed (cl:slot-value msg 'Type)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'Info))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'Info))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <capability>) istream)
  "Deserializes a message object of type '<capability>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'UserId) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Object) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'Pose) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'Type) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'Info) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'Info)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<capability>)))
  "Returns string type for a message object of type '<capability>"
  "sam_custom_messages/capability")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'capability)))
  "Returns string type for a message object of type 'capability"
  "sam_custom_messages/capability")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<capability>)))
  "Returns md5sum for a message object of type '<capability>"
  "0d980a9edeb2165abe1fcce834dfe67e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'capability)))
  "Returns md5sum for a message object of type 'capability"
  "0d980a9edeb2165abe1fcce834dfe67e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<capability>)))
  "Returns full string definition for message of type '<capability>"
  (cl:format cl:nil "## Message containing information on what capability user (robot or human) currently performing~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header Header~%#~%## ID of user (robot or human)~%int8 UserId~%#~%## object.msg~%# Information on object type and further details~%# int8 id~%# int8 type ~%# string[] info~%Object Object~%#~%# geometry_msgs/Pose.msg~%# A representation of pose in free space, composed of position and orientation. ~%# Point position~%# Quaternion orientation~%geometry_msgs/Pose Pose~%#~%# ID of capability type~%int8 Type~%#~%# Details on capability being performed~%string[] Info~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: sam_custom_messages/Object~%# Message containg information on objects within environment~%#~%# Unique ID of object~%int8 Id~%#~%# Type of object ID~%int8 Type~%#~%# Additional information on object~%string[] Info~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'capability)))
  "Returns full string definition for message of type 'capability"
  (cl:format cl:nil "## Message containing information on what capability user (robot or human) currently performing~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header Header~%#~%## ID of user (robot or human)~%int8 UserId~%#~%## object.msg~%# Information on object type and further details~%# int8 id~%# int8 type ~%# string[] info~%Object Object~%#~%# geometry_msgs/Pose.msg~%# A representation of pose in free space, composed of position and orientation. ~%# Point position~%# Quaternion orientation~%geometry_msgs/Pose Pose~%#~%# ID of capability type~%int8 Type~%#~%# Details on capability being performed~%string[] Info~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: sam_custom_messages/Object~%# Message containg information on objects within environment~%#~%# Unique ID of object~%int8 Id~%#~%# Type of object ID~%int8 Type~%#~%# Additional information on object~%string[] Info~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <capability>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Header))
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Object))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'Pose))
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'Info) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <capability>))
  "Converts a ROS message object to a list"
  (cl:list 'capability
    (cl:cons ':Header (Header msg))
    (cl:cons ':UserId (UserId msg))
    (cl:cons ':Object (Object msg))
    (cl:cons ':Pose (Pose msg))
    (cl:cons ':Type (Type msg))
    (cl:cons ':Info (Info msg))
))
