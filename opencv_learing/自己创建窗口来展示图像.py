import numpy as np
import cv2 as cv
img = cv.imread('cat.jpg', cv.IMREAD_COLOR)
img1 = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)
cv.namedWindow('CAT3', cv.WINDOW_NORMAL)
# cv.imshow('CAT', img)
# cv.imshow('CAT1', img1)
cv.imshow('CAT3', img2)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('the_first_picture.png', img1)


