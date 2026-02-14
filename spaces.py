import cv2 as cv

img=cv.imread('photos/large.jpg')#READ IMAGE
cv.imshow('large',img) #SHOW IMAGE

#bgr to gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
#the downside is you cant convert grayscale directly to hsv.

#bgr to hsv
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#bgrto l*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)
#in other formats bgr is rgb, so we can convert to rgb first and then to other formats

#bgr to rgb
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

cv.waitKey(0)
