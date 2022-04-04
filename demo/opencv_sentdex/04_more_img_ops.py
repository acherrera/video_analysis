"""
Doing some basic things with images
The hardest part of figuring this out was the indexing goes [y1:y2,x1:x2]. Which.... oh man. I figured that 
the indexing was y, x but didn't realize the exact way it went.
"""
import numpy as np
import cv2

def load_manipulate(filename):
    """
    Loads image and performs some manipulations for demonstration purposes.
    """
    img = cv2.imread(filename,cv2.IMREAD_COLOR)
    # Get single pixel
    px = img[55,55]

    # change pixel value to white and show new value
    img[55,55] = [255,255,255]
    px = img[55,55]
    print(px)

    # Now  get a region of interest (ROI)
    px = img[100:150,100:150]
    print(px)

    # And change the entire ROI to white
    # img[100:150,100:150] = [255,255,255]

    # Some reference values we can access 
    # print(img.shape)
    # print(img.size)
    # print(img.dtype)

    # cut out area (y, x) - annoying
    init_loc = (16, 914)

    # Keep track of the size of image extracted
    img_size = (400, 234)
    y1 = init_loc[0]
    y2 = init_loc[0]+img_size[0]

    x1 = init_loc[1]
    x2 = init_loc[1]+img_size[1]

    mtb_guy = img[y1:y2,x1:x2]

    # pasting is just setting the pixels to the values of the extracted area.
    img[0:img_size[0],0:img_size[1]] = mtb_guy

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    filename = "/home/tony/Pictures/mtb_images/01.jpg"
    load_manipulate(filename)
