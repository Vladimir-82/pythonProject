import cv2
import numpy as np

img = cv2.imread('images/kids.jpg')

new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con, -1, (255, 0, 0), 1)

cv2.imshow('kids', new_img)
cv2.waitKey(0)