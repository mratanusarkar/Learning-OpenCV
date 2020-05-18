import numpy as np
import cv2


# Display image
def show_image(image, winname="Image", width_size=800):
    h, w = image.shape[0:2]
    new_w = width_size
    new_h = int(new_w * (h / w))
    image = cv2.resize(image, (new_w, new_h))
    cv2.imshow(winname, image)
    cv2.waitKey(0)


img = cv2.imread("res/chessboard.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corner = cv2.cornerHarris(np.float32(img_gray), 2, 3, 0.04)
corner = cv2.dilate(corner, None)

# print(corner)
# print(img.shape)
# print(corner.shape)

img[corner > 0.01 * corner.max()] = [0, 0, 255]

# for x in range(0, corner.shape[0]):
#     for y in range(0, corner.shape[1]):
#         if corner[x, y] > (0.01 * corner.max()):
#             img = cv2.circle(img, (x, y), 2, (0, 0, 225), 2)

show_image(img, 'Output', 500)
# cv2.imshow("out", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
