import cv2
import numpy as np

img = cv2.imread('twitter.png')

#res = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC)

height, width = img.shape[:2]
print img.shape
res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('Twitter', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
