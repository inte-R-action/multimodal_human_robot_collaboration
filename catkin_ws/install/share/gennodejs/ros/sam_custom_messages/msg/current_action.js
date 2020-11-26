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

//-----------------------------------------------------------

class current_action {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Header = null;
      this.UserId = null;
      this.UserName = null;
      this.ActionProbs = null;
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
      if (initObj.hasOwnProperty('ActionProbs')) {
        this.ActionProbs = initObj.ActionProbs
      }
      else {
        this.ActionProbs = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type current_action
    // Serialize message field [Header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.Header, buffer, bufferOffset);
    // Serialize message field [UserId]
    bufferOffset = _serializer.int8(obj.UserId, buffer, bufferOffset);
    // Serialize message field [UserName]
    bufferOffset = _serializer.string(obj.UserName, buffer, bufferOffset);
    // Serialize message field [ActionProbs]
    bufferOffset = _arraySerializer.float64(obj.ActionProbs, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type current_action
    let len;
    let data = new current_action(null);
    // Deserialize message field [Header]
    data.Header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [UserId]
    data.UserId = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [UserName]
    data.UserName = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [ActionProbs]
    data.ActionProbs = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.Header);
    length += object.UserName.length;
    length += 8 * object.ActionProbs.length;
    return length + 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/current_action';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5a22afcb1583334c436419d2dee34df6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    ## Message containing predictions of what action user is currently performing
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
    ## Probabilities of curent actions
    float64[] ActionProbs
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new current_action(null);
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

    if (msg.ActionProbs !== undefined) {
      resolved.ActionProbs = msg.ActionProbs;
    }
    else {
      resolved.ActionProbs = []
    }

    return resolved;
    }
};

module.exports = current_action;
