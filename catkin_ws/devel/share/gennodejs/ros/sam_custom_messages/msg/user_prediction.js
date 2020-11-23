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

class user_prediction {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.user_id = null;
      this.predictions = null;
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
      if (initObj.hasOwnProperty('predictions')) {
        this.predictions = initObj.predictions
      }
      else {
        this.predictions = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type user_prediction
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [user_id]
    bufferOffset = _serializer.int8(obj.user_id, buffer, bufferOffset);
    // Serialize message field [predictions]
    bufferOffset = _arraySerializer.float64(obj.predictions, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type user_prediction
    let len;
    let data = new user_prediction(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [user_id]
    data.user_id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [predictions]
    data.predictions = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 8 * object.predictions.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/user_prediction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '546e38fb2a5d19f634c167b97894dce3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    ## Message containing predictions of what user capability will be performed next
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
    ## Probabilities of future capabilities being next
    float64[] predictions
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
    const resolved = new user_prediction(null);
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

    if (msg.predictions !== undefined) {
      resolved.predictions = msg.predictions;
    }
    else {
      resolved.predictions = []
    }

    return resolved;
    }
};

module.exports = user_prediction;
