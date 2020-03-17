import numpy as np
import cv2

# printing all the EVENTs available in OpenCV
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print("List of Key & Mouse events in OpenCV:")
# for event in events:
#     print(event)


def click_event(event, x, y, flags, params):
    # left click: image pixel coordinate
    if event == cv2.EVENT_LBUTTONDOWN:
        cord = '('+str(x)+', '+str(y)+')'
        print('(X,Y) =', cord)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, cord, (x, y), font, 0.5, (255,255,0), 1)
        cv2.imshow('image', img)

    # left click: image pixel coordinate
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        rgb = '(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
        print('(R,G,B) = ', rgb)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, rgb, (x, y), font, 0.5, (0, 255, 255), 1)
        cv2.imshow('image', img)

    # back to original image on click release
    if event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        img[:] = org
        cv2.imshow('image', img)


img = cv2.imread("res/lena.jpg", -1)
org = np.copy(img)
# img = np.zeros((720, 720, 3), np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
