import cv2


def nothing(x):
    print(x)


img_path = "res/lena.jpg"
X_max, Y_max, _ = cv2.imread(img_path).shape
cv2.namedWindow("image")

cv2.createTrackbar("Value", "image", 0, 999, nothing)
cv2.createTrackbar("Size", "image", 0, 50, nothing)
cv2.createTrackbar("Thickness", "image", 0, 50, nothing)
cv2.createTrackbar("X", "image", 0, X_max, nothing)
cv2.createTrackbar("Y", "image", 0, Y_max, nothing)
cv2.createTrackbar("Color/Gray", "image", 0, 1, nothing)

while 1:
    img = cv2.imread(img_path)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Esc key
        break

    val = cv2.getTrackbarPos("Value", "image")
    size = cv2.getTrackbarPos("Size", "image")
    thickness = cv2.getTrackbarPos("Thickness", "image")
    X = cv2.getTrackbarPos("X", "image")
    Y = cv2.getTrackbarPos("Y", "image")
    CG = cv2.getTrackbarPos("Color/Gray", "image")

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, str(val), (X, Y), font, size, (0, 0, 255), thickness)

    if CG == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("image", img)


cv2.destroyAllWindows()
