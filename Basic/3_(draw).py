import cv2 as cv
import numpy as np


# -- drawing shapes -- #
blank = np.zeros((500,500,3), dtype='uint8') # uint8 is the datatype of the image\



# ---- 1. Paint the image a certain color ---- #
blank[:] = 205, 141, 122 # green color (BGR) rgb()
blank[200:300, 300:400] = 0,0,255 # red color in a certain area
# [X:Y , x:y] --> X:Y is the area where the color will be applied 
# : means the whole image i.e all the pixels

# ---- 2. Draw a Rectangle ---- #
# cv.rectangle(blank, (0,0), (blank.shape[0]//2 , blank[1]//2), (0,255,0), thickness=2) 
# blank is the image on which the rectangle will be drawn
# (0,0) is the top left corner and (250,250) is the bottom right corner i.e the diagonal of the rectangle
# thickness is the thickness of the rectangle , thickeness = CV.FILLED fills the rectangle with the color
# # thickness=-1 fills the rectangle with the color

# ---- 3. Draw a Circle ---- #
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0,0,255), thickness=-1)
# (250,250) is the center of the circle 
# 40 is the radius of the circle

# ---- 4. Draw a line ---- #
cv.line(blank, (250,250), (300,400), (255,255,255), thickness=3)
# (100,250) is the starting point of the line 
# (300,400) is the ending point of the line

# ---- 5. Write text ---- #
cv.putText(blank, 'Hello, my name is Sami!!!', (4,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# (0,225) is the starting point of the text
# cv.FONT_HERSHEY_TRIPLEX is the font of the text
# 1.0 is the scale of the text i.e the size of the text
# 2 is the thickness of the text


cv.imshow('Blank', blank)
cv.waitKey(0)