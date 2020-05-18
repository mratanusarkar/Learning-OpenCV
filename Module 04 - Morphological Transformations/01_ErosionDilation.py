import cv2
import numpy as np
from matplotlib import pyplot as plt

# Note: Always try to keep foreground in white
img = cv2.imread("../res/smarties.png")
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

# define kernal
kernal = np.ones((2, 2), np.uint8)

# Erosion
img_erode = cv2.erode(img_bin, kernal, iterations=2)

# Dilation
img_dilate = cv2.dilate(img_bin, kernal, iterations=2)

titles = ["original image", "binary", "Erosion", "Dilation"]
images = [img_RGB, img_bin, img_erode, img_dilate]

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

