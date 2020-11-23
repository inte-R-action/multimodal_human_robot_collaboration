// Auto-generated. Do not edit!

// (in-package sam_custom_messages.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Object {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
      this.type = null;
      this.info = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('type')) {
        this.type = initObj.type
      }
      else {
        this.type = 0;
      }
      if (initObj.hasOwnProperty('info')) {
        this.info = initObj.info
      }
      else {
        this.info = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Object
    // Serialize message field [id]
    bufferOffset = _serializer.int8(obj.id, buffer, bufferOffset);
    // Serialize message field [type]
    bufferOffset = _serializer.int8(obj.type, buffer, bufferOffset);
    // Serialize message field [info]
    bufferOffset = _arraySerializer.string(obj.info, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Object
    let len;
    let data = new Object(null);
    // Deserialize message field [id]
    data.id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [type]
    data.type = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [info]
    data.info = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.info.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 6;
  }

  static datatype() {
    // Returns string type for a message object
    return 'sam_custom_messages/Object';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cc95ebc586991f7be21fb0175298a82c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Message containg information on objects within environment
    #
    # Unique ID of object
    int8 id
    #
    # Type of object ID
    int8 type
    #
    # Additional information on object
    string[] info
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Object(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.type !== undefined) {
      resolved.type = msg.type;
    }
    else {
      resolved.type = 0
    }

    if (msg.info !== undefined) {
      resolved.info = msg.info;
    }
    else {
      resolved.info = []
    }

    return resolved;
    }
};

module.exports = Object;
