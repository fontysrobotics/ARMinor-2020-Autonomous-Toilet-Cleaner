
    pA = [float(bbox[0][0][0]),float(bbox[0][0][1])]                        ##  B------A
    pB = [float(bbox[1][0][0]),float(bbox[1][0][1])]                        ##  |      |
    pC = [float(bbox[2][0][0]),float(bbox[2][0][1])]                        ##  |      |
    pD = [float(bbox[3][0][0]),float(bbox[3][0][1])]                        ##  C------D

    magA = math.sqrt(((pA[0]-pB[0])**2)+((pA[1]-pB[1])**2))
    degA = math.atan((pA[1]-pB[1])/(pA[0]-pB[0]))
    magB = math.sqrt(((pB[0]-pC[0])**2)+((pB[1]-pC[1])**2))
    degB = math.atan((pB[1]-pC[1])/(pB[0]-pC[0]))
    #print("A",magA,degA*180/math.pi)
    #print("B",magB,degB*180/math.pi)
    angle = math.sqrt((degA-degB)**2)
    print(angle*180/math.pi)
    #cv2.line(im, tuple(bbox[0][0]), tuple(bbox[1][0]), (0,0,255), 3)
    #cv2.line(im, tuple(bbox[1][0]), tuple(bbox[2][0]), (255,0,0), 3)
    # Find the rotation and translation vectors.


##DRAW

    corner = tuple(corners[0].ravel())
    img = cv2.circle(img,tuple(corners[0].ravel()),10,(0,0,200),-1)
    img = cv2.circle(img,tuple(corners[1].ravel()),10,(0,200,0),-1)
    img = cv2.circle(img,tuple(corners[2].ravel()),10,(200,0,0),-1)
    img = cv2.circle(img,tuple(corners[3].ravel()),10,(10,10,10),-1)

    # img = cv2.circle(img,tuple(imgpts[0].ravel()),5,(200,200,0),-1)
    # img = cv2.circle(img,tuple(imgpts[1].ravel()),5,(200,200,0),-1)
    # img = cv2.circle(img,tuple(imgpts[2].ravel()),5,(200,200,0),-1)
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    #img = drawCircle(img, corners[0][0][0],corners[0][0][1],corners[1][0][0],corners[1][0][1],corners[2][0][0],corners[2][0][1])
    #img = drawCircle(img,imgpts[0][0][0],imgpts[0][0][1],imgpts[1][0][0],imgpts[1][0][1],imgpts[2][0][0],imgpts[2][0][1])
    return img

#draws an circel which goes tru 3 points
def drawCircle(img, x1,y1,x2,y2,x3,y3):
    Xm1 = (x1+x2)/2
    Ym1 = (y1+y2)/2
    Xm2 = (x1+x3)/2
    Ym2 = (y1+y3)/2
    A1 = -((x2-x1)/(y2-y1))
    A2 = -((x3-x1)/(y3-y1))
    B1 = Ym1 - (A1*Xm1)
    B2 = Ym2 - (A2*Xm2)

    xP = int((-B1+B2)/(A1-A2))
    yP = int((A1*xP) + B1)
    R =  int(math.sqrt(((x1-xP)**2) + ((y1-yP)**2)))
    img = cv2.circle(img,(xP,yP),R,(100,100,255),5)
    return img
