import cv2
import numpy as np

img = cv2.imread("../res/lena.jpg")
levels = 3
res_up = [img]
res_down = [img]

current_img = img
for i in range(levels):
    current_img = cv2.pyrDown(current_img)
    res_down.append(current_img)

current_img = img
for i in range(levels):
    current_img = cv2.pyrUp(current_img)
    res_up.append(current_img)

# display the images
cv2.imshow("Original Image", img)
for i in range(levels):
    cv2.imshow("Pyramid Up - " + str(i), res_up[i])
for i in range(levels):
    cv2.imshow("Pyramid Down - " + str(i), res_down[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
