"""
Showing how to grab values from camera
"""

import numpy as np
import cv2



if __name__ == '__main__':

    # If multiple cameras, change this to other value
    cap = cv2.VideoCapture(0)
     
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
        cv2.imshow('frame',gray)

        # We we get the 'q' key.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
