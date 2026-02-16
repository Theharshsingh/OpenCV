import cv2 as cv

img=cv.imread('photos/small.jpg')
cv.imshow('small',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#simple thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY) #threshold value, max value, type of thresholding
cv.imshow('simple thresh', thresh)

cv.waitKey(0)