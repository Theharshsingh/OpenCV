import cv2 as cv

img=cv.imread('photos/g1.jpg')
cv.imshow('group',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray person', gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)#minNeighbors=4 means that the rectangle should have 4 neighbors to be considered a face, scaleFactor=1.1 means that the image is reduced by 10% at each image scale

print(f'Number of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0), thickness=2 )

cv.imshow('Detected Faces', img)
cv.waitKey(0)