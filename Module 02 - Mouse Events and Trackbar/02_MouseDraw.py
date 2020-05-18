import numpy as np
import cv2


def click_event(event, x, y, flags, params):
    # left click: image pixel coordinate
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (255, 0, 0), 3)
        cv2.imshow('image', img)


# img = cv2.imread("res/lena.jpg", -1)
img = np.zeros((720, 720, 3), np.uint8)

points = []
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
