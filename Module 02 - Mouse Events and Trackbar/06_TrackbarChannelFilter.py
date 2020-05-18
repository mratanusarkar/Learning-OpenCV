import cv2
import numpy as np


def nothing(x):
    print(x)


img_path = "res/lena.jpg"
cv2.namedWindow("image")

cv2.createTrackbar("B-channel", "image", 0, 1, nothing)
cv2.createTrackbar("G-channel", "image", 0, 1, nothing)
cv2.createTrackbar("R-channel", "image", 0, 1, nothing)

while 1:
    img = cv2.imread(img_path)
    rows, columns, _ = img.shape
    b, g, r = cv2.split(img)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Esc key
        break

    b_stat = cv2.getTrackbarPos("B-channel", "image")
    g_stat = cv2.getTrackbarPos("G-channel", "image")
    r_stat = cv2.getTrackbarPos("R-channel", "image")

    if b_stat == 0:
        b = np.zeros((rows, columns), np.uint8)
    if g_stat == 0:
        g = np.zeros((rows, columns), np.uint8)
    if r_stat == 0:
        r = np.zeros((rows, columns), np.uint8)

    img = cv2.merge((b, g, r))

    cv2.imshow("image", img)

cv2.destroyAllWindows()
