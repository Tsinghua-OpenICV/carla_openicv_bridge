# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from zzz_driver_msgs/RigidBodyStateStamped.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import zzz_driver_msgs.msg
import geometry_msgs.msg
import protocol.std_msgs.msg as std_msgs

class RigidBodyStateStamped(genpy.Message):
  _md5sum = "3ce82e0047669e82456465abb8d64149"
  _type = "zzz_driver_msgs/RigidBodyStateStamped"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Stamped version of RigidBodyState

Header header
RigidBodyState state

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
MSG: zzz_driver_msgs/RigidBodyState
# This message contains commonly used state variables of rigid body

# ID of frame fixed to the rigid body
string child_frame_id

# Location and orientatation of the object
geometry_msgs/PoseWithCovariance  pose

# Linear and angular velocity of the object
geometry_msgs/TwistWithCovariance twist

# Linear and angular acceleration of the object
geometry_msgs/AccelWithCovariance accel

================================================================================
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/TwistWithCovariance
# This expresses velocity in free space with uncertainty.

Twist twist

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/AccelWithCovariance
# This expresses acceleration in free space with uncertainty.

Accel accel

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Accel
# This expresses acceleration in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular
"""
  __slots__ = ['header','state']
  _slot_types = ['std_msgs/Header','zzz_driver_msgs/RigidBodyState']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,state

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RigidBodyStateStamped, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.Header()
      if self.state is None:
        self.state = zzz_driver_msgs.msg.RigidBodyState()
    else:
      self.header = std_msgs.Header()
      self.state = zzz_driver_msgs.msg.RigidBodyState()

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
      _x = self.state.child_frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.state.pose.pose.position.x, _x.state.pose.pose.position.y, _x.state.pose.pose.position.z, _x.state.pose.pose.orientation.x, _x.state.pose.pose.orientation.y, _x.state.pose.pose.orientation.z, _x.state.pose.pose.orientation.w))
      buff.write(_get_struct_36d().pack(*self.state.pose.covariance))
      _x = self
      buff.write(_get_struct_6d().pack(_x.state.twist.twist.linear.x, _x.state.twist.twist.linear.y, _x.state.twist.twist.linear.z, _x.state.twist.twist.angular.x, _x.state.twist.twist.angular.y, _x.state.twist.twist.angular.z))
      buff.write(_get_struct_36d().pack(*self.state.twist.covariance))
      _x = self
      buff.write(_get_struct_6d().pack(_x.state.accel.accel.linear.x, _x.state.accel.accel.linear.y, _x.state.accel.accel.linear.z, _x.state.accel.accel.angular.x, _x.state.accel.accel.angular.y, _x.state.accel.accel.angular.z))
      buff.write(_get_struct_36d().pack(*self.state.accel.covariance))
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
      if self.state is None:
        self.state = zzz_driver_msgs.msg.RigidBodyState()
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
        self.state.child_frame_id = str[start:end].decode('utf-8')
      else:
        self.state.child_frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.state.pose.pose.position.x, _x.state.pose.pose.position.y, _x.state.pose.pose.position.z, _x.state.pose.pose.orientation.x, _x.state.pose.pose.orientation.y, _x.state.pose.pose.orientation.z, _x.state.pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.state.pose.covariance = _get_struct_36d().unpack(str[start:end])
      _x = self
      start = end
      end += 48
      (_x.state.twist.twist.linear.x, _x.state.twist.twist.linear.y, _x.state.twist.twist.linear.z, _x.state.twist.twist.angular.x, _x.state.twist.twist.angular.y, _x.state.twist.twist.angular.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 288
      self.state.twist.covariance = _get_struct_36d().unpack(str[start:end])
      _x = self
      start = end
      end += 48
      (_x.state.accel.accel.linear.x, _x.state.accel.accel.linear.y, _x.state.accel.accel.linear.z, _x.state.accel.accel.angular.x, _x.state.accel.accel.angular.y, _x.state.accel.accel.angular.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 288
      self.state.accel.covariance = _get_struct_36d().unpack(str[start:end])
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
      _x = self.state.child_frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.state.pose.pose.position.x, _x.state.pose.pose.position.y, _x.state.pose.pose.position.z, _x.state.pose.pose.orientation.x, _x.state.pose.pose.orientation.y, _x.state.pose.pose.orientation.z, _x.state.pose.pose.orientation.w))
      buff.write(self.state.pose.covariance.tostring())
      _x = self
      buff.write(_get_struct_6d().pack(_x.state.twist.twist.linear.x, _x.state.twist.twist.linear.y, _x.state.twist.twist.linear.z, _x.state.twist.twist.angular.x, _x.state.twist.twist.angular.y, _x.state.twist.twist.angular.z))
      buff.write(self.state.twist.covariance.tostring())
      _x = self
      buff.write(_get_struct_6d().pack(_x.state.accel.accel.linear.x, _x.state.accel.accel.linear.y, _x.state.accel.accel.linear.z, _x.state.accel.accel.angular.x, _x.state.accel.accel.angular.y, _x.state.accel.accel.angular.z))
      buff.write(self.state.accel.covariance.tostring())
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
      if self.state is None:
        self.state = zzz_driver_msgs.msg.RigidBodyState()
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
        self.state.child_frame_id = str[start:end].decode('utf-8')
      else:
        self.state.child_frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.state.pose.pose.position.x, _x.state.pose.pose.position.y, _x.state.pose.pose.position.z, _x.state.pose.pose.orientation.x, _x.state.pose.pose.orientation.y, _x.state.pose.pose.orientation.z, _x.state.pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.state.pose.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      _x = self
      start = end
      end += 48
      (_x.state.twist.twist.linear.x, _x.state.twist.twist.linear.y, _x.state.twist.twist.linear.z, _x.state.twist.twist.angular.x, _x.state.twist.twist.angular.y, _x.state.twist.twist.angular.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 288
      self.state.twist.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      _x = self
      start = end
      end += 48
      (_x.state.accel.accel.linear.x, _x.state.accel.accel.linear.y, _x.state.accel.accel.linear.z, _x.state.accel.accel.angular.x, _x.state.accel.accel.angular.y, _x.state.accel.accel.angular.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 288
      self.state.accel.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

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
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d
_struct_36d = None
def _get_struct_36d():
    global _struct_36d
    if _struct_36d is None:
        _struct_36d = struct.Struct("<36d")
    return _struct_36d
