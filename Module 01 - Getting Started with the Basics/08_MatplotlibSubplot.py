import cv2
from matplotlib import pyplot as plt

lena = plt.imread("../res/lena.jpg", -1)
messi = plt.imread("../res/messi5.jpg", -1)
sudoku = plt.imread("../res/sudoku.png", -1)
smarties = plt.imread("../res/smarties.png", -1)

titles = ["Lena", "Messi", "Sudoku", "Smarties"]
images = [lena, messi, sudoku, smarties]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
