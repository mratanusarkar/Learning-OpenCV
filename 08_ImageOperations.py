import cv2

img = cv2.imread("res/messi5.jpg", -1)

print(img.shape)    # return a tuple with no of rows, columns and channels
print(img.size)     # returns total number of pixels
print(img.dtype)    # returns image datatype

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
