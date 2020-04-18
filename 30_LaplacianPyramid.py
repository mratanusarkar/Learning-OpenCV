import cv2
import numpy as np

# A Laplacian pyramid is very similar to a Gaussian pyramid but saves the difference image of the blurred versions
# between each levels. - Wikipedia
# A level in Laplacian Pyramid = Level in Gaussian Pyramid - Expanded version of it's lower
# Laplacian[i] = Gaussian[i] - PyramidUp( Gaussian[i-1] )    where, i<=0 (i.e Gaussian[i] is always PyramidDown)

img = cv2.imread("res/lena.jpg")
max_level = 3
previous_level = -1     # some out of range value!


# callback function
def nothing(x):
    print(x)


# create a black image window
cv2.namedWindow("Original Image")
cv2.namedWindow("Output Laplacian Pyramid Image")

# create track bars for level input
cv2.createTrackbar("level", "Original Image", 0, max_level, nothing)


while 1:
    cv2.imshow("Original Image", img)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # Esc key stops the code
        break

    # get the track bar values
    level = cv2.getTrackbarPos("level", "Original Image")

    if previous_level != level:     # only refresh if there is a change in level
        previous_level = level      # this removes destroyWindow bug inside infinite loop

        gaussian_i_down = img.copy()
        for i in range(level):
            gaussian_i_down = cv2.pyrDown(gaussian_i_down)
        gaussian_i_minus_1_down = cv2.pyrDown(gaussian_i_down)
        gaussian_extended = cv2.pyrUp(gaussian_i_minus_1_down)

        # Laplacian[i] = Gaussian[i] - PyramidUp( Gaussian[i-1] )   where, i<=0 (i.e Gaussian[i] is always PyramidDown)
        # or Laplacian[i] = Gaussian[i] - GaussianExtended[i]       where, GaussianExtended = PyramidUp(Gaussian[i-1])
        laplacian_i = cv2.subtract(gaussian_i_down, gaussian_extended)

        cv2.destroyWindow("Output Laplacian Pyramid Image")
        cv2.imshow("Output Laplacian Pyramid Image", laplacian_i)

cv2.destroyAllWindows()
