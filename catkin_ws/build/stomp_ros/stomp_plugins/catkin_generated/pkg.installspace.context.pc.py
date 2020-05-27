# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/usr/include;/usr/include/eigen3".split(';') if "${prefix}/include;/usr/include;/usr/include/eigen3" != "" else []
PROJECT_CATKIN_DEPENDS = "eigen_conversions;moveit_core;moveit_ros_planning;pluginlib;rosconsole;roslib;stomp_core;stomp_moveit;xmlrpcpp".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lstomp_plugins;/usr/lib/x86_64-linux-gnu/libboost_system.so".split(';') if "-lstomp_plugins;/usr/lib/x86_64-linux-gnu/libboost_system.so" != "" else []
PROJECT_NAME = "stomp_plugins"
PROJECT_SPACE_DIR = "/home/davinio/catkin_ws/install"
PROJECT_VERSION = "0.1.1"
