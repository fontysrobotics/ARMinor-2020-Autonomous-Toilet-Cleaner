#!/usr/bin/env python2

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

#rospy to communicate with ros
import rospy

from calibration import *

calibration = cameraCalibration(debug=True,showWindow=True)

def callback(data):
    if data is not None:
        cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
        print("test")
        cv2.imshow("Image window", cv_image)
        #add picture to 
        #calibration.addImage(cv_image)
        

        #If a is pressed, store the image
        if cv2.waitKey(33) == ord('a'):
            print("saving")
            #cv2.imwrite('ROSImage.png',cv_image)
            #calibration.calibrate()
            #calibration.saveCalibrationFile(filename="RosCalibrationFile.npz")
        
        #cv2.waitKey(3)

        r = rospy.Rate(2) # 2hz
        r.sleep()



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