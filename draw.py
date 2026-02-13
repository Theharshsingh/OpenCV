import cv2 as cv 
import numpy as np

blank =np.zeros((500,500,3), dtype='uint8' ) #height width color channels
cv.imshow('blank',blank)
img=cv.imread('photos/gdg.png')#READ IMAGE
cv.imshow('gdg',img)

#paint the imagea certain color
blank[:] = 0,255,0 
cv.imshow('green', blank)

#draw a rectangle
cv.rectangle(blank ,(0,0),(250,250),(0,255,0),thickness=cv.FILLED) #color and thickness
cv.imshow('rectangle', blank) #color and thickness