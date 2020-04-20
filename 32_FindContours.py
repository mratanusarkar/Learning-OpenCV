import cv2
import numpy as np

# original image
img = cv2.imread("res/opencv-logo.png")
img_copy = img.copy()

# to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# to binary
ret, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# find contours
# findContours(src=, mode=, method=, contours=None, hierarchy=None, offset=None)
contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of Contours found are:", str(len(contours)))

# draw the contours on the original image
cv2.drawContours(img_copy, contours, -1, (0, 179, 30), 3)

# for i in range(len(contours)):
#     img_copy = img.copy()
#     cv2.drawContours(img_copy, contours, i, (0, 179, 30), 3)
#     cv2.imshow("Image", img_copy)
#     cv2.waitKey(0)

cv2.imshow("Image", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: http://www.robindavid.fr/opencv-tutorial/chapter5-line-edge-and-contours-detection.html
