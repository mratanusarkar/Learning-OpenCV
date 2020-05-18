import numpy as np
import cv2

# image = cv2.imread("res/lena.jpg", 1)
image = np.zeros([512, 512, 3], np.uint8)

# overwrite the image with a line
image = cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 5)
image = cv2.arrowedLine(image, (0, 255), (255, 255), (252, 190, 3), 5)
image = cv2.rectangle(image, (370, 233), (474, 400), (0, 0, 255), 5)
image = cv2.circle(image, (447, 63), 63, (0, 255, 0), -1)
polygons = np.array([
            [(60, 30), (285, 255), (350, 255), (350, 210), (474, 210), (474, 150)]
            ])
image = cv2.polylines(image, polygons, True, (0, 255, 255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, "OpenCV", (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow("output", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
