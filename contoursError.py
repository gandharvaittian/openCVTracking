import numpy as np
import cv2

img = cv2.imread('star.jpg')
img = cv2.resize(img,None,fx=1, fy=1, interpolation = cv2.INTER_CUBIC)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
imgray = cv2.convexHull(cnt)
M = cv2.moments(cnt)
imgray = cv2.drawContours(imgray, contours, -1, (0,255,0), 3)
print M
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = cv2.contourArea(cnt)

perimeter = cv2.arcLength(cnt, True)

print "Centroid:",cx, cy
print ("Area: %s" % (area))
print ("Perimeter: %s" % (perimeter))

print imgray
cv2.imshow('Contour', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows
