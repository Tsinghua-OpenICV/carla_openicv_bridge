# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from visualization_msgs/ImageMarker.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import genpy
import protocol.std_msgs.msg as std_msgs

class ImageMarker(genpy.Message):
  _md5sum = "1de93c67ec8858b831025a08fbf1b35c"
  _type = "visualization_msgs/ImageMarker"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """uint8 CIRCLE=0
uint8 LINE_STRIP=1
uint8 LINE_LIST=2
uint8 POLYGON=3
uint8 POINTS=4

uint8 ADD=0
uint8 REMOVE=1

Header header
string ns		# namespace, used with id to form a unique id
int32 id          	# unique id within the namespace
int32 type        	# CIRCLE/LINE_STRIP/etc.
int32 action      	# ADD/REMOVE
geometry_msgs/Point position # 2D, in pixel-coords
float32 scale	 	# the diameter for a circle, etc.
std_msgs/ColorRGBA outline_color
uint8 filled		# whether to fill in the shape with color
std_msgs/ColorRGBA fill_color # color [0.0-1.0]
duration lifetime       # How long the object should last before being automatically deleted.  0 means forever


geometry_msgs/Point[] points # used for LINE_STRIP/LINE_LIST/POINTS/etc., 2D in pixel coords
std_msgs/ColorRGBA[] outline_colors # a color for each line, point, etc.
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
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a
"""
  # Pseudo-constants
  CIRCLE = 0
  LINE_STRIP = 1
  LINE_LIST = 2
  POLYGON = 3
  POINTS = 4
  ADD = 0
  REMOVE = 1

  __slots__ = ['header','ns','id','type','action','position','scale','outline_color','filled','fill_color','lifetime','points','outline_colors']
  _slot_types = ['std_msgs/Header','string','int32','int32','int32','geometry_msgs/Point','float32','std_msgs/ColorRGBA','uint8','std_msgs/ColorRGBA','duration','geometry_msgs/Point[]','std_msgs/ColorRGBA[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,ns,id,type,action,position,scale,outline_color,filled,fill_color,lifetime,points,outline_colors

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ImageMarker, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.Header()
      if self.ns is None:
        self.ns = ''
      if self.id is None:
        self.id = 0
      if self.type is None:
        self.type = 0
      if self.action is None:
        self.action = 0
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.scale is None:
        self.scale = 0.
      if self.outline_color is None:
        self.outline_color = std_msgs.ColorRGBA()
      if self.filled is None:
        self.filled = 0
      if self.fill_color is None:
        self.fill_color = std_msgs.ColorRGBA()
      if self.lifetime is None:
        self.lifetime = genpy.Duration()
      if self.points is None:
        self.points = []
      if self.outline_colors is None:
        self.outline_colors = []
    else:
      self.header = std_msgs.Header()
      self.ns = ''
      self.id = 0
      self.type = 0
      self.action = 0
      self.position = geometry_msgs.msg.Point()
      self.scale = 0.
      self.outline_color = std_msgs.ColorRGBA()
      self.filled = 0
      self.fill_color = std_msgs.ColorRGBA()
      self.lifetime = genpy.Duration()
      self.points = []
      self.outline_colors = []

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.ns
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3i3d5fB4f2i().pack(_x.id, _x.type, _x.action, _x.position.x, _x.position.y, _x.position.z, _x.scale, _x.outline_color.r, _x.outline_color.g, _x.outline_color.b, _x.outline_color.a, _x.filled, _x.fill_color.r, _x.fill_color.g, _x.fill_color.b, _x.fill_color.a, _x.lifetime.secs, _x.lifetime.nsecs))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.outline_colors)
      buff.write(_struct_I.pack(length))
      for val1 in self.outline_colors:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.Header()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.outline_color is None:
        self.outline_color = std_msgs.ColorRGBA()
      if self.fill_color is None:
        self.fill_color = std_msgs.ColorRGBA()
      if self.lifetime is None:
        self.lifetime = genpy.Duration()
      if self.points is None:
        self.points = None
      if self.outline_colors is None:
        self.outline_colors = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ns = str[start:end].decode('utf-8')
      else:
        self.ns = str[start:end]
      _x = self
      start = end
      end += 81
      (_x.id, _x.type, _x.action, _x.position.x, _x.position.y, _x.position.z, _x.scale, _x.outline_color.r, _x.outline_color.g, _x.outline_color.b, _x.outline_color.a, _x.filled, _x.fill_color.r, _x.fill_color.g, _x.fill_color.b, _x.fill_color.a, _x.lifetime.secs, _x.lifetime.nsecs,) = _get_struct_3i3d5fB4f2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.outline_colors = []
      for i in range(0, length):
        val1 = std_msgs.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.outline_colors.append(val1)
      self.lifetime.canon()
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.ns
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3i3d5fB4f2i().pack(_x.id, _x.type, _x.action, _x.position.x, _x.position.y, _x.position.z, _x.scale, _x.outline_color.r, _x.outline_color.g, _x.outline_color.b, _x.outline_color.a, _x.filled, _x.fill_color.r, _x.fill_color.g, _x.fill_color.b, _x.fill_color.a, _x.lifetime.secs, _x.lifetime.nsecs))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.outline_colors)
      buff.write(_struct_I.pack(length))
      for val1 in self.outline_colors:
        _x = val1
        buff.write(_get_struct_4f().pack(_x.r, _x.g, _x.b, _x.a))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.Header()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.outline_color is None:
        self.outline_color = std_msgs.ColorRGBA()
      if self.fill_color is None:
        self.fill_color = std_msgs.ColorRGBA()
      if self.lifetime is None:
        self.lifetime = genpy.Duration()
      if self.points is None:
        self.points = None
      if self.outline_colors is None:
        self.outline_colors = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ns = str[start:end].decode('utf-8')
      else:
        self.ns = str[start:end]
      _x = self
      start = end
      end += 81
      (_x.id, _x.type, _x.action, _x.position.x, _x.position.y, _x.position.z, _x.scale, _x.outline_color.r, _x.outline_color.g, _x.outline_color.b, _x.outline_color.a, _x.filled, _x.fill_color.r, _x.fill_color.g, _x.fill_color.b, _x.fill_color.a, _x.lifetime.secs, _x.lifetime.nsecs,) = _get_struct_3i3d5fB4f2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.points.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.outline_colors = []
      for i in range(0, length):
        val1 = std_msgs.ColorRGBA()
        _x = val1
        start = end
        end += 16
        (_x.r, _x.g, _x.b, _x.a,) = _get_struct_4f().unpack(str[start:end])
        self.outline_colors.append(val1)
      self.lifetime.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3i3d5fB4f2i = None
def _get_struct_3i3d5fB4f2i():
    global _struct_3i3d5fB4f2i
    if _struct_3i3d5fB4f2i is None:
        _struct_3i3d5fB4f2i = struct.Struct("<3i3d5fB4f2i")
    return _struct_3i3d5fB4f2i
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
