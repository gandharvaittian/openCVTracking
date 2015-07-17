import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('facebook.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

blur = cv2.blur(img,(5,5))

gaussianBlur = cv2.GaussianBlur(img,(5,5),0)

##plt.subplot(121),plt.imshow(img),plt.title('Original')
##plt.xticks([]), plt.yticks([])
##plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
##plt.xticks([]), plt.yticks([])
##plt.show()

cv2.imshow('initial', img)
cv2.imshow('final', blur)
cv2.imshow('final2', gaussianBlur)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
