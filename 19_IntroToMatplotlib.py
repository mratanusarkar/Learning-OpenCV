import cv2
from matplotlib import pyplot as plt

# read an image
img = cv2.imread("res/lena.jpg", -1)

# cv2 way (in BGR)
cv2.imshow("image", img)

# matplotlib way (in RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

# cv2 way to close
cv2.waitKey(0)
cv2.destroyAllWindows()
