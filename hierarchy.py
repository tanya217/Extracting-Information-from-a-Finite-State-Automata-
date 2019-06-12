import numpy as np
import cv2
im = cv2.imread('dfa1.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 187, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
	cnt=contours[i]
	k=cv2.isContourConvex(cnt)
	print(k)
	(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
	print(angle)

'''cnt=contours[0]
print(cnt)
M=cv2.moments(cnt)
area=cv2.contourArea(cnt)
print(area)
perimeter=cv2.arcLength(cnt,True)
print(perimeter)'''


'''epsilon = cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)'''
cv2.imwrite("ot.jpeg",im2)
cv2.waitKey()

