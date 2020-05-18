import numpy as np
import cv2


def click_event(event, x, y, flags, params):

    # left click: image pixel coordinate
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        # cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        color_image = np.zeros((128, 128, 3), np.uint8)
        color_image[:] = [blue, green, red]

        rgb = '(' + str(red) + ',' + str(green) + ',' + str(blue) + ')'
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(color_image, rgb, (10, 30), font, 0.5, (255-int(blue), 255-int(green), 255-int(red)), 1)
        cv2.imshow('image', img)

        cv2.imshow('color', color_image)


img = cv2.imread("../res/lena.jpg", -1)
# img = np.zeros((720, 720, 3), np.uint8)

points = []
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
