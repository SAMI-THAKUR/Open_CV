import cv2 as cv
import numpy as np

img = cv.imread("sample.png")
cv.imshow("plain" , img)

blank = np.zeros(img.shape[:2] , dtype='uint8')

b,g,r = cv.split(img)
# the function returns the blue, green and red channels of the image
print(b)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

# cv.imshow("Blue" , blue)
# cv.imshow("Green" , green)
# cv.imshow("Red" , red)

merger = cv.merge([b,g,r])
cv.imshow("Merged" , merger)

cv.waitKey(0)