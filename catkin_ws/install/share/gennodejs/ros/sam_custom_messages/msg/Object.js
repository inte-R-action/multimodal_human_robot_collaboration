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
      this.Id = null;
      this.Type = null;
      this.Info = null;
    }
    else {
      if (initObj.hasOwnProperty('Id')) {
        this.Id = initObj.Id
      }
      else {
        this.Id = 0;
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
    // Serializes a message object of type Object
    // Serialize message field [Id]
    bufferOffset = _serializer.int8(obj.Id, buffer, bufferOffset);
    // Serialize message field [Type]
    bufferOffset = _serializer.int8(obj.Type, buffer, bufferOffset);
    // Serialize message field [Info]
    bufferOffset = _arraySerializer.string(obj.Info, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Object
    let len;
    let data = new Object(null);
    // Deserialize message field [Id]
    data.Id = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [Type]
    data.Type = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [Info]
    data.Info = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.Info.forEach((val) => {
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
    return '08793d2cad4a594af24da817df20da39';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Object(null);
    if (msg.Id !== undefined) {
      resolved.Id = msg.Id;
    }
    else {
      resolved.Id = 0
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

module.exports = Object;
