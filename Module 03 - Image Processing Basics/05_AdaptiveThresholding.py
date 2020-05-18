import cv2

img = cv2.imread("res/sudoku.png", 0)

# applying adaptive threshold techniques available in opencv
th0 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# viewing the results
cv2.imshow("Original Image", img)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th0)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th1)

cv2.waitKey(0)
cv2.destroyAllWindows()
