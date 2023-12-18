import cv2 as cv
import numpy as np

# ------- Resizing and Rescaling Images --------- #

def rescale(frame, scale=0.8):
    # Images, Videos and Live Video
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale) 
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # (src , dimensions, interpolation) 
    # interpolation is the method of how the image is resized
    # INTER_AREA is used for shrinking the image and INTER_LINEAR is used for enlarging the image

img = rescale(cv.imread('old.png'))
# cv.imshow("Plain",img)

gray = cv.cvtColor(img , cv.COLOR_RGB2GRAY)
# cv.imshow("green" , gray)


canny = cv.Canny(gray , 125 , 175)
canny = cv.dilate(canny , (7,7) , iterations = 3)

threshold , thresh = cv.threshold(gray , 150 , 255, cv.THRESH_BINARY)
# Contour is the outline of the object in the image 
# basically the outline of the edges of the image 
contour,hirerachy = cv.findContours(canny , cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
thresh_contour , thresh_hirerachy = cv.findContours(thresh , cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
# (canny , retrieval method , approximation method)
# contour is a python list of all the coordinates of the contours in the image
# hirerachy is the hirerachy of the contours i.e from the outermost contour to the innermost contour
# canny is the image on which the contours are to be found
# cv.RETR_LIST returns all the contours in the image
# instead of cv.RETR_LIST , cv.RETR_EXTERNAL can also be used which returns only the outermost contours
# cv.CHAIN_APPROX_NONE is the method of how the contours are approximated 
# instead of cv.CHAIN_APPROX_NONE , cv.CHAIN_APPROX_SIMPLE can also be used which approximates the contours
print(len(contour))

blank = np.zeros(img.shape , dtype = "uint8") # plain canvas for drawing the contours
blank[:] = 0,255,0 # green color (BGR) rgb()

cont = cv.drawContours(blank , contour , -1 , (0,0,255) , 1)
thresh_cont = cv.drawContours(blank , thresh_contour , -1 , (0,0,255) , 1)
cv.imshow("contour" , cont)
cv.imshow("thresh_contour" , thresh_cont)

cv.waitKey(0)