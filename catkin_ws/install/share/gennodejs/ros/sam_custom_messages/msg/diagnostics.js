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
let diagnostic_msgs = _finder('diagnostic_msgs');

//-----------------------------------------------------------

class diagnostics {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Header = null;
      this.UserId = null;
      this.UserName = null;
      this.DiagnosticStatus = null;
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
      if (initObj.hasOwnProperty('DiagnosticStatus')) {
        this.DiagnosticStatus = initObj.DiagnosticStatus
      }
      else {
        this.DiagnosticStatus = new diagnostic_msgs.msg.DiagnosticStatus();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type diagnostics
    // Serialize message field [Header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.Header, buffer, bufferOffset);
    // Serialize message field [UserId]
    bufferOffset = _serializer.int8(obj.UserId, buffer, bufferOffset);
    // Serialize message field [UserName]
    bufferOffset = _serializer.string(obj.UserName, buffer, bufferOffset);
    // Serialize message field [DiagnosticStatus]
    bufferOffset = diagnostic_msgs.msg.DiagnosticStatus.serialize(obj.DiagnosticStatus, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type diagnostics
    let len;
    let data = new diagnostics(null);
    // Deserialize message field [Header]
    data.Header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [UserId]
    data.UserId = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [UserName]
    data.UserName = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [DiagnosticStatus]
    data.DiagnosticStatus = diagnostic_msgs.msg.DiagnosticStatus.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.Header);
    length += object.UserName.length;
    length += diagnostic_msgs.msg.DiagnosticStatus.getMessageSize(object.DiagnosticStatus);
    return length + 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/diagnostics';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd697c2568ce7a485465d81f6f70b8306';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    ## Message containing diagnostic information for sensors/devices/users within the system
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
    ## diagnostic_msgs/DiagnosticStatus.msg
    # Possible levels of operations
    # byte OK=0
    # byte WARN=1
    # byte ERROR=2
    # byte STALE=3
    # byte level # level of operation enumerated above 
    # string name # a description of the test/component reporting
    # string message # a description of the status
    # string hardware_id # a hardware unique string
    # KeyValue[] values # an array of values associated with the status
    diagnostic_msgs/DiagnosticStatus DiagnosticStatus
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
    MSG: diagnostic_msgs/DiagnosticStatus
    # This message holds the status of an individual component of the robot.
    # 
    
    # Possible levels of operations
    byte OK=0
    byte WARN=1
    byte ERROR=2
    byte STALE=3
    
    byte level # level of operation enumerated above 
    string name # a description of the test/component reporting
    string message # a description of the status
    string hardware_id # a hardware unique string
    KeyValue[] values # an array of values associated with the status
    
    
    ================================================================================
    MSG: diagnostic_msgs/KeyValue
    string key # what to label this value when viewing
    string value # a value to track over time
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new diagnostics(null);
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

    if (msg.DiagnosticStatus !== undefined) {
      resolved.DiagnosticStatus = diagnostic_msgs.msg.DiagnosticStatus.Resolve(msg.DiagnosticStatus)
    }
    else {
      resolved.DiagnosticStatus = new diagnostic_msgs.msg.DiagnosticStatus()
    }

    return resolved;
    }
};

module.exports = diagnostics;
