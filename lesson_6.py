"""
inversion, mask
"""
import cv2
import numpy

photo = cv2.imread('images/kids.jpg')
img = numpy.zeros(photo.shape[:2], dtype='uint8')
# img = numpy.zeros((700, 700), dtype='uint8')

circle = cv2.circle(img.copy(), (200, 300), 100, 255, -1)
rectangle = cv2.rectangle(img.copy(), (200, 250), (400, 500), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=circle)

# img = cv2.bitwise_and(circle, rectangle)
# img = cv2.bitwise_or(circle, rectangle)
# img = cv2.bitwise_xor(circle, rectangle)
# img = cv2.bitwise_not(circle, rectangle)


cv2.imshow('res', img)
cv2.waitKey(5000)