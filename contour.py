import numpy as np
import cv2
import imutils
im = cv2.imread('dfa1.png')
im2 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(im2, 0, 150, 0)
#im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
im2,cnts,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #cv2.RETR_EXTERNAL
#cnts = cnts[0] if imutils.is_cv2() else cnts[1]

for i in range(len(cnts)):
	#print("length",len(cnts[i]))
	c=cnts[i]
	#print(c)
	if(len(cnts[i])>=5):
		(x,y),(MA,ma),angle = cv2.fitEllipse(c)
		print(angle)
		if(angle>50):

			extLeft = tuple(c[c[:, :, 0].argmin()][0])
			extRight = tuple(c[c[:, :, 0].argmax()][0])
			extTop = tuple(c[c[:, :, 1].argmin()][0])
			extBot = tuple(c[c[:, :, 1].argmax()][0])


			cv2.drawContours(im, [c], -1, (0, 255, 255), 2)
			cv2.circle(im, extLeft, 8, (0, 0, 255), -1)
			cv2.circle(im, extRight, 8, (0, 255, 0), -1)
			cv2.circle(im, extTop, 8, (255, 0, 0), -1)
			cv2.circle(im, extBot, 8, (255, 255, 0), -1)

		

'''cnt=contours[0]
print(cnt)
M=cv2.moments(cnt)
area=cv2.contourArea(cnt)
print(area)
perimeter=cv2.arcLength(cnt,True)
print(perimeter)'''


'''epsilon = cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)'''
'''crop_img = im2[290:400,144:600]'''
cv2.imshow("ot",im)
cv2.waitKey()
