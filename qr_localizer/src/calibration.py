import sys
import os
import numpy as np
import cv2
import glob


class cameraCalibration():
    chessX = 9
    chessY = 6
    frames = []
    saveReady = False

    def __init__(self,debug=False,showWindow=False):
        self.debug=debug
        self.showWindow=showWindow

        if debug:
            print("cameraCalibration file has been loaded.")

    def isFileAvailable(self,filename="calibrationFile.npz"):
        if(os.path.exists(filename)):
            return True
        else:
            return False

    def loadCalibrated(self, filename="calibrationFile.npz"):
        npzfile = np.load(filename)
        sorted(npzfile.files)
        self._mtx_ = npzfile['_mtx_']
        self._dist_ = npzfile['_dist_']
        self._rvecs_ = npzfile['_rvecs_']
        self._tvecs_ = npzfile['_tvecs_']

    def addImage(self,frame):
        self.frames.append(frame)

    def saveCalibrationFile(self, filename="calibrationFile.npz"):
        if self.saveReady:
            np.savez(filename, _mtx_=self._mtx_,  _dist_=self. _dist_, _rvecs_=self._rvecs_, _tvecs_=self._tvecs_ )
        else:
            if self.debug:
                print("The calibration had nothing to save.")
            return False


    def calibrateFromFolder(self,pictureLocation="calibrationFiles/*.jpg"):
        """Load calibration from images"""
        # termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((self.chessX*self.chessY,3), np.float32)
        objp[:,:2] = np.mgrid[0:self.chessX,0:self.chessY].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.

        images = glob.glob(pictureLocation)
        if len(images)==0:
            if self.debug:
                print("No images were found. Stopping this script.")
            return False
        if self.debug:
            print("Found "+str(len(images))+" to calibrate.")

        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv2.findChessboardCorners(gray, (self.chessX,self.chessY),None)

            # If found, add object points, image points (after refining them)
            if ret == True:
                objpoints.append(objp)

                corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                imgpoints.append(corners2)

                if self.showWindow:
                    # Draw and display the corners
                    img = cv2.drawChessboardCorners(img, (self.chessX,self.chessY), corners2,ret)
                    cv2.imshow('img',img)
                    cv2.waitKey(500)

        cv2.destroyAllWindows()
        if self.debug:
            print(objpoints)
            print(imgpoints)
        self._mtx_, self._dist_, self._rvecs_, self._tvecs_ = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        self.saveReady = True

    def calibrate(self):
        """Calibrate from added frames"""
        # termination criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((chessX*chessY,3), np.float32)
        objp[:,:2] = np.mgrid[0:chessX,0:chessY].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.

        for fname in self.frame:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv2.findChessboardCorners(gray, (chessX,chessY),None)

            # If found, add object points, image points (after refining them)
            if ret == True:
                objpoints.append(objp)

                corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                imgpoints.append(corners2)

                if self.showWindow:
                    # Draw and display the corners
                    img = cv2.drawChessboardCorners(img, (chessX,chessY), corners2,ret)
                    cv2.imshow('img',img)
                    cv2.waitKey(500)

        cv2.destroyAllWindows()
        if self.debug:
            print(objpoints)
            print(imgpoints)
        self._mtx_, self._dist_, self._rvecs_, self._tvecs_ = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

    def undistortPicture(self,pictureLocation, mtx, dist):
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


if __name__=="__main__":
    calibrate = cameraCalibration(True,True)
    calibrate.calibrateFromFolder("qr_localizer/src/calibrationFiles/*.jpg")
    calibrate.saveCalibrationFile("Thomas.npz")
