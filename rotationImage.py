import cv2
import numpy as np

img = cv2.imread('instagram.png',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),0,2)	### (___, rotationAngle, scale)

print M

dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
