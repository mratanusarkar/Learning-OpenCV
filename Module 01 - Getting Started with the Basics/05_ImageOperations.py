import cv2

img = cv2.imread("../res/messi5.jpg", -1)
logo = cv2.imread("../res/opencv-logo.png")

print(img.shape)    # return a tuple with no of rows, columns and channels
print(img.size)     # returns total number of pixels
print(img.dtype)    # returns image datatype

# split channels and merge them back
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# roi to copy a part of the image to some other place
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# resizing both the image so that they have same shape and can be merged
print("image shape", img.shape)
print("logo shape", logo.shape)
img = cv2.resize(img, (548, 342))
logo = cv2.resize(logo, (548, 342))

# add or addWeighted may be used
# result = cv2.add(img, logo)
result = cv2.addWeighted(img, .9, logo, .1, 0)

cv2.imshow("image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
