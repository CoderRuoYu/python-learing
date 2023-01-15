import numpy as np
import cv2 as cv
img = np.zeros((512, 512, 3), np.uint8)
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 2)
cv.retangle(img,(0,512),(10,10),(255,0,0),1)
cv.imshow("result", img)
cv.waitKey(0)
cv.destroyAllWindows()