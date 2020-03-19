import cv2
import numpy as np


# callback function
def nothing(x):
    print(x)


# create a black image window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("image")

# create track bars with names B, G, R and Switch
cv2.createTrackbar("B", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("Switch", "image", 0, 1, nothing)

while 1:
    cv2.imshow("image", img)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # Esc key stops the code
        break

    # get the track bar values
    b = cv2.getTrackbarPos("B", "image")
    g = cv2.getTrackbarPos("G", "image")
    r = cv2.getTrackbarPos("R", "image")
    s = cv2.getTrackbarPos("Switch", "image")

    # switch on to show BGR combo color, else show black
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
