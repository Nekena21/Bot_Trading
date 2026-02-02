import cv2

import cv2


def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges



def detect_candle_color(img):
    # approximation
    green = img[:,:,1].mean()
    red = img[:,:,2].mean()

    if green > red:
        return "GREEN"
    else:
        return "RED"
