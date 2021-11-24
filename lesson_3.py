'''
https://www.youtube.com/watch?v=rjZ0CxPcuV4
images
'''
import cv2
import numpy as np

photo = np.zeros((300, 400, 3), dtype='uint8')
photo[:] = 255, 255, 255

cv2.rectangle(photo, (0, photo.shape[0]//3), (photo.shape[1], 2 * photo.shape[0]//3), (196, 196, 51), thickness=cv2.FILLED)

cv2.line(photo, (0, 0), (photo.shape[1], photo.shape[0]), (109, 51, 196), thickness=2)

cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 100, (0, 51, 255), thickness=1)

cv2.putText(photo, 'Zhive Belarus', (photo.shape[1]//2 - 120, photo.shape[0]//2), cv2.FONT_HERSHEY_TRIPLEX, 1, (51, 68, 51), thickness=3)

cv2.imshow('space', photo)

cv2.waitKey(0)
