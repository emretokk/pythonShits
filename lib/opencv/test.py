import cv2
import numpy as np

image = cv2.imread('hades.jpg')
y=0
x=0
h=100
w=200
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
cv2.waitKey(0) 