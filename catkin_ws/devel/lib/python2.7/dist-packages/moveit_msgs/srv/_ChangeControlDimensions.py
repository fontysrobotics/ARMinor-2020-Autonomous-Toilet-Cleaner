# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from moveit_msgs/ChangeControlDimensionsRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ChangeControlDimensionsRequest(genpy.Message):
  _md5sum = "64c0dd6d519e78f5ce2626b06dab34c1"
  _type = "moveit_msgs/ChangeControlDimensionsRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """



bool control_x_translation
bool control_y_translation
bool control_z_translation
bool control_x_rotation
bool control_y_rotation
bool control_z_rotation
"""
  __slots__ = ['control_x_translation','control_y_translation','control_z_translation','control_x_rotation','control_y_rotation','control_z_rotation']
  _slot_types = ['bool','bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       control_x_translation,control_y_translation,control_z_translation,control_x_rotation,control_y_rotation,control_z_rotation

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ChangeControlDimensionsRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.control_x_translation is None:
        self.control_x_translation = False
      if self.control_y_translation is None:
        self.control_y_translation = False
      if self.control_z_translation is None:
        self.control_z_translation = False
      if self.control_x_rotation is None:
        self.control_x_rotation = False
      if self.control_y_rotation is None:
        self.control_y_rotation = False
      if self.control_z_rotation is None:
        self.control_z_rotation = False
    else:
      self.control_x_translation = False
      self.control_y_translation = False
      self.control_z_translation = False
      self.control_x_rotation = False
      self.control_y_rotation = False
      self.control_z_rotation = False

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
      buff.write(_get_struct_6B().pack(_x.control_x_translation, _x.control_y_translation, _x.control_z_translation, _x.control_x_rotation, _x.control_y_rotation, _x.control_z_rotation))
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
      end += 6
      (_x.control_x_translation, _x.control_y_translation, _x.control_z_translation, _x.control_x_rotation, _x.control_y_rotation, _x.control_z_rotation,) = _get_struct_6B().unpack(str[start:end])
      self.control_x_translation = bool(self.control_x_translation)
      self.control_y_translation = bool(self.control_y_translation)
      self.control_z_translation = bool(self.control_z_translation)
      self.control_x_rotation = bool(self.control_x_rotation)
      self.control_y_rotation = bool(self.control_y_rotation)
      self.control_z_rotation = bool(self.control_z_rotation)
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
      buff.write(_get_struct_6B().pack(_x.control_x_translation, _x.control_y_translation, _x.control_z_translation, _x.control_x_rotation, _x.control_y_rotation, _x.control_z_rotation))
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
      end += 6
      (_x.control_x_translation, _x.control_y_translation, _x.control_z_translation, _x.control_x_rotation, _x.control_y_rotation, _x.control_z_rotation,) = _get_struct_6B().unpack(str[start:end])
      self.control_x_translation = bool(self.control_x_translation)
      self.control_y_translation = bool(self.control_y_translation)
      self.control_z_translation = bool(self.control_z_translation)
      self.control_x_rotation = bool(self.control_x_rotation)
      self.control_y_rotation = bool(self.control_y_rotation)
      self.control_z_rotation = bool(self.control_z_rotation)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6B = None
def _get_struct_6B():
    global _struct_6B
    if _struct_6B is None:
        _struct_6B = struct.Struct("<6B")
    return _struct_6B
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from moveit_msgs/ChangeControlDimensionsResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ChangeControlDimensionsResponse(genpy.Message):
  _md5sum = "358e233cde0c8a8bcfea4ce193f8fc15"
  _type = "moveit_msgs/ChangeControlDimensionsResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success

"""
  __slots__ = ['success']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ChangeControlDimensionsResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
    else:
      self.success = False

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
      buff.write(_get_struct_B().pack(self.success))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
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
      buff.write(_get_struct_B().pack(self.success))
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
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class ChangeControlDimensions(object):
  _type          = 'moveit_msgs/ChangeControlDimensions'
  _md5sum = '35b43a24f32e4654e4afa7596399fc3c'
  _request_class  = ChangeControlDimensionsRequest
  _response_class = ChangeControlDimensionsResponse
