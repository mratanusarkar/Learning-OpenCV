import cv2
import numpy as np

# get the image
img = cv2.imread("../res/sudoku.png")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img, 60, 225, cv2.THRESH_BINARY)

# get the template
# got the coordinates using using 05_MouseEvent.py
#
#   x1, y1
# (406, 312)  (452, 310)
# (408, 356)  (454, 355)
#               x2, y2
#
# [y1: y2, x1: x2]
template = img[312:355, 406:454, :]
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
_, template_bin = cv2.threshold(template, 60, 225, cv2.THRESH_BINARY)
w, h = template_gray.shape[::-1]

# template matching
match = cv2.matchTemplate(img_bin, template_bin, cv2.TM_CCORR_NORMED)
print(match)
threshold = 0.98
loc = np.where(match >= threshold)
print(loc)

# drawing rectangles on detected template locations
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

# showing the result
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
