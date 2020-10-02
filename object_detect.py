import cv2
import numpy as np
def nothing(x):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow('Track')
cv2.createTrackbar('lh','Track',0,255,nothing)
cv2.createTrackbar('ls','Track',0,255,nothing)
cv2.createTrackbar('lv','Track',0,255,nothing)
cv2.createTrackbar('hh','Track',255,255,nothing)
cv2.createTrackbar('hs','Track',255,255,nothing)
cv2.createTrackbar('hv','Track',255,255,nothing)

while True:
    #frame=cv2.imread('smarties.png')
    ret,frame=cap.read()
    #print(frame)
    lh=cv2.getTrackbarPos('lh','Track')
    ls=cv2.getTrackbarPos('ls','Track')
    lv=cv2.getTrackbarPos('lv','Track')

    hh=cv2.getTrackbarPos('hh','Track')
    hs=cv2.getTrackbarPos('hs','Track')
    hv=cv2.getTrackbarPos('hv','Track')
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #since hsv is in RGB format
    l_b=np.array([lh,ls,lv]) #lower bound
    u_b=np.array([hh,hs,hv])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k=cv2.waitKey(1)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()