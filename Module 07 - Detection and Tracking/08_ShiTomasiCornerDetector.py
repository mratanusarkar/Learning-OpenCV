import numpy as np
import cv2

img = cv2.imread("../res/pic1.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Tomasi = img.copy()
Harris = img.copy()

# Shi Tomasi Corner Detection
corners = cv2.goodFeaturesToTrack(img_gray, 25, 0.01, 10)
corners = np.int64(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(Tomasi, (x, y), 3, (0, 0, 255), -1)

# Harris Corner Detection (from previous code for comparison)
corner = cv2.cornerHarris(np.float32(img_gray), 2, 3, 0.04)
corner = cv2.dilate(corner, None)
Harris[corner > 0.01 * corner.max()] = [255, 0, 0]

# display the results
cv2.imshow("Original Image", img)
cv2.imshow("Shi Tomasi Corner Detection", Tomasi)
cv2.imshow("Harris Corner Detection", Harris)
cv2.waitKey(0)
cv2.destroyAllWindows()
