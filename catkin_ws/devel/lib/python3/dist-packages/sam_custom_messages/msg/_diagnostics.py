# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sam_custom_messages/diagnostics.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import diagnostic_msgs.msg
import std_msgs.msg

class diagnostics(genpy.Message):
  _md5sum = "d697c2568ce7a485465d81f6f70b8306"
  _type = "sam_custom_messages/diagnostics"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """## Message containing diagnostic information for sensors/devices/users within the system
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
"""
  __slots__ = ['Header','UserId','UserName','DiagnosticStatus']
  _slot_types = ['std_msgs/Header','int8','string','diagnostic_msgs/DiagnosticStatus']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Header,UserId,UserName,DiagnosticStatus

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(diagnostics, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Header is None:
        self.Header = std_msgs.msg.Header()
      if self.UserId is None:
        self.UserId = 0
      if self.UserName is None:
        self.UserName = ''
      if self.DiagnosticStatus is None:
        self.DiagnosticStatus = diagnostic_msgs.msg.DiagnosticStatus()
    else:
      self.Header = std_msgs.msg.Header()
      self.UserId = 0
      self.UserName = ''
      self.DiagnosticStatus = diagnostic_msgs.msg.DiagnosticStatus()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.Header.seq, _x.Header.stamp.secs, _x.Header.stamp.nsecs))
      _x = self.Header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.UserId
      buff.write(_get_struct_b().pack(_x))
      _x = self.UserName
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.DiagnosticStatus.level
      buff.write(_get_struct_b().pack(_x))
      _x = self.DiagnosticStatus.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.DiagnosticStatus.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.DiagnosticStatus.hardware_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.DiagnosticStatus.values)
      buff.write(_struct_I.pack(length))
      for val1 in self.DiagnosticStatus.values:
        _x = val1.key
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.value
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.Header is None:
        self.Header = std_msgs.msg.Header()
      if self.DiagnosticStatus is None:
        self.DiagnosticStatus = diagnostic_msgs.msg.DiagnosticStatus()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.Header.seq, _x.Header.stamp.secs, _x.Header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Header.frame_id = str[start:end]
      start = end
      end += 1
      (self.UserId,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.UserName = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.UserName = str[start:end]
      start = end
      end += 1
      (self.DiagnosticStatus.level,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.DiagnosticStatus.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.DiagnosticStatus.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.DiagnosticStatus.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.DiagnosticStatus.message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.DiagnosticStatus.hardware_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.DiagnosticStatus.hardware_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.DiagnosticStatus.values = []
      for i in range(0, length):
        val1 = diagnostic_msgs.msg.KeyValue()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.key = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.value = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.value = str[start:end]
        self.DiagnosticStatus.values.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.Header.seq, _x.Header.stamp.secs, _x.Header.stamp.nsecs))
      _x = self.Header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.UserId
      buff.write(_get_struct_b().pack(_x))
      _x = self.UserName
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.DiagnosticStatus.level
      buff.write(_get_struct_b().pack(_x))
      _x = self.DiagnosticStatus.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.DiagnosticStatus.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.DiagnosticStatus.hardware_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.DiagnosticStatus.values)
      buff.write(_struct_I.pack(length))
      for val1 in self.DiagnosticStatus.values:
        _x = val1.key
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.value
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.Header is None:
        self.Header = std_msgs.msg.Header()
      if self.DiagnosticStatus is None:
        self.DiagnosticStatus = diagnostic_msgs.msg.DiagnosticStatus()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.Header.seq, _x.Header.stamp.secs, _x.Header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Header.frame_id = str[start:end]
      start = end
      end += 1
      (self.UserId,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.UserName = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.UserName = str[start:end]
      start = end
      end += 1
      (self.DiagnosticStatus.level,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.DiagnosticStatus.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.DiagnosticStatus.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.DiagnosticStatus.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.DiagnosticStatus.message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.DiagnosticStatus.hardware_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.DiagnosticStatus.hardware_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.DiagnosticStatus.values = []
      for i in range(0, length):
        val1 = diagnostic_msgs.msg.KeyValue()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.key = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.value = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.value = str[start:end]
        self.DiagnosticStatus.values.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
