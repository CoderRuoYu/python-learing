import numpy as np
import cv2 as cv

def cv_show(name, img):
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.detroyAllWindows()


img = cv.imread('R.jpg', 0)
cat = img[0:500, 0:200]
cv_show('result', cat)