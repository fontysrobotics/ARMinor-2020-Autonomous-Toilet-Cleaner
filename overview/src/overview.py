#!/usr/bin/env python2

#rospy to communicate with ros
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

from nav_msgs.msg import Odometry




def callback(msg):
    print (msg.pose.pose)


if __name__ == '__main__':

    try:
        rospy.init_node('overview_py')
        odom_sub = rospy.Subscriber('/odom', Odometry, callback)
        rospy.spin()
        
            
    except rospy.ROSInterruptException:
        rospy.loginfo("Error occured somewhere")