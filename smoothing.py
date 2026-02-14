import cv2 as cv

img=cv.imread('photos/large.jpg')#READ IMAGE
cv.imshow('large',img) #SHOW IMAGE

#averaging
average=cv.blur(img,(3,3)) #img, kernel size high  the kernel size=high blurrier the image
cv.imshow('average blur', average)

#gaussian blur
gauss=cv.GaussianBlur(img,(3,3),0) #img, kernel size, sigmaX(how much the image is blurred in x direction)
cv.imshow('gaussian blur', gauss)

#median blur
median=cv.medianBlur(img,3) #img, kernel size (must be odd)
cv.imshow('median blur', median)

#bilateral blur
bilateral=cv.bilateralFilter(img, 10, 35, 25) #img, diameter of each pixel neighborhood, sigmaColor, sigmaSpace
cv.imshow('bilateral blur', bilateral)

cv.waitKey(0)