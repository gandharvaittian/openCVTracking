import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)    ### BLACK IMAGE

### LINE ###
img = cv2.line(img, (0,0), (511,511), (255,0,0), 5)     ### (x1,y1), (x2,y2), BGR, Width

### RECTANGLE ###
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

### CIRCLE ###
img = cv2.circle(img, (447,63), 63, (0,0,255), -1)

### ELLIPSE ###
img = cv2.ellipse(img, (256,256), (100,50), 40, 0, 360, (105,0,300), -1)   ###centre, (majorAxis length, minorAxis length), angleOfRotaion, startAngle, endAngle, BGR, width 

### POLYGON ###
points = np.array( [ [10,5], [20,30], [70,20], [50,10] ], np.int32)
#points = points.reshape((-1,1,2))
img = cv2.polylines(img, [points], True, (0,255,255))

### TEXT ###
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'HELL HARV', (10,500), font, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
