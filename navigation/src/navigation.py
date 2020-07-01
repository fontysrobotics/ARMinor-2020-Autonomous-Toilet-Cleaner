#!/usr/bin/env python

#rospy to communicate with ros
import rospy

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
 #x,y:w,z
waypoint1 = [0.512904361916, -4.55462047238, 1, 0]      #bottom right
waypoint2 = [-3.87694825, -4.37246237871, 0.7,0.7]      #bottom left
qrCode = [-4.97636646652, 4.29934520406, -0.7, -0.7] 
toilet = [-6.3675401338, 0.466594043915, 0.7, -0.7] 
 
#waypoints = [waypoint1,waypoint2,qrCode,waypoint2,waypoint1]
waypoints = [qrCode,toilet]

def movebase_client(waypoint):
 
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    
    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    
    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    
    # set goal on the "map" coordinate frame 
    goal.target_pose.pose.position.x = waypoint[0]
    goal.target_pose.pose.position.y = waypoint[1] 
    # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.z = waypoint[2]
    goal.target_pose.pose.orientation.w = waypoint[3]
    
    # Sends the goal to the action server.
    client.send_goal(goal)
    # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
    # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result() 
 

#-----------------------------------------------------------------------

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
   
    try:
        # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        for waypoint in waypoints:
            result = movebase_client(waypoint)
            if result:
                rospy.loginfo("Goal execution done!")
            
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")