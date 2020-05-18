import cv2
import numpy as np

max_level = 6

# ---------------------------------------------------------------------------------------------------------------------
# In order to Blend two images using Image Pyramid technique, simply follow these 5 steps:
# ---------------------------------------------------------------------------------------------------------------------
# 1) Load the two images. Example: here "apple.jpg" and "orange.jpg".
# 2) Find the Gaussian Pyramids for both the images (in this particular example, number of levels is 6).
# 3) From Gaussian Pyramids, find their Laplacian Pyramids.
# 4) Now join the left half of the first image with the right half of the second in each levels of Laplacian Pyramids.
# 5) Finally from this joint image pyramids, reconstruct the original image.
# ---------------------------------------------------------------------------------------------------------------------

# Step 1:
# load both the images
apple_img = cv2.imread("../res/apple.jpg")
orange_img = cv2.imread("../res/orange.jpg")
print("apple image shape", apple_img.shape)
print("orange image shape", orange_img.shape)

# let's see how it looks by stacking half of both the images side by side
cols, rows, chs = apple_img.shape
apple_orange = np.hstack((apple_img[:, :int(cols/2), :], orange_img[:, int(cols/2):, :]))


# step 2
# generate Gaussian pyramid for apple
layer = apple_img.copy()
gaussian_pyramid_apple = [layer]
for level in range(max_level):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_apple.append(layer)

# generate Gaussian pyramid for orange
layer = orange_img.copy()
gaussian_pyramid_orange = [layer]
for level in range(max_level):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_orange.append(layer)


# step 3
# generate Laplacian pyramid for apple
laplacian_pyramid_apple = [gaussian_pyramid_apple[(max_level-1)]]
for level in range((max_level-1), 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_apple[level])    # pyrUp at i -> blurred image at (i-1)
    laplacian = cv2.subtract(gaussian_pyramid_apple[level - 1], gaussian_extended)  # gauss (i-1) - blurred gauss (i-1)
    laplacian_pyramid_apple.append(laplacian)

# generate Laplacian pyramid for orange
laplacian_pyramid_orange = [gaussian_pyramid_orange[(max_level-1)]]
for level in range((max_level-1), 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_orange[level])    # pyrUp at i -> blurred image at (i-1)
    laplacian = cv2.subtract(gaussian_pyramid_orange[level - 1], gaussian_extended)  # gauss (i-1) - blurred gauss (i-1)
    laplacian_pyramid_orange.append(laplacian)


# step 4
# join left half of apple with right half of orange in each level of the laplacian pyramids
laplacian_pyramid_apple_orange = []
n = 0
# for i in range(max_level):
#     n += 1
#     laplacian = np.hstack((laplacian_pyramid_apple[i][:, 0:int(cols/2)],laplacian_pyramid_orange[i][:, int(cols/2):]))
#     laplacian_pyramid_apple_orange.append(laplacian)
for apple_lap, orange_lap in zip(laplacian_pyramid_apple, laplacian_pyramid_orange):
    n += 1
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    laplacian_pyramid_apple_orange.append(laplacian)


# step 5
# reconstruct the final image
apple_orange_reconstruct = laplacian_pyramid_apple_orange[0]    # remember, at 0th index we had original image halves
for i in range(1, max_level):                                   # these are the laplacian stacked halves
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_reconstruct, laplacian_pyramid_apple_orange[i])


# # uncomment to test and understand the steps and what's going on in each layer
# index = 1   # change index from [0 to (max_level-1)] and see what happens!
# cv2.imshow("gp_a", gaussian_pyramid_apple[index])
# cv2.imshow("gp_o", gaussian_pyramid_orange[index])
# cv2.imshow("lp_a", laplacian_pyramid_apple[index])
# cv2.imshow("lp_o", laplacian_pyramid_apple_orange[index])
# cv2.imshow("lp_ao", laplacian_pyramid_apple_orange[index])

# display the images
cv2.imshow("apple", apple_img)
cv2.imshow("orange", orange_img)
cv2.imshow("1/2 apple 1/2 orange", apple_orange)
cv2.imshow("reconstructed blended image from laplacian pyramids", apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()
