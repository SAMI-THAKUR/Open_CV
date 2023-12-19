import cv2 as cv

img = cv.imread("sample.png")
# cv.imshow("plain" , img)

# Averaging
average = cv.blur(img , (7,7))
# (src , (kernel_size))
cv.imshow("Average Blur" , average)

# Gaussian Blur
gauss = cv.GaussianBlur(img , (7,7) , 0)
# (src , (kernel_size) , sigmaX)
# cv.imshow("Gaussian Blur" , gauss)

# Median Blur
median = cv.medianBlur(img , 7)
# (src , (kernel_size))
# cv.imshow("Median Blur" , median)

# Bilateral Blur --> Most effective
bilateral = cv.bilateralFilter(img, 20, 35, 125)
# (src , diameter , sigmaColor , sigmaSpace)
# diameter --> Diameter of each pixel neighborhood that is used during filtering
# sigmaColor --> sigmaColor is a parameter of the color space conversion
# sigmaSpace --> sigmaSpace is a parameter of the coordinate space conversion
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)