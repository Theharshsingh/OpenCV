import cv2 as cv

capture=cv.VideoCapture('videos/d2.mp4')#READ VIDEO
#reading video frame by frame
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #press d to stop video
        break
capture.release() #release video
cv.destroyAllWindows()   

#-215 error shows when video is not read properly or ran out of frames, check path and file name of video.

