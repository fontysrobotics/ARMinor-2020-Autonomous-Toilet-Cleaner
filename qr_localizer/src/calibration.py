import sys
import os
import numpy as np
import cv2
import glob

def calibrate(picturesLocation):
    chessX = 9
    chessY = 6
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((chessX*chessY,3), np.float32)
    objp[:,:2] = np.mgrid[0:chessX,0:chessY].T.reshape(-1,2)

    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.

    images = glob.glob(picturesLocation)

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (chessX,chessY),None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (chessX,chessY), corners2,ret)
            cv2.imshow('img',img)
            cv2.waitKey(500)

    cv2.destroyAllWindows()
    print(objpoints)
    print(imgpoints)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
    return mtx, dist, rvecs, tvecs

def undistortPicture(pictureLocation, mtx, dist):
    lastImg = cv2.imread(pictureLocation)
    h,  w = lastImg.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

    # undistort
    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
    dst = cv2.remap(lastImg,mapx,mapy,cv2.INTER_LINEAR)

    # crop the image
    x,y,w,h = roi
    dst = dst[y:y+h, x:x+w]
    cv2.imshow('Calibrated',dst)
    #cv2.imwrite('calibresult.jpg',dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    filename = "CalibrationFileNick.npz"
    #check if it is calibrated
    if(not os.path.exists(filename)):
        print("start calibrating")
        _mtx_, _dist_, _rvecs_, _tvecs_ = calibrate('CalibrationNick/*.jpg')
        np.savez(filename, _mtx_=_mtx_,  _dist_= _dist_, _rvecs_=_rvecs_, _tvecs_=_tvecs_ )
        print("done calibarting")
     
    #get data from files
    npzfile = np.load(filename)
    sorted(npzfile.files)

    #undistort
    #undistortPicture('calibrationImg/t1.jpg', npzfile['_mtx_'], npzfile['_dist_'])

if __name__ == "__main__":
    main()

