import cv2 as cv
import numpy as np

blank=np.zeros((400,400), dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1) #draw rectangle
circle=cv.circle(blank.copy(),(200,200),200,255,-1) #draw circle

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwiseand--intersection of the two shapes
bitwise_and=cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

#bitwiseor--union of the two shapes
bitwise_or=cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)

#bitwisexor--areas that are in either the rectangle or circle but not both
bitwise_xor=cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

#bitwise_not--inverts the colors of the image
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('bitwise_not', bitwise_not)

cv.waitKey(0)