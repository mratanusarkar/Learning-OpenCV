import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("res/messi5.jpg", cv2.IMREAD_GRAYSCALE)


def nothing(x):
    pass


cv2.namedWindow("Canny Edge Detection")
cv2.createTrackbar("Threshold 1", "Canny Edge Detection", 0, 500, nothing)
cv2.createTrackbar("Threshold 2", "Canny Edge Detection", 500, 500, nothing)

# 3. canny edge detection
# composed of 5 steps:
# 1. Noise reduction
# 2. Gradient calculations (see previous file)
# 3. Non-maximum suppression
# 4. Double threshold
# 5. Edge Tracking by Hysteresis (th1, th2)

while True:
    th1 = cv2.getTrackbarPos("Threshold 1", "Canny Edge Detection")
    th2 = cv2.getTrackbarPos("Threshold 2", "Canny Edge Detection")

    canny = cv2.Canny(img, th1, th2)

    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edge Detection", canny)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()


