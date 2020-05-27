  import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
  from nav_msgs.msg import Odometry

  def callback(msg):
  		print msg.pose.pose

  	rospy.init_node('check_odometry')
  	odom_sub = rospy.Subscriber('/odom', Odometry)

  	rospy.spin()
