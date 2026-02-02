import mss
import time
import cv2
import numpy as np

CHART_ZONE = {
    "top": 100,
    "left": 100,
    "width": 1200,
    "height": 600
}

def capture_chart():
    with mss.mss() as sct:
        img = np.array(sct.grab(CHART_ZONE))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img
