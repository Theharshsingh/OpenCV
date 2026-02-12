import cv2 as cv 

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)  #variable to store dimensions of frame after rescaling

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('videos/d2.mp4')#READ VIDEO
#reading video frame by frame
while True:
    isTrue,frame=capture.read()

    frame_resized=rescaleFrame(frame , scale=0.2) #rescaling frame
    cv.imshow('video',frame)
    cv.imshow('video resized',frame_resized) #showing resized video

    if cv.waitKey(20) & 0xFF==ord('d'): #press d to stop video
        break
capture.release() #release video
cv.destroyAllWindows()
    

    #def changeres(frame,scale):  live video resizing
    #    width=int(frame.shape[1]*scale)
    #    height=int(frame.shape[0]*scale)
