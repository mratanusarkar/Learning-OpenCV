import cv2

# enter the path to the image
imgPath = "res/sudoku.png"  # "res/gradient.png"


def nothing(x):
    pass


cv2.namedWindow("Original Image")
cv2.namedWindow("Threshold Image")
cv2.createTrackbar("Value", "Threshold Image", 0, 255, nothing)
cv2.createTrackbar("Technique", "Threshold Image", 0, 4, nothing)


while True:
    # get image
    img = cv2.imread(imgPath, 0)

    # get values from the track bar
    thVal = cv2.getTrackbarPos("Value", "Threshold Image")
    thChoice = cv2.getTrackbarPos("Technique", "Threshold Image")

    text = ""

    if thChoice == 0:
        _, th = cv2.threshold(img, thVal, 225, cv2.THRESH_BINARY)
        text = "BINARY"
    elif thChoice == 1:
        _, th = cv2.threshold(img, thVal, 225, cv2.THRESH_BINARY_INV)
        text = "BINARY INV"
    elif thChoice == 2:
        _, th = cv2.threshold(img, thVal, 225, cv2.THRESH_TOZERO)
        text = "TO ZERO"
    elif thChoice == 3:
        _, th = cv2.threshold(img, thVal, 225, cv2.THRESH_TOZERO_INV)
        text = "TO ZERO INV"
    elif thChoice == 4:
        _, th = cv2.threshold(img, thVal, 225, cv2.THRESH_TRUNC)
        text = "TRUNC"
    else:
        pass

    # viewing the results
    cv2.imshow("Original Image", img)

    font = cv2.FONT_HERSHEY_SIMPLEX
    th = cv2.putText(th, text, (10, 20), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("Threshold Image", th)

    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()
