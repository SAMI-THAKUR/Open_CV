import cv2 as cv

img = cv.imread('old.png')
# cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(gray, 125, 175)
# cv.imshow('Canny Edges', canny)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
# threshold is the threshold value
# thresh is the thresholded image
# (src, min value, max value, threshold type) 
# if pixel is less than threshold value, then it is white and if it is greater than threshold value, then it is black 
# cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
# in this case, if pixel is less than threshold value, then it is black and if it is greater than threshold value, then it is white
# cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
# in this case, the threshold value is not fixed, it is calculated for smaller regions
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)