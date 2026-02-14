import cv2 as cv 
img=cv.imread('photos/large.jpg')#READ IMAGE
cv.imshow('large',img) #SHOW IMAGE

#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascades
canny=cv.Canny(img,125,175) #img/blurr, lower threshold, upper threshold
cv.imshow('canny edges', canny)

#dilating the image
dilated=cv.dilate(canny, (7,7), iterations=1)
cv.imshow('dilated', dilated)

#eroding the image/reverse the dilated image
eroded=cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

#resizing


cv.waitKey(0)  #k capital


