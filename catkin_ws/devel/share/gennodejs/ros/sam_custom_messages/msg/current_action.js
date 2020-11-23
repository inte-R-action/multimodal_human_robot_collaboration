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
      this.header = null;
      this.user_id = null;
      this.action_probs = null;
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
      if (initObj.hasOwnProperty('action_probs')) {
        this.action_probs = initObj.action_probs
      }
      else {
        this.action_probs = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type current_action
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [user_id]
    bufferOffset = _serializer.int8(obj.user_id, buffer, bufferOffset);
    // Serialize message field [action_probs]
    bufferOffset = _arraySerializer.float64(obj.action_probs, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type current_action
    let len;
    let data = new current_action(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [user_id]
    data.user_id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [action_probs]
    data.action_probs = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 8 * object.action_probs.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/current_action';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '799d6ed84a84e9c791e69aeaf9e13c8a';
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
    Header header
    #
    ## ID of user (robot or human)
    int8 user_id
    #
    ## Probabilities of curent actions
    float64[] action_probs
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

    if (msg.action_probs !== undefined) {
      resolved.action_probs = msg.action_probs;
    }
    else {
      resolved.action_probs = []
    }

    return resolved;
    }
};

module.exports = current_action;
