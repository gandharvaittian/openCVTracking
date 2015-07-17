import cv2
import numpy as np

img = cv2.imread('facebook.png')
rows,cols,ch = [700,700,3]#img.shape

pts1 = np.float32([[0,0],[200,0],[0,200]])
pts2 = np.float32([[0,100],[200,50],[100,250]])

print pts1, pts2
M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

#plt.subplot(121),plt.imshow(img),plt.title('Input')
#plt.subplot(122),plt.imshow(dst),plt.title('Output')
#plt.show()

cv2.imshow('final', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
