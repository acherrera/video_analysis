import numpy as np
import cv2
from matplotlib import pyplot as plt


def background_extract(filename):
    """
    remove background and fine just foreground
    """
    img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
    mask = np.zeros(img.shape[:2],np.uint8)

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    rect = (161,79,150,150)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]

    plt.imshow(img)
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    filename = "/home/tony/Pictures/opencv-python-foreground-extraction-tutorial.jpg"
    background_extract(filename)
