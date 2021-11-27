'''
https://www.youtube.com/watch?v=1biHdzEkAJg
'''
import cv2

img = cv2.imread('images/image2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('videos/faces.xml')

result = faces.detectMultiScale(img, scaleFactor=1, minNeighbors=3)

for (x, y, w, h) in result:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)

cv2.imshow('res', img)
cv2.waitKey(0)