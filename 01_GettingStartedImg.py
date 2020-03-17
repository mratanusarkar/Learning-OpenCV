import cv2

# cv2.imread(<img relative path>, <flag>)
# flags:
#  1   : color
#  0   : grayscale
# -1   : loads img as it is including alpha channel
image = cv2.imread("res/lena.jpg", -1)
print(image)

# cv2.imshow(<window name>, <img variable>)
cv2.imshow("original image", image)

key = cv2.waitKey(0) & 0xFF

if key == 27: # Esc key
    cv2.destroyAllWindows()
elif key == ord('s'):
    print('saving a copy of the image...')
    cv2.imwrite('lena_copy.png', image)
    cv2.destroyAllWindows()
else:
    print('end of code')
    cv2.destroyAllWindows()
