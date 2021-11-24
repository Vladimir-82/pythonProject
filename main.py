import cv2
import numpy as np


img = cv2.imread('images/kids.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
img = cv2.Canny(img, 100, 100)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

# new_img = cv2.resize(img, (300, 300))
cv2.imshow('i love my kids', img)



cv2.waitKey(0)

# cap = cv2.VideoCapture('videos/Mountain.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow('Res', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print(cv2.waitKey(1) & 0xFF)
#         break

