# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/davinio/catkin_ws/src/geometric_shapes

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/davinio/catkin_ws/build_isolated/geometric_shapes

# Include any dependencies generated for this target.
include test/CMakeFiles/test_bounding_box.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/test_bounding_box.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/test_bounding_box.dir/flags.make

test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o: test/CMakeFiles/test_bounding_box.dir/flags.make
test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o: /home/davinio/catkin_ws/src/geometric_shapes/test/test_bounding_box.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/davinio/catkin_ws/build_isolated/geometric_shapes/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o"
	cd /home/davinio/catkin_ws/build_isolated/geometric_shapes/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o -c /home/davinio/catkin_ws/src/geometric_shapes/test/test_bounding_box.cpp

test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.i"
	cd /home/davinio/catkin_ws/build_isolated/geometric_shapes/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/davinio/catkin_ws/src/geometric_shapes/test/test_bounding_box.cpp > CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.i

test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.s"
	cd /home/davinio/catkin_ws/build_isolated/geometric_shapes/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/davinio/catkin_ws/src/geometric_shapes/test/test_bounding_box.cpp -o CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.s

test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o.requires:

.PHONY : test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o.requires

test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o.provides: test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o.requires
	$(MAKE) -f test/CMakeFiles/test_bounding_box.dir/build.make test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o.provides.build
.PHONY : test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o.provides

test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o.provides.build: test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o


# Object files for target test_bounding_box
test_bounding_box_OBJECTS = \
"CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o"

# External object files for target test_bounding_box
test_bounding_box_EXTERNAL_OBJECTS =

/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: test/CMakeFiles/test_bounding_box.dir/build.make
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: gtest/googlemock/gtest/libgtest.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/libgeometric_shapes.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/librandom_numbers.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/libresource_retriever.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/librostime.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/libcpp_common.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libassimp.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libqhull.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/librandom_numbers.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/libresource_retriever.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/librostime.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /opt/ros/melodic/lib/libcpp_common.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box: test/CMakeFiles/test_bounding_box.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/davinio/catkin_ws/build_isolated/geometric_shapes/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box"
	cd /home/davinio/catkin_ws/build_isolated/geometric_shapes/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_bounding_box.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/test_bounding_box.dir/build: /home/davinio/catkin_ws/devel_isolated/geometric_shapes/lib/geometric_shapes/test_bounding_box

.PHONY : test/CMakeFiles/test_bounding_box.dir/build

test/CMakeFiles/test_bounding_box.dir/requires: test/CMakeFiles/test_bounding_box.dir/test_bounding_box.cpp.o.requires

.PHONY : test/CMakeFiles/test_bounding_box.dir/requires

test/CMakeFiles/test_bounding_box.dir/clean:
	cd /home/davinio/catkin_ws/build_isolated/geometric_shapes/test && $(CMAKE_COMMAND) -P CMakeFiles/test_bounding_box.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/test_bounding_box.dir/clean

test/CMakeFiles/test_bounding_box.dir/depend:
	cd /home/davinio/catkin_ws/build_isolated/geometric_shapes && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/davinio/catkin_ws/src/geometric_shapes /home/davinio/catkin_ws/src/geometric_shapes/test /home/davinio/catkin_ws/build_isolated/geometric_shapes /home/davinio/catkin_ws/build_isolated/geometric_shapes/test /home/davinio/catkin_ws/build_isolated/geometric_shapes/test/CMakeFiles/test_bounding_box.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/test_bounding_box.dir/depend

