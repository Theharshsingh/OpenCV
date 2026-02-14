import cv2 as cv
import numpy as np

img=cv.imread('photos/gdg.png')#READ IMAGE
cv.imshow('gdg',img)

blank=np.zeros(img.shape ,dtype='uint8') #black image
cv.imshow('blank', blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur', blur) 

canny=cv.Canny(gray,125,175) 
cv.imshow('canny edges', canny)

ret,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY) #thresholding
cv.imshow('thresh', thresh)

contours, hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#RETR_LIST --> all contours, RETR_EXTERNAL --> external contours, RETR_TREE --> all contours and reconstructs a full hierarchy of nested contours.
print(f'{len(contours)} contours found!')

cv.drawContours(blank,contours,-1,(0,0,255),1) #draw contours on blank image
cv.imshow('contours drawn', blank)

cv.waitKey(0)