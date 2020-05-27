

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import time
## END_SUB_TUTORIAL


def move_group():
  ## First initialize `moveit_commander`_ and a `rospy`_ node:
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('move_group', anonymous=True)

  ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
  ## kinematic model and the robot's current joint states
  robot = moveit_commander.RobotCommander()

  ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
  ## for getting, setting, and updating the robot's internal understanding of the
  ## surrounding world:
  scene = moveit_commander.PlanningSceneInterface()

  ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
  ## to a planning group (group of joints).  In this tutorial the group is the primary
  ## arm joints in the Panda robot, so we set the group's name to "panda_arm".
  ## If you are using a different robot, change this value to the name of your robot
  ## arm planning group.
  ## This interface can be used to plan and execute motions:
  group_name = "arm"
  move_group = moveit_commander.MoveGroupCommander(group_name)
  move_group.set_planner_id("STOMP")

  ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
  ## trajectories in Rviz:
  display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                 moveit_msgs.msg.DisplayTrajectory, queue_size = 20)

  group_variable_values = move_group.get_current_joint_values()

  group_variable_values[0] = 0
  group_variable_values[1] = 0
  group_variable_values[2] = 0
  group_variable_values[3] = 0
  group_variable_values[4] = 0
  group_variable_values[5] = 0
  move_group.set_joint_value_target(group_variable_values)

  plan2 = move_group.plan()
 # display_trajectory = moveit_msgs.msg.DisplayTrajectory()
  #display_trajectory.trajectory_start = robot.get_current_state()
  #display_trajectory.trajectory.append(plan2)
  # Publish
  #display_trajectory_publisher.publish(display_trajectory);
  move_group.go(group_variable_values, wait = True)

  group_variable_values[0] = 0
  group_variable_values[1] = -1.4
  group_variable_values[2] = 0.1
  group_variable_values[3] = 0
  group_variable_values[4] = 0
  group_variable_values[5] = 0
  move_group.set_joint_value_target(group_variable_values)

  plan2 = move_group.plan()
  move_group.go(group_variable_values, wait = True)

  group_variable_values[0] = 0
  group_variable_values[1] = 0
  group_variable_values[2] = 0
  group_variable_values[3] = 0
  group_variable_values[4] = 0
  group_variable_values[5] = 0
  move_group.set_joint_value_target(group_variable_values)

  plan2 = move_group.plan()
  move_group.go(group_variable_values, wait = True)

  group_variable_values[0] = 1
  group_variable_values[1] = -1.4
  group_variable_values[2] = 0.1
  group_variable_values[3] = 0
  group_variable_values[4] = 0
  group_variable_values[5] = 0
  move_group.set_joint_value_target(group_variable_values)

  plan2 = move_group.plan()
  move_group.go(group_variable_values, wait = True)

  group_variable_values[0] = -1
  group_variable_values[1] = -1.4
  group_variable_values[2] = -0.1
  group_variable_values[3] = 0
  group_variable_values[4] = 0
  group_variable_values[5] = 0
  move_group.set_joint_value_target(group_variable_values)

  plan2 = move_group.plan()
  move_group.go(group_variable_values, wait = True)

  group_variable_values[0] = 0.1
  group_variable_values[1] = 0
  group_variable_values[2] = 0
  group_variable_values[3] = 0
  group_variable_values[4] = 0
  group_variable_values[5] = 0
  move_group.set_joint_value_target(group_variable_values)

  plan2 = move_group.plan()
  move_group.go(group_variable_values, wait = True)

  move_group.clear_pose_targets()
  moveit_commander.roscpp_shutdown()
  ## We can plan a motion for this group to a desired pose for the
  ## end-effector:
  #pose_goal = move_group.get_current_pose()

  #pose_goal = geometry_msgs.msg.Pose()
  #pose_goal.orientation.w = 0.5
  #pose_goal.position.x = 0.0
  #pose_goal.position.y = 0.9
  #pose_goal.position.z = 0.1

  #move_group.set_pose_target(pose_goal)

  #plan1 = move_group.plan()
  ## END_SUB_TUTORIAL




if __name__=='__main__':
  try:
    move_group()
  except rospy.ROSInterruptException:
    pass


