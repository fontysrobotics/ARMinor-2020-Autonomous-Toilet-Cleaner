#!/usr/bin/env python2

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

#rospy to communicate with ros
import rospy


def callback(data):
    if data is not None:
        cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")

        cv2.imshow("Image window", cv_image)

        #If a is pressed, store the image
        if cv2.waitKey(33) == ord('a'):
            cv2.imwrite('ROSImage.png',cv_image)
        
        
        cv2.waitKey(3)



if __name__ == '__main__':
   
    try:
        rospy.init_node('vision_py')

        while True:
            rospy.Subscriber("/rrbot/camera2/image_raw", Image, callback)
        
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                break
        
            
    except rospy.ROSInterruptException:
        rospy.loginfo("Error occured somewhere")