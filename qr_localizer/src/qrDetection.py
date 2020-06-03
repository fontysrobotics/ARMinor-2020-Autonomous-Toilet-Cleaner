import cv2
import numpy as np
import sys
import time
import math
import glob


font = cv2.FONT_HERSHEY_SIMPLEX


class QrDetector():

    
    def __init__(self, CalibrationFile='CalibrationFile.npz',mode=0,pictureFolder="QR/*.jpg",visualizeResult=False,debug=False,caneraNum=0):
        """
        **This is needed to initialize the module.**

        [CalibrationFile] The file that is made using Calibration class.

        [mode] 0.Camera| 1.Images|2.Live Feed Images

        [pictureFolder] Needed for when using Mode 1

        [visualizeResult] Used to display images

        [debug] Using print debug

        [cameraNum] Needed when using Mode 0
        """
        self.stop = False
        self.qrDecoder = cv2.QRCodeDetector()    
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        self.objp = np.zeros((2*2,3), np.float32)
        self.objp[:,:2] = np.mgrid[0:2,0:2].T.reshape(-1,2)

        self.axis = np.float32([[0,0,0], [0,1,0], [1,1,0], [1,0,0],
                        [0,0,-1],[0,1,-1],[1,1,-1],[1,0,-1] ])

        self.state = 0
        self.debug =debug
        self.visualizeResult = visualizeResult
        self.usePicture=False
        self.mode=mode
        if(mode==2):
            pass
        elif(mode==1):
            self.usePicture=True
            images = glob.glob(pictureFolder)
            self.pictures = []
            for fname in images:
                self.pictures.append(cv2.imread(fname))
            print("I found "+str(len(self.pictures))+" images... Good Luck!")
        else:
            self.cap = cv2.VideoCapture(caneraNum)            

        with np.load(CalibrationFile) as X:
            self.mtx, self.dist, _, _ = [X[i] for i in ('_mtx_','_dist_','_rvecs_','_tvecs_')]

   
    def drawBox(self,img, imgpts):
        """Draws box using 3d image points"""
        imgpts = np.int32(imgpts).reshape(-1,2)
        # draw ground floor in green
        img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
        # draw pillars in blue color
        for i,j in zip(range(4),range(4,8)):
            img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
        # draw top layer in red color
        img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)
        return img

    
    def GetDistanceAndAngle(self,im,rvecs, tvecs, QRsize=13):
        """Use rotation and translation vectors and size of a QR code to determan euler angles and distance"""
        #get distance from matrix
        dis = (tvecs.ravel()[2]*QRsize).item()

        # calc euler angle
        rotation_mat, _ = cv2.Rodrigues(rvecs)
        pose_mat = cv2.hconcat((rotation_mat, tvecs))
        _, _, _, _, _, _, euler_angle = cv2.decomposeProjectionMatrix(pose_mat)
        if(self.visualizeResult):
            cv2.putText(im,("Distance: "+str(round(dis,2))+"cm"),(5,25),font,1,(255,50,50),2)
            cv2.putText(im,("angles X: "+str(round(euler_angle[0][0],2))+"degree"),(5,65),font,1,(255,50,50),2)
            cv2.putText(im,("angles Y: "+str(round(euler_angle[1][0],2))+"degree"),(5,105),font,1,(255,50,50),2)
            cv2.putText(im,("angles Z: "+str(round(euler_angle[2][0],2))+"degree"),(5,145),font,1,(255,50,50),2)
        if(self.debug):
            print("Distance: "+str(dis)+"|AngX: "+str(euler_angle[0][0])+"|AngY: "+str(euler_angle[1][0])+"|AngZ: "+str(euler_angle[2][0]))

        return dis,euler_angle

    # Display barcode and QR code location
    def display(self,im, rvecs,tvecs):
        """Display results and projected images"""
        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(self.axis, rvecs, tvecs, self.mtx, self.dist)
        im = self.drawBox(im,imgpts)
        # Display results
        cv2.imshow("Results", im)
        
    def qrData(self,data):
        """Tests whether the QR-code is part of the service, if so returns information"""
        splitted = data.split(";")
        if(self.debug):
            print("Splitted String contains:",splitted)
        if(splitted[0]=="QRLOCSYS"):
            return True,[splitted[1],splitted[2],splitted[3]],[splitted[4],splitted[5],splitted[6]],splitted[7]
        else:
            return False,[],[],1

    def calculateOwnLocation(self,distance,QRAngX,QRAngY,QRAngZ):
        X=math.cos(QRAngZ)*distance
        Y=math.cos(QRAngZ)*distance
        Z=0
        AngX=0
        AngY=0
        AngZ=180-QRAngZ

        return [X, Y, Z],[AngX,AngY,AngZ]

    def calculateGlobalLocation(self,coordinatesQR,coordinatesRoQR,rotationQR,rotationRoQR):
        X=0
        Y=0
        Z=0
        AngX=0
        AngY=0
        AngZ=0
 
        return [X,Y,Z],[AngX,AngY,AngZ]

    def readImage(self,frame):
        """This only looks for QR-code and processes it from a single input image"""
        data,bbox,rectifiedImage = self.qrDecoder.detectAndDecode(frame)                        
        if len(data)>0:
            varify,coordinates, rotationCoordinates, size = self.qrData(data)
            if (varify):
                idx = [1,2,0,3]
                bbox = bbox[idx]
                ret,rvecs, tvecs = cv2.solvePnP(self.objp, bbox, self.mtx, self.dist)
                dis,ang = self.GetDistanceAndAngle(frame,rvecs,tvecs,float(size))
                if(self.visualizeResult):
                    self.display(frame, rvecs,tvecs)
                    rectifiedImage = np.uint8(rectifiedImage)
                    cv2.imshow("Rectified QRCode", rectifiedImage)
        else:
            if(self.visualizeResult):
                cv2.imshow("Results", frame)
        if(self.visualizeResult):
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                self.stop=True
        time.sleep(0.05)
        #return [dis,ang[0][0],ang[1][0],ang[2][0]]


    def loop(self):
        """Run this in a looping manner to update camerafeed or cycle through images in an image folder"""
        #Use picture or use Camera
        if(self.usePicture):
            time.sleep(2)
            frame = self.pictures[self.state]
            if(self.state<(len(self.pictures)-1)):
                self.state=self.state+1
            else:
                self.state=0
        else:
            _, frame = self.cap.read()

        data,bbox,rectifiedImage = self.qrDecoder.detectAndDecode(frame)
        if len(data)>0:
            varify,coordinates, rotationCoordinates, size = self.qrData(data)
            if (varify):
                idx = [1,2,0,3]
                bbox = bbox[idx]
                ret,rvecs, tvecs = cv2.solvePnP(self.objp, bbox, self.mtx, self.dist)
                dis,ang = self.GetDistanceAndAngle(frame,rvecs,tvecs,float(size))
                if(self.visualizeResult):
                    self.display(frame, rvecs,tvecs)
                    rectifiedImage = np.uint8(rectifiedImage)
                    cv2.imshow("Rectified QRCode", rectifiedImage)
        else:
            if(self.visualizeResult):
                cv2.imshow("Results", frame)
        if(self.visualizeResult):
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                self.stop=True
        time.sleep(0.05)
        #return [dis,ang[0][0],ang[1][0],ang[2][0]]


    def closeCap(self):
        """Used to close the connection with Webcam and destroys open windows."""
        cv2.destroyAllWindows()
        if(not self.usePicture):
            self.cap.release()
    
    # Detect and decode the qrcode
        

if (__name__=="__main__"):
    print("File initialized as main component.")
    qrScan = QrDetector(mode=0,visualizeResult=True,debug=True)
    while(1):
        qrScan.loop()
        if(qrScan.stop):
            qrScan.closeCap()
            break
    print("Tadaa")