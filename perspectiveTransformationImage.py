import cv2
import numpy as np

img = cv2.imread('instagram.png')
rows,cols,ch = img.shape

pts1 = np.float32([[0,0],[512,0],[28,387],[389,390]])
pts2 = np.float32([[0,100],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

#plt.subplot(121),plt.imshow(img),plt.title('Input')
#plt.subplot(122),plt.imshow(dst),plt.title('Output')
#plt.show()

cv2.imshow('final', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
