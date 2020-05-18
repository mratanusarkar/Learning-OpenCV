import cv2
import numpy as np

img = cv2.imread("../res/lena.jpg")
max_level = 3
previous_level = max_level + 1     # some out of range value!


# callback function
def nothing(x):
    print(x)


# create a black image window
cv2.namedWindow("Original Image")
cv2.namedWindow("Output Gaussian Pyramid Image")

# create track bars for level input
Min = 0
Mid = max_level
Max = max_level * 2
# (-max_level ... Zero ... +max_level)
cv2.createTrackbar("level", "Original Image", Mid, Max, nothing)


while 1:
    cv2.imshow("Original Image", img)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # Esc key stops the code
        break

    # get the track bar values
    level = cv2.getTrackbarPos("level", "Original Image")

    # rescale the values from (-max_level ... Zero ... +max_level)
    level -= max_level

    if previous_level != level:     # only refresh if there is a change in level
        previous_level = level      # this removes destroyWindow bug inside infinite loop

        if level < 0:
            level *= -1     # take the magnitude
            layer = img.copy()
            for i in range(level):
                layer = cv2.pyrDown(layer)
            cv2.destroyWindow("Output Gaussian Pyramid Image")
            cv2.imshow("Output Gaussian Pyramid Image", layer)
        elif level > 0:
            layer = img.copy()
            for i in range(max_level):
                layer = cv2.pyrUp(layer)
            cv2.destroyWindow("Output Gaussian Pyramid Image")
            cv2.imshow("Output Gaussian Pyramid Image", layer)
        else:
            layer = img.copy()
            cv2.destroyWindow("Output Gaussian Pyramid Image")
            cv2.imshow("Output Gaussian Pyramid Image", layer)

cv2.destroyAllWindows()
