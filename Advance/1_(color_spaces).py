import cv2  as cv
import matplotlib.pyplot as plt


img = cv.imread("sample.png")
cv.imshow("Image", img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# BGR to HSV
# Hue Saturation Value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# BGR to LAB
# L = Lightness, A = Green to Red, B = Blue to Yellow
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# BGR to RGB
# BGR stands for Blue Green Red
# RGB stands for Red Green Blue
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)


cv.waitKey(0)