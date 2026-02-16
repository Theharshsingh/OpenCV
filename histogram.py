import cv2 as cv


img=cv.imread('photos/small.jpg')
cv.imshow('small',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#grayscale histogram
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256]) #[images], [channels], [mask], [bins], [range]

#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()
cv.imshow('gray_histogram', gray_hist)



cv.waitKey(0)