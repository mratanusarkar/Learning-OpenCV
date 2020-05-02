import cv2
import numpy as np
from matplotlib import pyplot as plt

img_black = np.zeros((200, 200), np.uint8)

img_add_white = img_black.copy()
img_add_white = cv2.rectangle(img_add_white, (0, 100), (200, 200), 255, -1)

img_add_gray = img_add_white.copy()
img_add_gray = cv2.rectangle(img_add_gray, (0, 50), (100, 100), 127, -1)

img_lena_gray = cv2.imread("res/lena.jpg", cv2.IMREAD_GRAYSCALE)
img_lena = plt.imread("res/lena.jpg", -1)
img_messi = plt.imread("res/messi5.jpg", -1)

img_r = plt.imread("res/red225x225.jpg", -1)
img_g = plt.imread("res/green225x225.jpg", -1)
img_b = plt.imread("res/blue225x225.jpg", -1)
img_rgb = plt.imread("res/RGB_400x400.png", -1)

# all images in RGB format
images = [
    img_black,
    img_add_white,
    img_add_gray,
    img_lena_gray,
    img_r,
    img_g,
    img_b,
    img_rgb,
    img_lena,
    img_messi
]

titles = [
    str(img_black.shape) + " Black - 2D",
    str(img_add_white.shape) + " 1/2 Black 1/2 White - 2D",
    str(img_add_gray.shape) + " Black, White, Gray - 2D",
    str(img_lena_gray.shape) + " lena.jpg Grayscale - 2D",
    str(img_r.shape) + " Red template - 3D",
    str(img_g.shape) + " Green template - 3D",
    str(img_b.shape) + " Blue template - 3D",
    str(img_rgb.shape) + " RGB template - 4D",
    str(img_lena.shape) + " lena.jpg Original - 3D",
    str(img_messi.shape) + " messi5.jpg Original - 3D"
]

for i, image in enumerate(images):
    plt.close("all")
    plt.subplot(1, 2, 1)
    plt.imshow(image, "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 2, 2)
    if len(image.shape) < 3:
        plt.hist(image.ravel(), 256, [0, 256])
    elif len(image.shape) == 3:
        if image.shape[2] == 3:
            r, g, b = cv2.split(image)
        elif image.shape[2] == 4:
            r, g, b, a = cv2.split(image)
            plt.hist(a.ravel(), 256, [0, 256], color="gray", lw=0, alpha=0.5, label='alpha')
        else:
            print("unknown number of channels in the image")
            r, g, b, a = [], [], [], []
            pass
        plt.hist(r.ravel(), 256, [0, 256], color="red", lw=0, alpha=0.5, label='R')
        plt.hist(g.ravel(), 256, [0, 256], color="green", lw=0, alpha=0.5, label='G')
        plt.hist(b.ravel(), 256, [0, 256], color="blue", lw=0, alpha=0.5, label='B')
        plt.legend(loc='upper right')
    else:
        print("unknown image format")
        plt.hist(image.ravel(), 256, [0, 256])
    plt.title("Histogram")

    plt.get_current_fig_manager().window.showMaximized()
    plt.show()
