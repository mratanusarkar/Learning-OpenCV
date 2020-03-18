import cv2
import numpy as np

# create images to test bit-wise-operators in opencv
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (187, 0), (313, 126), (255, 255, 255), -1)

img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (0, 0), (250, 250), (255, 255, 255), -1)

# let's see the two test images
cv2.imshow("image1: white square in top-middle", img1)
cv2.imshow("image2: half white half black", img2)

# let's try AND, OR and XOR operations
img1_AND_img2 = cv2.bitwise_and(img1, img2)
img1_OR_img2 = cv2.bitwise_or(img1, img2)
img1_XOR_img2 = cv2.bitwise_xor(img1, img2)

cv2.imshow("image1 AND image2", img1_AND_img2)
cv2.imshow("image1 OR  image2", img1_OR_img2)
cv2.imshow("image1 XOR image2", img1_XOR_img2)

# let's try NOT operations
NOT_img1 = cv2.bitwise_not(img1)
NOT_img2 = cv2.bitwise_not(img2)

cv2.imshow("image1 NOT (complement)", NOT_img1)
cv2.imshow("image2 NOT (complement)", NOT_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
