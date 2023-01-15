import cv2 as cv
import numpy as np
def cv_show(name,img):
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


img = cv.imread('R.jpg', 0)
cv_show("result", img)
# 加载彩色图像
# img = cv.imread('R.jpg', 0)
# 展示图像
# cv.imshow('first_img', img)
# # 按任意键结束图像
# cv.waitKey(0)
# 销毁所有窗口
# cv.destroyAllWindows()

# print(img.shape)

