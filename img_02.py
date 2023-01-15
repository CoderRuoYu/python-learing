# 视频的基本操作
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("打开失败")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("打开失败")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("result", gray)
    if cv.waitKey(100) & 0xff == 1:
        break
cap.release()
cv.destroyAllWindows()

