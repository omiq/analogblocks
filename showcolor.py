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
    print(image[80,80])

    # delay
    time.sleep(1)
