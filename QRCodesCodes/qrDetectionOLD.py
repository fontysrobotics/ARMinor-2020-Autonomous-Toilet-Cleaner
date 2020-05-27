import cv2
import numpy as np
import sys
import time
import math
import glob

#aruco ros

usePictures = True
Debug = True
font = cv2.FONT_HERSHEY_SIMPLEX

#load all the calibration data
with np.load('CalibrationFileNick.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('_mtx_','_dist_','_rvecs_','_tvecs_')]
    
#prepare array for 3D information
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((2*2,3), np.float32)
objp[:,:2] = np.mgrid[0:2,0:2].T.reshape(-1,2)

#axis = np.float32([[1,0,0], [0,1,0], [0,0,-1]]).reshape(-1,3)

#the shape of the cube overlay
axis = np.float32([[0,0,0], [0,1,0], [1,1,0], [1,0,0],
                   [0,0,-1],[0,1,-1],[1,1,-1],[1,0,-1] ])

state = 0
if usePictures:
    images = glob.glob("QR/*.jpg")
    pictures = []
    for fname in images:
        pictures.append(cv2.imread(fname))
    print("I found "+str(len(pictures))+" images... Good Luck!")
else:
    cap = cv2.VideoCapture(0)

qrDecoder = cv2.QRCodeDetector()




#Shoelace algorithm
#needs an array of cordinates
#A = [1,4]
#B = [2,5]
#vertices = [A,B]
def polygonArea(vertices):                              
  #A function to apply the Shoelace algorithm                   [[[3,4]],[[5,4]],[[12,5]]] =>points[0].ravel() => [3,4]

  numberOfVertices = len(vertices)
  #print("number of vertices = ",numberOfVertices)
  sum1 = 0
  sum2 = 0
  
  for i in range(0,numberOfVertices-1):
    #print("test")
    sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
    sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
  #print("sum1 = ",sum1)
  #Add xn.y1
  sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
  #Add x1.yn
  sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   
  
  area = abs(sum1 - sum2) / 2
  return area

def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist 

def DistanceToLine(imageHeight,ObjectHeight,realHeight,sensorHeight,focalDistance):
    return (focalDistance*realHeight*imageHeight)/(ObjectHeight*sensorHeight)

def GetRealDistanceToLine(x1,y1,x2,y2,img):
    height, width, channels = img.shape
    imageHeight = width
    realHeight = 13

    apertureWidth  = 3888 
    apertureHeight = 2430  
    imageSize = (width,height)
    cameraMatrix = mtx
    fovx, fovy, focalLength, principalPoint, aspectRatio = cv2.calibrationMatrixValues(cameraMatrix, imageSize, apertureWidth, apertureHeight) 

    objectHeight = calculateDistance(x1,y1,x2,y2)
    return DistanceToLine(imageHeight,objectHeight,realHeight,apertureWidth,focalLength)
  
#draw the cube
def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)

    imgpts = np.int32(imgpts).reshape(-1,2)
    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    # draw pillars in blue color
    for i,j in zip(range(4),range(4,8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

    #DRAWING THE "SHADOW"
    #print(imgpts)
    # hull = []
    # hull.append(cv2.convexHull(imgpts, False))
    # cv2.drawContours(img, hull, 0, (0,255,0), 1, 8)
    # hullpts = np.int32(hull).reshape(-1,2)
    # area = polygonArea(hullpts)
    #print(area)

    # blackspotX = corners[3][0][0]
    # blackspotY = corners[3][0][1]
    # greenspotX = corners[1][0][0]
    # greenspotY = corners[1][0][1]

    #print(GetRealDistanceToLine(blackspotX,blackspotY,greenspotX,greenspotY,img))

    return img


def GetDistanceAndAngle(rvecs, tvecs, im):
    #get distance from matrix
    dis = (tvecs.ravel()[2]*9.5).item()

   
    # calc euler angle
    rotation_mat, _ = cv2.Rodrigues(rvecs)
    pose_mat = cv2.hconcat((rotation_mat, tvecs))
    _, _, _, _, _, _, euler_angle = cv2.decomposeProjectionMatrix(pose_mat)

    if(Debug):
        cv2.putText(im,("Distance: "+str(round(dis,2))+"cm"),(5,25),font,1,(255,50,50),2)
        cv2.putText(im,("angles X: "+str(round(euler_angle[0][0],2))+"degree"),(5,65),font,1,(255,50,50),2)
        cv2.putText(im,("angles Y: "+str(round(euler_angle[1][0],2))+"degree"),(5,105),font,1,(255,50,50),2)
        cv2.putText(im,("angles Z: "+str(round(euler_angle[2][0],2))+"degree"),(5,145),font,1,(255,50,50),2)

    return dis,euler_angle


# Display barcode and QR code location
def display(rvecs, tvecs, im):

    # project 3D points to image plane
    imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
    im = draw(im,bbox,imgpts)    

    # Display results
    cv2.imshow("Results", im)



        

# Detect and decode the qrcode
while(1):
    #try:
    if(usePictures):
        time.sleep(2)
        frame = pictures[state]
        if(state<(len(pictures)-1)):
            state=state+1
        else:
            state=0
    else:
        _, frame = cap.read()

    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)

    #put the bbox in the order Cv2 Expects
    idx = [1,2,0,3]
    bbox = bbox[idx]

    #imgpts = tuple(map(tuple, imgpts.reshape(8, 2)))

    if len(data)>0:
    # print("Decoded Data : {}".format(data))

        #calculate 3D points
        ret,rvecs, tvecs = cv2.solvePnP(objp, bbox, mtx, dist)

        #calculate angle and distance
        GetDistanceAndAngle(rvecs, tvecs, frame)

        #Display the shape or QR Code
        display(rvecs,tvecs, frame)

        
        rectifiedImage = np.uint8(rectifiedImage)
        cv2.imshow("Rectified QRCode", rectifiedImage)
    else:
        cv2.imshow("Results", frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    time.sleep(0.05)
    #except:
    #    print("errrrrroooooooorrrrrrr!!!!!!!!!!!!!!!")

cv2.destroyAllWindows()
if(not usePictures):
    cap.release()
