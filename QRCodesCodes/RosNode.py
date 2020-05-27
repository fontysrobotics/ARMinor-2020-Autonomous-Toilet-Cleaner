import numpy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

#rospy to communicate with ros
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

from qrDetection import *
qrDetector = QrDetector(mode=2,visualizeResult=True)

dtype = np.float64

def talker(dataArray):
    #print(type(dataArray),dataArray)
    dataArrayNumpy = numpy.array(dataArray)
    dataArrayNumpy = dataArrayNumpy.astype('float32')
    #print(type(dataArrayNumpy),dataArrayNumpy)
    pub = rospy.Publisher('QrCodeValues', numpy_msg(Floats),queue_size=10)
    #r = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
    #dataArrayNumpy = numpy.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)
    pub.publish(dataArrayNumpy)
        #r.sleep()




def callback(data):
    if data is not None:
        cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")

        #cv2.imshow("Image window", cv_image)
        data = qrDetector.readImage(cv_image)
        #data = numpy.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)
        talker(data)
        cv2.waitKey(3)



if __name__ == '__main__':
   
    try:
        rospy.init_node('vision_py')
        rospy.Subscriber("/rrbot/camera2/image_raw", Image, callback)
        rospy.spin() #keeps python exiting until this node is stopped
        
            
    except rospy.ROSInterruptException:
        rospy.loginfo("Error occured somewhere")