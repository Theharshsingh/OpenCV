import cv2 as cv
import numpy as np

img=cv.imread('photos/large.jpg')
cv.imshow('large',img)

blank=np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

mask=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1) #draw circle mask
cv.imshow('mask', mask)

masked=cv.bitwise_and(img,img,mask=mask) #apply mask to image
cv.imshow('masked', masked)

cv.waitKey(0)