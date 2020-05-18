import cv2
import numpy as np
from matplotlib import pyplot as plt

# Note: Always try to keep foreground in white
img = cv2.imread("res/shapes.jpg")
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

# define kernal
kernal = np.ones((2, 2), np.uint8)

# all morphological transformations on opencv
img_erode = cv2.erode(img_bin, kernal, iterations=2)
img_dilate = cv2.dilate(img_bin, kernal, iterations=2)
img_opening = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal)
img_closing = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernal)
img_gradient = cv2.morphologyEx(img_bin, cv2.MORPH_GRADIENT, kernal)
img_tophat = cv2.morphologyEx(img_bin, cv2.MORPH_TOPHAT, kernal)
img_blackhat = cv2.morphologyEx(img_bin, cv2.MORPH_BLACKHAT, kernal)
img_hitmiss = cv2.morphologyEx(img_bin, cv2.MORPH_HITMISS, kernal)

titles = ["original image", "binary", "Erosion", "Dilation", "Opening", "Closing", "Gradient", "Top Hat", "Black Hat", "Hit Miss"]
images = [img_RGB, img_bin, img_erode, img_dilate, img_opening, img_closing, img_gradient, img_tophat, img_blackhat, img_hitmiss]

for i in range(len(images)):
    plt.subplot(2, 5, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

