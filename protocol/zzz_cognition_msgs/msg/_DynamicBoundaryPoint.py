# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from zzz_cognition_msgs/DynamicBoundaryPoint.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class DynamicBoundaryPoint(genpy.Message):
  _md5sum = "4d60f51b54e63f480fa675cabac5f594"
  _type = "zzz_cognition_msgs/DynamicBoundaryPoint"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This message represents a point in the dynamic boundary

float32 x
float32 y
float32 vx
float32 vy
float32 omega
uint8 flag"""
  __slots__ = ['x','y','vx','vy','omega','flag']
  _slot_types = ['float32','float32','float32','float32','float32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x,y,vx,vy,omega,flag

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DynamicBoundaryPoint, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.vx is None:
        self.vx = 0.
      if self.vy is None:
        self.vy = 0.
      if self.omega is None:
        self.omega = 0.
      if self.flag is None:
        self.flag = 0
    else:
      self.x = 0.
      self.y = 0.
      self.vx = 0.
      self.vy = 0.
      self.omega = 0.
      self.flag = 0

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
      buff.write(_get_struct_5fB().pack(_x.x, _x.y, _x.vx, _x.vy, _x.omega, _x.flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 21
      (_x.x, _x.y, _x.vx, _x.vy, _x.omega, _x.flag,) = _get_struct_5fB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_5fB().pack(_x.x, _x.y, _x.vx, _x.vy, _x.omega, _x.flag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 21
      (_x.x, _x.y, _x.vx, _x.vy, _x.omega, _x.flag,) = _get_struct_5fB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_5fB = None
def _get_struct_5fB():
    global _struct_5fB
    if _struct_5fB is None:
        _struct_5fB = struct.Struct("<5fB")
    return _struct_5fB
