import cv2
import numpy as np

# Note: Always try to keep foreground in white
imgPath = "../res/shapes.jpg"
# imgPath = "../res/smarties.png"
# imgPath = "../res/salt_and_pepper_noise_zebra.png"


def nothing(x):
    pass


cv2.namedWindow("Console")
cv2.createTrackbar("bin type", "Console", 0, 1, nothing)
cv2.createTrackbar("bin threshold", "Console", 0, 255, nothing)
cv2.createTrackbar("kernal type", "Console", 0, 2, nothing)
cv2.createTrackbar("kernal size m", "Console", 1, 10, nothing)
cv2.createTrackbar("kernal size n", "Console", 1, 10, nothing)
cv2.createTrackbar("iterations", "Console", 1, 10, nothing)


img = cv2.imread(imgPath)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


while True:
    # get values from the track bar
    bin_type = cv2.getTrackbarPos("bin type", "Console")
    thVal = cv2.getTrackbarPos("bin threshold", "Console")
    K_type = cv2.getTrackbarPos("kernal type", "Console")
    m = cv2.getTrackbarPos("kernal size m", "Console")
    n = cv2.getTrackbarPos("kernal size n", "Console")
    iteration = cv2.getTrackbarPos("iterations", "Console")
    if m == 0:
        m = 1
    if n == 0:
        n = 1

    # To Binary
    if bin_type == 0:
        _, img_bin = cv2.threshold(img_gray, thVal, 255, cv2.THRESH_BINARY_INV)
    elif bin_type == 1:
        _, img_bin = cv2.threshold(img_gray, thVal, 255, cv2.THRESH_BINARY)

    # define kernal
    kernal = np.ones((2, 2), np.uint8)
    if K_type == 0:
        kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (m, n))
    elif K_type == 1:
        kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (m, n))
    elif K_type == 2:
        kernal = cv2.getStructuringElement(cv2.MORPH_CROSS, (m, n))

    # all morphological transformations on opencv
    img_erode = cv2.erode(img_bin, kernal, iterations=iteration)
    img_dilate = cv2.dilate(img_bin, kernal, iterations=iteration)
    img_opening = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal, iterations=iteration)
    img_closing = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernal, iterations=iteration)
    img_gradient = cv2.morphologyEx(img_bin, cv2.MORPH_GRADIENT, kernal, iterations=iteration)
    img_tophat = cv2.morphologyEx(img_bin, cv2.MORPH_TOPHAT, kernal, iterations=iteration)
    img_blackhat = cv2.morphologyEx(img_bin, cv2.MORPH_BLACKHAT, kernal, iterations=iteration)
    img_hitmiss = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernal, iterations=iteration)

    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", img_gray)
    cv2.imshow("Binary Image", img_bin)
    cv2.imshow("Erosion", img_erode)
    cv2.imshow("Dilation", img_dilate)
    cv2.imshow("Opening", img_opening)
    cv2.imshow("Closing", img_closing)
    cv2.imshow("Gradient", img_gradient)
    cv2.imshow("Top Hat", img_tophat)
    cv2.imshow("Black Hat", img_blackhat)
    cv2.imshow("Hit Miss", img_hitmiss)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
