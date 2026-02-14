import cv2 as cv 
import numpy as np
img=cv.imread('photos/large.jpg')#READ IMAGE
cv.imshow('large',img) #SHOW IMAGE

#translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]]) #tranlation matrix
    dimensions=(img.shape[1],img.shape[0])#width/height
    return cv.warpAffine(img,transMat,dimensions)

#-x --> left
#-y --> up
#x --> right
#y --> down
translated=translate(img,100,100)#tranlate(img,x,y)
cv.imshow('translated', translated)

#rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0) #rotation matrix
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45) #rotate(img,angle,rotPoint)
cv.imshow('rotated', rotated)
rotated_rotated=rotate(img, -90)
cv.imshow('rotated rotated', rotated_rotated)

#resizing
resized=cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#flipping
flip=cv.flip(img,0) #0-->vertical, 1-->horizontal, -1-->both
cv.imshow('flip', flip)

#cropping
cropped=img[50:200,300:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)  

