# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from moveit_msgs/BoundingVolume.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import shape_msgs.msg

class BoundingVolume(genpy.Message):
  _md5sum = "22db94010f39e9198032cb4a1aeda26e"
  _type = "moveit_msgs/BoundingVolume"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Define a volume in 3D

# A set of solid geometric primitives that make up the volume to define (as a union)
shape_msgs/SolidPrimitive[] primitives

# The poses at which the primitives are located
geometry_msgs/Pose[] primitive_poses

# In addition to primitives, meshes can be specified to add to the bounding volume (again, as union)
shape_msgs/Mesh[] meshes

# The poses at which the meshes are located
geometry_msgs/Pose[] mesh_poses

================================================================================
MSG: shape_msgs/SolidPrimitive
# Define box, sphere, cylinder, cone 
# All shapes are defined to have their bounding boxes centered around 0,0,0.

uint8 BOX=1
uint8 SPHERE=2
uint8 CYLINDER=3
uint8 CONE=4

# The type of the shape
uint8 type


# The dimensions of the shape
float64[] dimensions

# The meaning of the shape dimensions: each constant defines the index in the 'dimensions' array

# For the BOX type, the X, Y, and Z dimensions are the length of the corresponding
# sides of the box.
uint8 BOX_X=0
uint8 BOX_Y=1
uint8 BOX_Z=2


# For the SPHERE type, only one component is used, and it gives the radius of
# the sphere.
uint8 SPHERE_RADIUS=0


# For the CYLINDER and CONE types, the center line is oriented along
# the Z axis.  Therefore the CYLINDER_HEIGHT (CONE_HEIGHT) component
# of dimensions gives the height of the cylinder (cone).  The
# CYLINDER_RADIUS (CONE_RADIUS) component of dimensions gives the
# radius of the base of the cylinder (cone).  Cone and cylinder
# primitives are defined to be circular. The tip of the cone is
# pointing up, along +Z axis.

uint8 CYLINDER_HEIGHT=0
uint8 CYLINDER_RADIUS=1

uint8 CONE_HEIGHT=0
uint8 CONE_RADIUS=1

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
MSG: shape_msgs/Mesh
# Definition of a mesh

# list of triangles; the index values refer to positions in vertices[]
MeshTriangle[] triangles

# the actual vertices that make up the mesh
geometry_msgs/Point[] vertices

================================================================================
MSG: shape_msgs/MeshTriangle
# Definition of a triangle's vertices
uint32[3] vertex_indices
"""
  __slots__ = ['primitives','primitive_poses','meshes','mesh_poses']
  _slot_types = ['shape_msgs/SolidPrimitive[]','geometry_msgs/Pose[]','shape_msgs/Mesh[]','geometry_msgs/Pose[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       primitives,primitive_poses,meshes,mesh_poses

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BoundingVolume, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.primitives is None:
        self.primitives = []
      if self.primitive_poses is None:
        self.primitive_poses = []
      if self.meshes is None:
        self.meshes = []
      if self.mesh_poses is None:
        self.mesh_poses = []
    else:
      self.primitives = []
      self.primitive_poses = []
      self.meshes = []
      self.mesh_poses = []

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
      length = len(self.primitives)
      buff.write(_struct_I.pack(length))
      for val1 in self.primitives:
        buff.write(_get_struct_B().pack(val1.type))
        length = len(val1.dimensions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.dimensions))
      length = len(self.primitive_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.primitive_poses:
        _v1 = val1.position
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v2 = val1.orientation
        _x = _v2
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.meshes)
      buff.write(_struct_I.pack(length))
      for val1 in self.meshes:
        length = len(val1.triangles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.triangles:
          buff.write(_get_struct_3I().pack(*val2.vertex_indices))
        length = len(val1.vertices)
        buff.write(_struct_I.pack(length))
        for val2 in val1.vertices:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.mesh_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.mesh_poses:
        _v3 = val1.position
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v4 = val1.orientation
        _x = _v4
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.primitives is None:
        self.primitives = None
      if self.primitive_poses is None:
        self.primitive_poses = None
      if self.meshes is None:
        self.meshes = None
      if self.mesh_poses is None:
        self.mesh_poses = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.primitives = []
      for i in range(0, length):
        val1 = shape_msgs.msg.SolidPrimitive()
        start = end
        end += 1
        (val1.type,) = _get_struct_B().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.dimensions = struct.unpack(pattern, str[start:end])
        self.primitives.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.primitive_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v5 = val1.position
        _x = _v5
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v6 = val1.orientation
        _x = _v6
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.primitive_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.meshes = []
      for i in range(0, length):
        val1 = shape_msgs.msg.Mesh()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.triangles = []
        for i in range(0, length):
          val2 = shape_msgs.msg.MeshTriangle()
          start = end
          end += 12
          val2.vertex_indices = _get_struct_3I().unpack(str[start:end])
          val1.triangles.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.vertices = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.vertices.append(val2)
        self.meshes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mesh_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v7 = val1.position
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v8 = val1.orientation
        _x = _v8
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.mesh_poses.append(val1)
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
      length = len(self.primitives)
      buff.write(_struct_I.pack(length))
      for val1 in self.primitives:
        buff.write(_get_struct_B().pack(val1.type))
        length = len(val1.dimensions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.dimensions.tostring())
      length = len(self.primitive_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.primitive_poses:
        _v9 = val1.position
        _x = _v9
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v10 = val1.orientation
        _x = _v10
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.meshes)
      buff.write(_struct_I.pack(length))
      for val1 in self.meshes:
        length = len(val1.triangles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.triangles:
          buff.write(val2.vertex_indices.tostring())
        length = len(val1.vertices)
        buff.write(_struct_I.pack(length))
        for val2 in val1.vertices:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.mesh_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.mesh_poses:
        _v11 = val1.position
        _x = _v11
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v12 = val1.orientation
        _x = _v12
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.primitives is None:
        self.primitives = None
      if self.primitive_poses is None:
        self.primitive_poses = None
      if self.meshes is None:
        self.meshes = None
      if self.mesh_poses is None:
        self.mesh_poses = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.primitives = []
      for i in range(0, length):
        val1 = shape_msgs.msg.SolidPrimitive()
        start = end
        end += 1
        (val1.type,) = _get_struct_B().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.dimensions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        self.primitives.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.primitive_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v13 = val1.position
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v14 = val1.orientation
        _x = _v14
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.primitive_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.meshes = []
      for i in range(0, length):
        val1 = shape_msgs.msg.Mesh()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.triangles = []
        for i in range(0, length):
          val2 = shape_msgs.msg.MeshTriangle()
          start = end
          end += 12
          val2.vertex_indices = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=3)
          val1.triangles.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.vertices = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.vertices.append(val2)
        self.meshes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mesh_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v15 = val1.position
        _x = _v15
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v16 = val1.orientation
        _x = _v16
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.mesh_poses.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
