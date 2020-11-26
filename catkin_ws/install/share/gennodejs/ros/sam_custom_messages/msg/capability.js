// Auto-generated. Do not edit!

// (in-package sam_custom_messages.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Object = require('./Object.js');
let geometry_msgs = _finder('geometry_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class capability {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Header = null;
      this.UserId = null;
      this.Object = null;
      this.Pose = null;
      this.Type = null;
      this.Info = null;
    }
    else {
      if (initObj.hasOwnProperty('Header')) {
        this.Header = initObj.Header
      }
      else {
        this.Header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('UserId')) {
        this.UserId = initObj.UserId
      }
      else {
        this.UserId = 0;
      }
      if (initObj.hasOwnProperty('Object')) {
        this.Object = initObj.Object
      }
      else {
        this.Object = new Object();
      }
      if (initObj.hasOwnProperty('Pose')) {
        this.Pose = initObj.Pose
      }
      else {
        this.Pose = new geometry_msgs.msg.Pose();
      }
      if (initObj.hasOwnProperty('Type')) {
        this.Type = initObj.Type
      }
      else {
        this.Type = 0;
      }
      if (initObj.hasOwnProperty('Info')) {
        this.Info = initObj.Info
      }
      else {
        this.Info = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type capability
    // Serialize message field [Header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.Header, buffer, bufferOffset);
    // Serialize message field [UserId]
    bufferOffset = _serializer.int8(obj.UserId, buffer, bufferOffset);
    // Serialize message field [Object]
    bufferOffset = Object.serialize(obj.Object, buffer, bufferOffset);
    // Serialize message field [Pose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.Pose, buffer, bufferOffset);
    // Serialize message field [Type]
    bufferOffset = _serializer.int8(obj.Type, buffer, bufferOffset);
    // Serialize message field [Info]
    bufferOffset = _arraySerializer.string(obj.Info, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type capability
    let len;
    let data = new capability(null);
    // Deserialize message field [Header]
    data.Header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [UserId]
    data.UserId = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [Object]
    data.Object = Object.deserialize(buffer, bufferOffset);
    // Deserialize message field [Pose]
    data.Pose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    // Deserialize message field [Type]
    data.Type = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [Info]
    data.Info = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.Header);
    length += Object.getMessageSize(object.Object);
    object.Info.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 62;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/capability';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0d980a9edeb2165abe1fcce834dfe67e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    ## Message containing information on what capability user (robot or human) currently performing
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
    ## object.msg
    # Information on object type and further details
    # int8 id
    # int8 type 
    # string[] info
    Object Object
    #
    # geometry_msgs/Pose.msg
    # A representation of pose in free space, composed of position and orientation. 
    # Point position
    # Quaternion orientation
    geometry_msgs/Pose Pose
    #
    # ID of capability type
    int8 Type
    #
    # Details on capability being performed
    string[] Info
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
    MSG: sam_custom_messages/Object
    # Message containg information on objects within environment
    #
    # Unique ID of object
    int8 Id
    #
    # Type of object ID
    int8 Type
    #
    # Additional information on object
    string[] Info
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new capability(null);
    if (msg.Header !== undefined) {
      resolved.Header = std_msgs.msg.Header.Resolve(msg.Header)
    }
    else {
      resolved.Header = new std_msgs.msg.Header()
    }

    if (msg.UserId !== undefined) {
      resolved.UserId = msg.UserId;
    }
    else {
      resolved.UserId = 0
    }

    if (msg.Object !== undefined) {
      resolved.Object = Object.Resolve(msg.Object)
    }
    else {
      resolved.Object = new Object()
    }

    if (msg.Pose !== undefined) {
      resolved.Pose = geometry_msgs.msg.Pose.Resolve(msg.Pose)
    }
    else {
      resolved.Pose = new geometry_msgs.msg.Pose()
    }

    if (msg.Type !== undefined) {
      resolved.Type = msg.Type;
    }
    else {
      resolved.Type = 0
    }

    if (msg.Info !== undefined) {
      resolved.Info = msg.Info;
    }
    else {
      resolved.Info = []
    }

    return resolved;
    }
};

module.exports = capability;
