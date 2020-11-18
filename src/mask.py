import cv2
import numpy as np


def get_mask():
    """
    Compute a binary mask from the manually processed mask.
    """
    mask = cv2.imread("media/mask.png")
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    lower = np.array(1)
    upper = np.array(255)
    return cv2.inRange(mask, lower, upper)
