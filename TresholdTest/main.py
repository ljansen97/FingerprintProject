import cv2

img = cv2.imread("finger1c.pgm")

cv2.imshow("Result", img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imshow("Result1", img)
cv2.waitKey(0)