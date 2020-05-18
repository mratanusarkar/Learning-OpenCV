import cv2
import numpy as np

img = cv2.imread("../res/sudoku.png", -1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# step 1:
edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)

# step 2:
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

# step 3:
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
