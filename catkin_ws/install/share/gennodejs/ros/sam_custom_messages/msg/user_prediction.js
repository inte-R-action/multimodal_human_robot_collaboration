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
      this.Header = null;
      this.UserId = null;
      this.Predictions = null;
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
      if (initObj.hasOwnProperty('Predictions')) {
        this.Predictions = initObj.Predictions
      }
      else {
        this.Predictions = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type user_prediction
    // Serialize message field [Header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.Header, buffer, bufferOffset);
    // Serialize message field [UserId]
    bufferOffset = _serializer.int8(obj.UserId, buffer, bufferOffset);
    // Serialize message field [Predictions]
    bufferOffset = _arraySerializer.float64(obj.Predictions, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type user_prediction
    let len;
    let data = new user_prediction(null);
    // Deserialize message field [Header]
    data.Header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [UserId]
    data.UserId = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [Predictions]
    data.Predictions = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.Header);
    length += 8 * object.Predictions.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/user_prediction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a0a99151d0431e7e25d8e440508ac456';
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
    Header Header
    #
    ## ID of user (robot or human)
    int8 UserId
    #
    ## Probabilities of future capabilities being next
    float64[] Predictions
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

    if (msg.Predictions !== undefined) {
      resolved.Predictions = msg.Predictions;
    }
    else {
      resolved.Predictions = []
    }

    return resolved;
    }
};

module.exports = user_prediction;
