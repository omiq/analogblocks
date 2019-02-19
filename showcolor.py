# import the necessary packages
import numpy as np
import cv2
import requests
import json
import time

# load the image
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)

# success?
if not cap.isOpened():
    raise Exception("Could not open video device")
# Set properties. Each returns === True on success (i.e. correct resolution)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 160)

while 1:
    # get a frame of video
    ret, image = cap.read()

    # Get the color of the pixel
    b, g, r = (image[60, 60])
    b2, g2, r2 = (image[80, 80])
    b3, g3, r3 = (image[100, 100])
    print("[{},{},{}]".format(int((b+b2+b3)/3), int((g+g2+g3)/3), int((r+r2+r3)/3)))

    # delay
    time.sleep(1)

