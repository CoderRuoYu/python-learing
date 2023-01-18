import numpy as np
import cv2 as cv
img = np.zeros((512, 512, 3), np.uint8)
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 2)
cv.rectangle(img, (0, 0), (60, 40), (0, 255, 0), 1)
cv.ellipse(img, (256, 256), (100, 50), 90, 0, 360, (255, 255, 255), -1)
cv.imshow("result", img)
cv.waitKey(0)
cv.destroyAllWindows()