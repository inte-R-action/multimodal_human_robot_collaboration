// Auto-generated. Do not edit!

// (in-package sam_custom_messages.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let diagnostic_msgs = _finder('diagnostic_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class diagnostics {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.user_id = null;
      this.diagnosticstatus = null;
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
      if (initObj.hasOwnProperty('diagnosticstatus')) {
        this.diagnosticstatus = initObj.diagnosticstatus
      }
      else {
        this.diagnosticstatus = new diagnostic_msgs.msg.DiagnosticStatus();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type diagnostics
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [user_id]
    bufferOffset = _serializer.int8(obj.user_id, buffer, bufferOffset);
    // Serialize message field [diagnosticstatus]
    bufferOffset = diagnostic_msgs.msg.DiagnosticStatus.serialize(obj.diagnosticstatus, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type diagnostics
    let len;
    let data = new diagnostics(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [user_id]
    data.user_id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [diagnosticstatus]
    data.diagnosticstatus = diagnostic_msgs.msg.DiagnosticStatus.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += diagnostic_msgs.msg.DiagnosticStatus.getMessageSize(object.diagnosticstatus);
    return length + 1;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/diagnostics';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '166ea485f1a6548735c38b7c8eac661c';
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
    Header header
    #
    ## ID of user (robot or human)
    int8 user_id
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
    diagnostic_msgs/DiagnosticStatus diagnosticstatus
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

    if (msg.diagnosticstatus !== undefined) {
      resolved.diagnosticstatus = diagnostic_msgs.msg.DiagnosticStatus.Resolve(msg.diagnosticstatus)
    }
    else {
      resolved.diagnosticstatus = new diagnostic_msgs.msg.DiagnosticStatus()
    }

    return resolved;
    }
};

module.exports = diagnostics;
