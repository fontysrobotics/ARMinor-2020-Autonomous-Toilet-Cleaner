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
CMAKE_SOURCE_DIR = /home/davinio/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/davinio/catkin_ws/build

# Utility rule file for test_reading_writing_config_autogen.

# Include the progress variables for this target.
include moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/progress.make

moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/davinio/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC for target test_reading_writing_config"
	cd /home/davinio/catkin_ws/build/moveit/moveit_setup_assistant && /usr/bin/cmake -E cmake_autogen /home/davinio/catkin_ws/build/moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir Release

test_reading_writing_config_autogen: moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen
test_reading_writing_config_autogen: moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/build.make

.PHONY : test_reading_writing_config_autogen

# Rule to build all files generated by this target.
moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/build: test_reading_writing_config_autogen

.PHONY : moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/build

moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/clean:
	cd /home/davinio/catkin_ws/build/moveit/moveit_setup_assistant && $(CMAKE_COMMAND) -P CMakeFiles/test_reading_writing_config_autogen.dir/cmake_clean.cmake
.PHONY : moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/clean

moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/depend:
	cd /home/davinio/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/davinio/catkin_ws/src /home/davinio/catkin_ws/src/moveit/moveit_setup_assistant /home/davinio/catkin_ws/build /home/davinio/catkin_ws/build/moveit/moveit_setup_assistant /home/davinio/catkin_ws/build/moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : moveit/moveit_setup_assistant/CMakeFiles/test_reading_writing_config_autogen.dir/depend

