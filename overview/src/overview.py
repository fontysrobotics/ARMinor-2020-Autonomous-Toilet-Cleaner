#!/usr/bin/env python2

#rospy to communicate with ros
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

from nav_msgs.msg import Odometry

thisdict = {
    "RobotName"         :   "Toiletcleaner",
    "Robot id"          :   1,
    "Toilets cleaned"   :   5
}

global odom

def printDictonary():
    for x, y in thisdict.items():
        print(x + " = " + y)     

def Update(name,value):
    thisdict[name] = value
    
def Remove(name):
    thisdict.pop(name)

def Clear():
    thisdict.clear()

def AddValue(name):
    thisdict[name] = thisdict[name]+1

def Getvalue(name):
    return thisdict[name]


def callback(msg):
    odom = msg
    printDictonary()
    print(odom)


if __name__ == '__main__':


    try:
        rospy.init_node('overview_py')
        odom_sub = rospy.Subscriber('/odom', Odometry, callback)
        rospy.spin()
        
        
            
    except rospy.ROSInterruptException:
        rospy.loginfo("Error occured somewhere")