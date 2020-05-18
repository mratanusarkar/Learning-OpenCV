import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../res/smarties.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(img_gray, 5)

circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=60, param2=35, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))

for x, y, r in detected_circles[0, :]:
    cv2.circle(img, (x, y), r, (0, 255, 0), 3)
    cv2.circle(img, (x, y), 0, (100, 255, 30), 3)


cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
