import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("res/messi5.jpg", cv2.IMREAD_GRAYSCALE)
# define kernel
k_width = 3
k_height = 3
k_size = 3
kernel = []

# ## high pass filters (HPF): helps in finding edges in images
# gradient is a directional change in the intensity / color of an image

# 1. Laplacian derivative
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=k_size)  # supports -ve numbers totp 64 bit float
laplacian = np.uint8(np.absolute(laplacian))

# 2. Sobel X, Sobel Y, Sobel XY
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=k_size)
sobel_x = np.uint8(np.absolute(sobel_x))

sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=k_size)
sobel_y = np.uint8(np.absolute(sobel_y))

sobel_xy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=k_size)
sobel_xy = np.uint8(np.absolute(sobel_xy))

sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

# 3. canny edge detection
# pass    # check the next file...
# mean = np.mean(img)
# th1 = 0.66 * mean
# th2 = 1.33 * mean
# print(th1, th2)
canny = cv2.Canny(img, 100, 200)

# display the output
cv2.imshow("Original Image", img)
titles = ["Laplacian", "Sobel X", "Sobel Y", "Sobel XY", "Sobel X OR Y", "Canny Edge Detection"]
images = [laplacian, sobel_x, sobel_y, sobel_xy, sobel_combined, canny]

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
