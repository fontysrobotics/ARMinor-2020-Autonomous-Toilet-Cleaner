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
CMAKE_SOURCE_DIR = /home/davinio/catkin_ws/src/octomap/octomap

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/davinio/catkin_ws/build_isolated/octomap/devel

# Include any dependencies generated for this target.
include src/CMakeFiles/graph2tree.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/graph2tree.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/graph2tree.dir/flags.make

src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o: src/CMakeFiles/graph2tree.dir/flags.make
src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o: /home/davinio/catkin_ws/src/octomap/octomap/src/graph2tree.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/davinio/catkin_ws/build_isolated/octomap/devel/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o"
	cd /home/davinio/catkin_ws/build_isolated/octomap/devel/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/graph2tree.dir/graph2tree.cpp.o -c /home/davinio/catkin_ws/src/octomap/octomap/src/graph2tree.cpp

src/CMakeFiles/graph2tree.dir/graph2tree.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/graph2tree.dir/graph2tree.cpp.i"
	cd /home/davinio/catkin_ws/build_isolated/octomap/devel/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/davinio/catkin_ws/src/octomap/octomap/src/graph2tree.cpp > CMakeFiles/graph2tree.dir/graph2tree.cpp.i

src/CMakeFiles/graph2tree.dir/graph2tree.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/graph2tree.dir/graph2tree.cpp.s"
	cd /home/davinio/catkin_ws/build_isolated/octomap/devel/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/davinio/catkin_ws/src/octomap/octomap/src/graph2tree.cpp -o CMakeFiles/graph2tree.dir/graph2tree.cpp.s

src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o.requires:

.PHONY : src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o.requires

src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o.provides: src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o.requires
	$(MAKE) -f src/CMakeFiles/graph2tree.dir/build.make src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o.provides.build
.PHONY : src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o.provides

src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o.provides.build: src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o


# Object files for target graph2tree
graph2tree_OBJECTS = \
"CMakeFiles/graph2tree.dir/graph2tree.cpp.o"

# External object files for target graph2tree
graph2tree_EXTERNAL_OBJECTS =

/home/davinio/catkin_ws/src/octomap/octomap/bin/graph2tree: src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o
/home/davinio/catkin_ws/src/octomap/octomap/bin/graph2tree: src/CMakeFiles/graph2tree.dir/build.make
/home/davinio/catkin_ws/src/octomap/octomap/bin/graph2tree: /home/davinio/catkin_ws/src/octomap/octomap/lib/liboctomap.so.1.9.5
/home/davinio/catkin_ws/src/octomap/octomap/bin/graph2tree: /home/davinio/catkin_ws/src/octomap/octomap/lib/liboctomath.so.1.9.5
/home/davinio/catkin_ws/src/octomap/octomap/bin/graph2tree: src/CMakeFiles/graph2tree.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/davinio/catkin_ws/build_isolated/octomap/devel/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/davinio/catkin_ws/src/octomap/octomap/bin/graph2tree"
	cd /home/davinio/catkin_ws/build_isolated/octomap/devel/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/graph2tree.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/graph2tree.dir/build: /home/davinio/catkin_ws/src/octomap/octomap/bin/graph2tree

.PHONY : src/CMakeFiles/graph2tree.dir/build

src/CMakeFiles/graph2tree.dir/requires: src/CMakeFiles/graph2tree.dir/graph2tree.cpp.o.requires

.PHONY : src/CMakeFiles/graph2tree.dir/requires

src/CMakeFiles/graph2tree.dir/clean:
	cd /home/davinio/catkin_ws/build_isolated/octomap/devel/src && $(CMAKE_COMMAND) -P CMakeFiles/graph2tree.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/graph2tree.dir/clean

src/CMakeFiles/graph2tree.dir/depend:
	cd /home/davinio/catkin_ws/build_isolated/octomap/devel && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/davinio/catkin_ws/src/octomap/octomap /home/davinio/catkin_ws/src/octomap/octomap/src /home/davinio/catkin_ws/build_isolated/octomap/devel /home/davinio/catkin_ws/build_isolated/octomap/devel/src /home/davinio/catkin_ws/build_isolated/octomap/devel/src/CMakeFiles/graph2tree.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/graph2tree.dir/depend

