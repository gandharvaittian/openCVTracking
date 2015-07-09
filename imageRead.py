import numpy as np
import cv2

img = cv2.imread('pic.jpg',0)
cv2.imshow('image', img)
cv2.imwrite('pic_gray.jpg', img)
cv2.waitKey(0)
cv2.destroyWindow('image')
