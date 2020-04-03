import cv2
import numpy as np
from matplotlib import pyplot as plt

img_paths = ["res/opencv-logo.png",
             "res/lena.jpg",
             "res/lena_with_gaussian_noise.jpg",
             "res/salt_and_pepper_noise_img.png",
             "res/salt_and_pepper_noise_zebra.png",
             "res/shapes.jpg"]


def apply_homogeneous_low_pass_filters(img_path, kernel_width, kernel_height):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # define kernel
    k_width = kernel_width
    k_height = kernel_height
    kernel = []

    # homogeneous filter (2D convolution): each o/p pixel is mean of kernel neighbours
    kernel = np.ones((k_width, k_height), np.float32) / (k_width * k_height)
    convolution_2d = cv2.filter2D(img, -1, kernel)

    # ## low pass filters (LPF): helps in removing noise and blur

    # averaging algorithm: simple blur to smooth out sharp edges
    blur = cv2.blur(img, (k_width, k_height))

    # gaussian blur algorithm: the kernal has higher weight in the center and lower in the edges
    gaussian_blur = cv2.GaussianBlur(img, (k_width, k_height), 0)

    # median filter: replace each pixel with median of neighbouring pixels. Best for salt and pepper noise
    k_size = kernel_width   # should be an odd number greater than 1
    if k_size % 2 == 0:
        k_size = k_size + 1
    median = cv2.medianBlur(img, k_size)

    # preserve the edges
    bilateral = cv2.bilateralFilter(img, 9, 75, 75, )

    # ## high pass filters (HPF): helps in finding edges in images

    pass    # check the next file...

    # display the output
    titles = ["original image", "2D convolution with 5x5 kernel", "Blur", "Gaussian Blur", "Median Blur",
              "Bilateral Filter"]
    images = [img, convolution_2d, blur, gaussian_blur, median, bilateral]

    for i in range(len(images)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], "gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


for path in img_paths:
    apply_homogeneous_low_pass_filters(path, 5, 5)
