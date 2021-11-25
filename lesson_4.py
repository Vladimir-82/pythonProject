'''
https://www.youtube.com/watch?v=cobu9gdC0Ao
rotate, mirror, transform, read and draw
'''
import cv2
import numpy as np

def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)

    mat = cv2.getRotationMatrix2D(point, angle, 0.5)
    return cv2.warpAffine(img_param, mat, (width, height))

def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))

img = cv2.imread('images/kids.jpg')
# img = cv2.flip(img, 1)
# img = rotate(img, -90)
img = transform(img, 20, 80)
cv2.imshow('kids', img)

cv2.waitKey(0)
