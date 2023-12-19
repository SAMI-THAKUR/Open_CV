import cv2 as cv
import numpy as np 

img = cv.imread("old.png")
print(img.shape)
# cv.imshow("plain" , img)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2,img.shape[0]//2), 500, 255, -1)
#cv.imshow('Circle NOT', weird)

masked = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)