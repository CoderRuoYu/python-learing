import numpy as np
import cv2 as cv
img = cv.imread("cat.jpg", cv.IMREAD_COLOR)
cv.imshow('CAT', img)
cv.waitKey(0)
cv.destroyAllWindows()