import cv2

# enter the path to the image
imgPath = "res/sudoku.png"  # "res/gradient.png"


def nothing(x):
    pass


cv2.namedWindow("Original Image")
cv2.namedWindow("Threshold Image")
cv2.createTrackbar("Adaptive Method", "Threshold Image", 0, 1, nothing)
cv2.createTrackbar("Threshold Type", "Threshold Image", 0, 1, nothing)  # seems like it only works with binary
cv2.createTrackbar("Block Size", "Threshold Image", 3, 100, nothing)
cv2.createTrackbar("C", "Threshold Image", 1, 50, nothing)

adaptive_method_dict = {
    0: cv2.ADAPTIVE_THRESH_MEAN_C,
    1: cv2.ADAPTIVE_THRESH_GAUSSIAN_C
}

threshold_type_dict = {
    0: cv2.THRESH_BINARY,
    1: cv2.THRESH_BINARY_INV,
    2: cv2.THRESH_TOZERO,
    3: cv2.THRESH_TOZERO_INV,
    4: cv2.THRESH_TRUNC
}

adaptive_name_dict = {
    0: "ADAPTIVE THRESH MEAN C",
    1: "ADAPTIVE THRESH GAUSSIAN C"
}

threshold_name_dict = {
    0: "BINARY",
    1: "BINARY INV",
    2: "TOZERO",
    3: "TOZERO INV",
    4: "TRUNC"
}

while True:
    # get image
    img = cv2.imread(imgPath, 0)

    # get values from the track bar
    mtd = cv2.getTrackbarPos("Adaptive Method", "Threshold Image")
    typ = cv2.getTrackbarPos("Threshold Type", "Threshold Image")
    blk = cv2.getTrackbarPos("Block Size", "Threshold Image")   # should be an odd number and greater than 1
    if blk == 0:
        blk = 3
    else:
        blk = blk * 2 + 1
    c = cv2.getTrackbarPos("C", "Threshold Image")

    # get adaptive threshold image
    th = cv2.adaptiveThreshold(img, 255, adaptive_method_dict[mtd], threshold_type_dict[typ], blk, c)

    # prepare adaptive threshold image
    font = cv2.FONT_HERSHEY_SIMPLEX
    th = cv2.putText(th, adaptive_name_dict[mtd], (10, 20), font, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
    th = cv2.putText(th, threshold_name_dict[typ], (10, 40), font, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
    th = cv2.putText(th, "Block Size: "+str(blk), (10, 60), font, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
    th = cv2.putText(th, "C: "+str(c), (10, 80), font, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

    # viewing the results
    cv2.imshow("Original Image", img)
    cv2.imshow("Threshold Image", th)

    # printing to the console
    print("-----------------------------------------------")
    print("Adaptive Method :", adaptive_method_dict[mtd])
    print("Threshold Type  :", threshold_type_dict[typ])
    print("Block Size      :", blk)
    print("Constant C      :", c)
    print("-----------------------------------------------")

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
