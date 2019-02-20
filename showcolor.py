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
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3)

while 1:
    # get a frame of video
    ret, image = cap.read()

    # Get the color of the pixel
    b, g, r = (image[1, 1])
    print("[{},{},{}]".format(b, g, r))

    # delay
    time.sleep(1)

