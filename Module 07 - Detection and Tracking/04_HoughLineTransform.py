import cv2
import numpy as np

img = cv2.imread("../res/sudoku.png", -1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# For Hough Line Transform, follow the following steps:
# 1. Edge Detection (canny)
# 2. Mapping of Edge points to the Hough Space and store in an accumulator
# 3. Interpret the accumulator to yield lines of infinite length
# 4. Convert infinite lines to finite lines

# step 1:
edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)

# step 2:
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for line in lines:
    # step 3:
    r, theta = line[0]

    # polar to cartesian conversion
    x0 = r * np.cos(theta)
    y0 = r * np.sin(theta)

    # step 4:
    x1 = int(x0 + 1000 * -np.sin(theta))
    y1 = int(y0 + 1000 * np.cos(theta))

    x2 = int(x0 - 1000 * -np.sin(theta))
    y2 = int(y0 - 1000 * np.cos(theta))

    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
