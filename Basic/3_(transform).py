#pylint:disable=no-member

import cv2 as cv
import numpy as np


def rescale(frame, scale=0.4):
    # Images, Videos and Live Video
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale) 
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # (src , dimensions, interpolation) 
    # interpolation is the method of how the image is resized
    # INTER_AREA is used for shrinking the image and INTER_LINEAR is used for enlarging the image

img = rescale(cv.imread('thor.png'))
# cv.imshow('plain', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) 
    # float32 is the datatype of the matrix and the matrix is a 2x3 matrix
    # in the matrix, the first row is for the x direction and the second row is for the y direction
    # float32 takes in a list of lists and converts it into a matrix
    # 1,0,x --> x is the number of pixels to be translated in the x direction
    # 0,1,y --> y is the number of pixels to be translated in the y direction
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions) # (src, transformation matrix, dimensions)
    # warpAffine is the function which translates the image

# -x --> Left
# -y --> Up
# +x --> Right
# +y --> Down

translated = translate(img, -100, 100)
# cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # (center, angle, scale)
    # rotMat is the rotation matrix of the image i.e the matrix by which the image is rotated
    # rotPoint is the point around which the image is rotated
    # angle is the angle by which the image is rotated
    # scale is the scale of the image i.e the size of the image
    dimensions = (width,height) # creating a tuple of the dimensions of the image

    return cv.warpAffine(img, rotMat, dimensions)
    # warpAffine is the function which rotates the image

rotated = rotate(img, -45)
# cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
# cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# interpolation is the method of how the image is resized 
# INTER_CUBIC is used for enlarging the image
# INTER_AREA is used for shrinking the image
# cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 1)
# (src, flipcode) --> flipcode is the code by which the image is flipped
# 0 --> flipping the image vertically
# 1 --> flipping the image horizontally
# -1 --> flipping the image both vertically and horizontally
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
# cv.imshow('Cropped', cropped)


cv.waitKey(0)