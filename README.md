# deltaStartup
## Intro:
This is a description document of a Ros simulation package created for the project “P3 project autonomous toilet cleaner”.
The document will explain the gazebo,  robot description, Slam_gmapping, navigation, iraLaserTools, and moveit integration packages.
A demo video can be found at: _https://youtu.be/FsXPII8OoOU_
In this link you can find the final result after implementing all the packages including octomap (_http://wiki.ros.org/octomap_): _https://youtu.be/KRT96bKQ_DQ_
## Gitrepo: 
Gazebo environment:
The environment consists of two main spaces. The first one simulates a main area (living room , office ..), the second is a main space that has access to a toilet space. The environment was created to  simulate a scenario where the robot can perform  mapping and navigation tasks.

## Robot description:
#### Models:
The package consists of two main 3D models. A design provided by the manufacturer, a holonomic platform where the arm is mounted, and 3D models of RGB, depth, and lidar sensors.

#### Ros Plugins:
The description package includes multiple ROS/Gazebo plugins:
Libgazebo_ros_planar_move : for holonomic movement simulation.
Libgazebo_ros_control,
libgazebo_joint_control,
libgazebo_joint_state_publisher,
Libgazebo_joint_trajectory_server: for publishing and controlling the arm joints state using moveit.
Ros transmissions : to simulate joints control.
Libgazebo_ros_laser: to simulate lidar sensors.
Libgazebo_ros_openni_kinect: to simulate rgb and depth cams.


#### Control files:
A .yaml file that includes configurations used further by movit to control the arm.
World file:
Includes the design of the environment.
Launch files:
Gazebo.launch: not to run, included in robot.launch
Arm.launch: not to run , included in robot.launch
Robot.launch : starts the robot and arm simulation in gazebo.
Slam_gmapping.launch : start the nodes required for gmapping.
Launch commands: 
$ roslaunch toiletcleaner robot.launch
$ roslaunch toiletcleaner slam_gmapping.launch

#### Tcnav:
The package include teb.launcn file to start the ROS nodes required to perform navigation using Teb local planner and dwa global planner.
Launch command:
$ roslaunch tcnav teb.launch

#### IRA_laser_tools:
Used to merge the data from both lidars and publish results on /Scan topic.
The nodes are started at the launch of toiletcleaner/robot.launch
TcMoveit:
The package contains moveit configuration files and a launch file to start required nodes in order to simulate moveit integration with the robot.
Launch command:
$ roslaunch tcmoveit tc.launch

## ROS lookup Table
The robot makes use of a Lookup table. It is a requestable table of information in which a server or other robots can request information about the robot such as; location, battery level, actions or anything else added.  
To implement this the following example code can be checked */something/something/something.py*
To start this the following command can be used: $ roslaunch overview overview.launch
The code has a few functions to add/update/remove functions from the lookup table

## QR-localization
The QR-localization is made up of three parts:
•	Calibration of Camera
•	QR-code creation
•	Localization
The whole project can be used using ROS or using the python source files.

### Calibration of Camera
Camera distortion is caused by a deviation in manufacturing the physical parts. The lenses inside a camera a responsible for creating a laminar image but due to very small deviations the image will be distorted. In some cases, the distortion is intentional to create a larger angle of view. Take a fish-eye lens as an example.  
The script uses a checkerboard as a reference to see deformations in the lens. The information can be saved to a file to use in later references.

#### Calibration in ROS
To begin the calibration in ROS you first put the robot in front of the calibration board. Then run the command:$ roslaunch qr_localizer calibrate.launch 
Drive the robot around while keeping the camera pointed to the calibration board. CLick on the image and press the a button to stop the calibration. Now it will calculate the camera veriables and store these to be used for the localization.

#### _From calibration import cameraCalibration_
The possible functions:
#### _calibrateFromFolder(pictureLocation)_
pictureLocation is the location of a photograph to calibrate. (use * for multiple files.) ["calibrationFiles/*.jpg"]

#### _addImage(frame)_
Append Image to be used in the calibration.

#### _calibrate()_
Calibate using appended images

#### _saveCalibrationFile(filename)_
Save a calibration with ‘filename’ for later use or use within different code. ["calibrationFile.npz"]

### QR-Creation
QR-Codes are very useful markers as they can not only be used to find orientation, but they can also contain information. Making it great to store coordinates, orientation and the QR-codes size, allowing for different size markers.
Getting started:

from qrCodeGenerator import locationCode  
QRcode = locationCode(X,Y,Z,RotationX,RotationY,RotationZ,Size,QRcodeName)  
QRcode.createQR()  
  
The X,Y,Z coordinates are used as position of the QR-code within the world.  
The rotationX,rotationY,rotationZ indicate its orientation.  
The size of the QR-code can be altered from its default of 13cm (Size is in cm)  
and the QRcodeName is the image filename.  
  
This script can also be used within for loops to create largere amounts of QRcodes.  


### QR-Detection
This is the part where the software uses the calibrated camera and the QR-codes that were made with the other script to detect its location within the envourment.  
To run the QR-Detection in the ROS base use the command: $ roslaunch qr_localizer qr_localizer.launch.  
Drive the robot around with Rviz and the set target arrow. The screen will display the cordinates of the robot.  

To get started with the software as standalone import the class from the source file:  
#### _from qrDetection import QrDetector_  
Then add an instance  
#### _detect = QrDetector(CalibrationFile='CalibrationFile.npz',mode=0,pictureFolder="QR/*.jpg",visualizeResult=False,debug=False,caneraNum=0)_
The QrDetector initial function takes multiple arguments.  
The calibration file is needed to calibrate the camera and made using a script above.  
The mode sets whether to use Camera/webcam, images from a folder or a live feed from an external source (such as ROS) [mode 0,1,2 respectively]  
The pictureFolder is only needed in mode1 and like the calibration is the image file. using an astrix will allow a whole folder.  
Visualize result will use create a window showing what computing and overlaying is being done for the calculations. (Good option for debugging)  
Debug mode is toggled to output debug info to console.  
Camera number is needed for mode 0. This is the webcam that the software will use. This needs to be changed in the case of multiple cameras.  

#### _readImage(frame)_
Read QR-detection from frame. This is used when data is being sent from another source such as with ROS.  

#### _loop()_
This starts the loop for reading the images or webcam.  

#### _closeCap()_
Closes the webcam feed. This is needed at the end of the script when using mode 0.  
