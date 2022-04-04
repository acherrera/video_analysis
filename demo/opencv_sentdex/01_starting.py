"""
Demonstrating showing images
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


def cv_show(filename):
    # Show image with opencv
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def matplot_show(filename):
    # show image with matplotlib
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
    plt.show()


if __name__ == "__main__":

    # This could be any image
    filename = "/home/tony/Pictures/mtb_images/01.jpg"
    matplot_show(filename)
