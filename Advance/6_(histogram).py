#pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('old.png')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow('Mask', masked)

# GRayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )
# return a list of 256 values (0-255) of the number of pixels in the image that have that value
# 0 = black, 255 = white

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Colour Histogram

# plt.figure()
# plt.title('Colour Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# colors = ('b', 'g', 'r')
# for i,col in enumerate(colors):
#     hist = cv.calcHist([img], [i], mask, [256], [0,256])
#     plt.plot(hist, color=col)
#     plt.xlim([0,256])

# plt.show()

cv.waitKey(0)