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
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)
ret, image = cap.read()

while 1:
    # get a frame of video
    ret, image = cap.read()
    cv2.rectangle(image, (60, 60), (95, 95), (0, 255, 0), 5)
    cv2.imshow('Webcam', image)
    cv2.waitKey()

    # Get the color of the pixel
    b, g, r = (image[65, 65])
    b2, g2, r2 = (image[70, 70])
    b3, g3, r3 = (image[90, 90])

    print("\n\n[{},{},{}]".format(int(b), int(g), int(r)))
    print("[{},{},{}]".format(int(b2), int(g2), int(r2)))
    print("[{},{},{}]".format(int(b3), int(g3), int(r3)))


