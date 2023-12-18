import cv2 as cv

capture = cv.VideoCapture("csi.mp4")
# 0 is the default webcam
# 1 is the second webcam
# 2 is the third webcam

# ------- Resizing and Rescaling Images --------- #
def rescale(frame, scale=0.4):
    # Images, Videos and Live Video
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale) 
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # (src , dimensions, interpolation) 
    # interpolation is the method of how the image is resized
    # INTER_AREA is used for shrinking the image and INTER_LINEAR is used for enlarging the image

def Res(width, height):
    # Live Video --> web cam
    capture.set(10, width) # 3 is the width
    capture.set(10, height) # 4 is the height

Res(500, 500)

while True:
    isTrue, frame = capture.read() # isTrue is a boolean value which tells us if the video is being read correctly or not
    r_frame = rescale(frame)
    cv.imshow('Video', r_frame)

    if cv.waitKey(5) & 0xFF==ord('d'):
        # 20 is the delay means that the video will be played at 50 fps , to increase the fps decrease the delay
        # 0xFF==ord('d') is the key to stop the video i.e pressing 'd' will stop the video
        break

capture.release() # releases the capture
cv.destroyAllWindows() # destroys all the windows
# cv.waitKey(0)