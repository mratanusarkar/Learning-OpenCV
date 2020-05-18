import cv2

img = cv2.imread("res/gradient.png", 0)
thVal = 127

# applying threshold techniques available in opencv
_, th0 = cv2.threshold(img, thVal, 225, cv2.THRESH_BINARY)
_, th1 = cv2.threshold(img, thVal, 225, cv2.THRESH_BINARY_INV)
_, th2 = cv2.threshold(img, thVal, 225, cv2.THRESH_TOZERO)
_, th3 = cv2.threshold(img, thVal, 225, cv2.THRESH_TOZERO_INV)
_, th4 = cv2.threshold(img, thVal, 225, cv2.THRESH_TRUNC)
_, th5 = cv2.threshold(img, thVal, 225, cv2.THRESH_TRIANGLE)
_, th6 = cv2.threshold(img, thVal, 225, cv2.THRESH_MASK)
_, th7 = cv2.threshold(img, thVal, 225, cv2.THRESH_OTSU)
_, th8 = cv2.threshold(img, thVal, 225, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
_, th9 = cv2.threshold(img, thVal, 225, cv2.ADAPTIVE_THRESH_MEAN_C)

# viewing the results
cv2.imshow("Original Image", img)
cv2.imshow("BINARY", th0)
cv2.imshow("BINARY_INV", th1)
cv2.imshow("TOZERO", th2)
cv2.imshow("TOZERO_INV", th3)
cv2.imshow("TRUNC", th4)
cv2.imshow("TRIANGLE", th5)
cv2.imshow("MASK", th6)
cv2.imshow("OTSU", th7)
cv2.imshow("ADAPTIVE_GAUSSIAN_C", th8)
cv2.imshow("ADAPTIVE_MEAN_C", th9)

cv2.waitKey(0)
cv2.destroyAllWindows()
