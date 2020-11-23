; Auto-generated. Do not edit!


(cl:in-package sam_custom_messages-msg)


;//! \htmlinclude object_state.msg.html

(cl:defclass <object_state> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (object
    :reader object
    :initarg :object
    :type sam_custom_messages-msg:Object
    :initform (cl:make-instance 'sam_custom_messages-msg:Object))
   (pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass object_state (<object_state>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <object_state>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'object_state)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sam_custom_messages-msg:<object_state> is deprecated: use sam_custom_messages-msg:object_state instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <object_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:header-val is deprecated.  Use sam_custom_messages-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'object-val :lambda-list '(m))
(cl:defmethod object-val ((m <object_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:object-val is deprecated.  Use sam_custom_messages-msg:object instead.")
  (object m))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <object_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sam_custom_messages-msg:pose-val is deprecated.  Use sam_custom_messages-msg:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <object_state>) ostream)
  "Serializes a message object of type '<object_state>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'object) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <object_state>) istream)
  "Deserializes a message object of type '<object_state>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'object) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<object_state>)))
  "Returns string type for a message object of type '<object_state>"
  "sam_custom_messages/object_state")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'object_state)))
  "Returns string type for a message object of type 'object_state"
  "sam_custom_messages/object_state")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<object_state>)))
  "Returns md5sum for a message object of type '<object_state>"
  "2219f508c564a641c1ef4997ea740e7e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'object_state)))
  "Returns md5sum for a message object of type 'object_state"
  "2219f508c564a641c1ef4997ea740e7e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<object_state>)))
  "Returns full string definition for message of type '<object_state>"
  (cl:format cl:nil "## Message containing information on location, type and details about an object in the environment~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header header~%#~%## object.msg~%# Information on object type and further details~%# int8 id~%# int8 type ~%# string[] info~%Object object~%#~%# geometry_msgs/Pose.msg~%# A representation of pose in free space, composed of position and orientation. ~%# Point position~%# Quaternion orientation~%geometry_msgs/Pose pose~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: sam_custom_messages/Object~%# Message containg information on objects within environment~%#~%# Unique ID of object~%int8 id~%#~%# Type of object ID~%int8 type~%#~%# Additional information on object~%string[] info~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'object_state)))
  "Returns full string definition for message of type 'object_state"
  (cl:format cl:nil "## Message containing information on location, type and details about an object in the environment~%#~%## std_msgs/Header.msg~%# sequence ID: consecutively increasing ID ~%# uint32 seq~%# Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%# time stamp~%# Frame this data is associated with~%# string frame_id~%Header header~%#~%## object.msg~%# Information on object type and further details~%# int8 id~%# int8 type ~%# string[] info~%Object object~%#~%# geometry_msgs/Pose.msg~%# A representation of pose in free space, composed of position and orientation. ~%# Point position~%# Quaternion orientation~%geometry_msgs/Pose pose~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: sam_custom_messages/Object~%# Message containg information on objects within environment~%#~%# Unique ID of object~%int8 id~%#~%# Type of object ID~%int8 type~%#~%# Additional information on object~%string[] info~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <object_state>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'object))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <object_state>))
  "Converts a ROS message object to a list"
  (cl:list 'object_state
    (cl:cons ':header (header msg))
    (cl:cons ':object (object msg))
    (cl:cons ':pose (pose msg))
))
