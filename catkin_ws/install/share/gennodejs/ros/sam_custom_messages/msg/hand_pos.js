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
      this.Header = null;
      this.UserId = null;
      this.UserName = null;
      this.Hand = null;
      this.Pose = null;
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
      if (initObj.hasOwnProperty('UserName')) {
        this.UserName = initObj.UserName
      }
      else {
        this.UserName = '';
      }
      if (initObj.hasOwnProperty('Hand')) {
        this.Hand = initObj.Hand
      }
      else {
        this.Hand = 0;
      }
      if (initObj.hasOwnProperty('Pose')) {
        this.Pose = initObj.Pose
      }
      else {
        this.Pose = new geometry_msgs.msg.Pose();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type hand_pos
    // Serialize message field [Header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.Header, buffer, bufferOffset);
    // Serialize message field [UserId]
    bufferOffset = _serializer.int8(obj.UserId, buffer, bufferOffset);
    // Serialize message field [UserName]
    bufferOffset = _serializer.string(obj.UserName, buffer, bufferOffset);
    // Serialize message field [Hand]
    bufferOffset = _serializer.int8(obj.Hand, buffer, bufferOffset);
    // Serialize message field [Pose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.Pose, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type hand_pos
    let len;
    let data = new hand_pos(null);
    // Deserialize message field [Header]
    data.Header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [UserId]
    data.UserId = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [UserName]
    data.UserName = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [Hand]
    data.Hand = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [Pose]
    data.Pose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.Header);
    length += object.UserName.length;
    return length + 62;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/hand_pos';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c3a4ac1d92f14f60ae68b389fe0ff85a';
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
    Header Header
    #
    ## ID of user (robot or human)
    int8 UserId
    #
    ## Name of user (robot or human)
    string UserName
    #
    ## Which hand location is for, 0:left, 1:right
    int8 Hand
    #
    # geometry_msgs/Pose.msg
    # A representation of pose in free space, composed of position and orientation. 
    # Point position
    # Quaternion orientation
    geometry_msgs/Pose Pose
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

    if (msg.UserName !== undefined) {
      resolved.UserName = msg.UserName;
    }
    else {
      resolved.UserName = ''
    }

    if (msg.Hand !== undefined) {
      resolved.Hand = msg.Hand;
    }
    else {
      resolved.Hand = 0
    }

    if (msg.Pose !== undefined) {
      resolved.Pose = geometry_msgs.msg.Pose.Resolve(msg.Pose)
    }
    else {
      resolved.Pose = new geometry_msgs.msg.Pose()
    }

    return resolved;
    }
};

module.exports = hand_pos;
