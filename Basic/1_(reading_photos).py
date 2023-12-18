#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('thor.png')
# cv.imshow('Thor', img) --> displays the image and "thor" is the name of the window

# print(img.shape) # (height, width, channels) --> channels are the BGR values


# ------- Resizing and Rescaling Images --------- #

def rescale(frame, scale=0.4):
    # Images, Videos and Live Video
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale) 
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # (src , dimensions, interpolation) 
    # interpolation is the method of how the image is resized
    # INTER_AREA is used for shrinking the image and INTER_LINEAR is used for enlarging the image

resized_image = rescale(img)
# cv.imshow('Resized', resized_image)

# ------- Drawing Shapes and Text on Images --------- #
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# ---- Blur ---- #
blur = rescale(cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT))
# (7,7) is the kernel size and cv.BORDER_DEFAULT is the border type
# cv.imshow('Blur', blur)



# ---- Edge Cascade ---- #
canny = rescale(cv.Canny(img, 125, 175))
# edge detection is done using canny edge detection
# 125 is the threshold1 and 175 is the threshold2 i.e the lower and upper threshold
cv.imshow('Canny Edges', canny)


# ---- Dilating the image ---- #
# Dilating is used to increase the thickness of the edges
dilated = rescale(cv.dilate(canny, (7,7), iterations=3))
# (7,7) is the kernel size and iterations is the number of times the image is dilated
cv.imshow('Dilated', dilated)


# ---- Eroding ---- #
# Eroding means to decrease the thickness of the edges
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# # Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# ---- Cropping ---- #
cropped = rescale(img[50:1000, 200:4000])
# [X:Y, x:y] --> X:Y is the height and x:y is the width
cv.imshow('Cropped', cropped)

cv.waitKey(0)