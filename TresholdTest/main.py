import cv2

img = cv2.imread("finger1c.pgm")

cv2.imshow("Input", img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,31,0 + cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
res = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)


cv2.imshow("Result2", res)
cv2.waitKey(0)