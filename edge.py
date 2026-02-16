import cv2 as cv 
import numpy as np

img=cv.imread('photos/small.jpg')
cv.imshow('small',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#laplacian edge detection
lap=cv.Laplacian(gray,cv.CV_64F) #depth of the output image
lap=np.uint8(np.absolute(lap)) #convert to uint8
cv.imshow('laplacian', lap)

#sobel edge detection
sobelx=cv.Sobel(gray,cv.CV_64F,1,0) #x direction    
sobely=cv.Sobel(gray,cv.CV_64F,0,1) #y direction
combined_sobel=cv.bitwise_or(sobelx,sobely) #combine x and y direction
cv.imshow('combined sobel', combined_sobel)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)

canny=cv.Canny(gray,150,175) #threshold1, threshold2
cv.imshow('canny', canny)

cv.waitKey(0)