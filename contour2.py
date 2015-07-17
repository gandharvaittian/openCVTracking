
import numpy as np
import cv2

img = cv2.imread('bolt.jpg')
img = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

##############################################################
### STRAIGHT BOUNDING RECTANGLE###
##################################
x,y,w,h = cv2.boundingRect(cnt)
straightRect = cv2.rectangle(imgray,(x,y),(x+w,y+h),(0,255,0),2)

##############################################################
##############################################################
### ROTATED RECTANGLE ###
#########################
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
rotatedRect = cv2.drawContours(imgray,[box],0,(0,0,255),2)

##############################################################
##############################################################
### MIN ENCLOSING CIRCLE ###
############################
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
minEnclosingCirc = cv2.circle(imgray,center,radius,(0,255,0),2)

#############################################################
#############################################################
### ELLIPSE CONTOUR ###
#######################
ellipse = cv2.fitEllipse(cnt)
ellipseContour = cv2.ellipse(imgray,ellipse,(0,255,0),2)

#############################################################
#cv2.namedWindow("Straight Rectangle", cv2.WINDOW_NORMAL)
cv2.imshow("Straight Rectangle", straightRect)
#cv2.namedWindow("Rotated Rectangle", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated Rectangle", rotatedRect)
#cv2.namedWindow("Min Enclosing Circle", cv2.WINDOW_NORMAL)
cv2.imshow("Min Enclosing Circle", minEnclosingCirc)
cv2.imshow("Ellipse Contour", ellipseContour)
cv2.waitKey(0)
cv2.destroyAllWindows
