#!/usr/bin/env python2


#This node is used for calibrating the camera.
#Open this file and drive past the checkerboard.
#Press A if you have made enough pictures
#It will store the callibration file as en NPZ






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
        calibration.addImage(cv_image)
        

        #If a is pressed, store the image
        if cv2.waitKey(33) == ord('a'):
            cv2.destroyAllWindows()
            print("saving")
            #cv2.imwrite('ROSImage.png',cv_image)
            try:
                calibration.calibrate()
                calibration.saveCalibrationFile(filename="RosCalibrationFile.npz")
            except:
                 rospy.signal_shutdown("Done calibrating")   
            rospy.signal_shutdown("Done calibrating")
        

        #cv2.waitKey(3)

        r = rospy.Rate(2) # 2hz
        r.sleep()



if __name__ == '__main__':
   
    try:
        rospy.init_node('vision_py',disable_signals=True)

        #while True:
        rospy.Subscriber("/rrbot/camera2/image_raw", Image, callback)
        rospy.spin()
        
        
            
    except rospy.ROSInterruptException:
        rospy.loginfo("Error occured somewhere")