import cv2 as cv

img=cv.imread('photos/small.jpg')
cv.imshow('small',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#simple thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY) #threshold value, max value, type of thresholding
cv.imshow('simple thresh', thresh)

threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) 
cv.imshow(' thresh_inv', thresh_inv)#inverse of simple thresholding

#adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3) #max value, adaptive method, threshold type, block size, constant
cv.imshow('adaptive thresh', adaptive_thresh)

cv.waitKey(0)