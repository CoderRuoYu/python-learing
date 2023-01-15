import numpy as np
import cv2 as cv
video = cv.VideoCapture(0)
while True:
    ret, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('result', gray)
    cv.waitKey(100)
video.release()
cv.destroyAllWindows()
