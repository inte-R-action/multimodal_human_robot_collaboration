// Auto-generated. Do not edit!

// (in-package sam_custom_messages.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class hand_pos {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.user_id = null;
      this.user_name = null;
      this.hand = null;
      this.pose = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('user_id')) {
        this.user_id = initObj.user_id
      }
      else {
        this.user_id = 0;
      }
      if (initObj.hasOwnProperty('user_name')) {
        this.user_name = initObj.user_name
      }
      else {
        this.user_name = '';
      }
      if (initObj.hasOwnProperty('hand')) {
        this.hand = initObj.hand
      }
      else {
        this.hand = 0;
      }
      if (initObj.hasOwnProperty('pose')) {
        this.pose = initObj.pose
      }
      else {
        this.pose = new geometry_msgs.msg.Pose();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type hand_pos
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [user_id]
    bufferOffset = _serializer.int8(obj.user_id, buffer, bufferOffset);
    // Serialize message field [user_name]
    bufferOffset = _serializer.string(obj.user_name, buffer, bufferOffset);
    // Serialize message field [hand]
    bufferOffset = _serializer.int8(obj.hand, buffer, bufferOffset);
    // Serialize message field [pose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.pose, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type hand_pos
    let len;
    let data = new hand_pos(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [user_id]
    data.user_id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [user_name]
    data.user_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [hand]
    data.hand = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [pose]
    data.pose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += object.user_name.length;
    return length + 62;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/hand_pos';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1c6006785295f1dfe86ef734b697fe78';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    ## Message containing location of a users hand
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
    ## Name of user (robot or human)
    string user_name
    #
    ## Which hand location is for, 0:left, 1:right
    int8 hand
    #
    # geometry_msgs/Pose.msg
    # A representation of pose in free space, composed of position and orientation. 
    # Point position
    # Quaternion orientation
    geometry_msgs/Pose pose
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
    const resolved = new hand_pos(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.user_id !== undefined) {
      resolved.user_id = msg.user_id;
    }
    else {
      resolved.user_id = 0
    }

    if (msg.user_name !== undefined) {
      resolved.user_name = msg.user_name;
    }
    else {
      resolved.user_name = ''
    }

    if (msg.hand !== undefined) {
      resolved.hand = msg.hand;
    }
    else {
      resolved.hand = 0
    }

    if (msg.pose !== undefined) {
      resolved.pose = geometry_msgs.msg.Pose.Resolve(msg.pose)
    }
    else {
      resolved.pose = new geometry_msgs.msg.Pose()
    }

    return resolved;
    }
};

module.exports = hand_pos;
