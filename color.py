# import the necessary packages
import numpy as np
import cv2
import requests
import json

def unpack_triple_nested(tn):
    '''
    [[[x1, y1]], [x2, y2]], ...] --> [(x1, y1), (x2, y2), ...]
    '''
    tuples = []
    if tn is not None:
        for dn in tn:
            for sn in dn:
                tuples.append((sn[0], sn[1]))
    return tuples


def simple_centroid(points):
    '''
    Simple centroid without any outlier compensation
    '''
    count = 0
    xsum = 0
    ysum = 0
    for (x, y) in points:
        count += 1
        xsum += x
        ysum += y
    if count:
        return (xsum/count, ysum/count)
    else:
        return None


# load the image
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)

# success?
if not cap.isOpened():
    raise Exception("Could not open video device")
# Set properties. Each returns === True on success (i.e. correct resolution)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

# get a frame of video
ret, image = cap.read()

# display and save the image
#cv2.imshow('Webcam', image)
#cv2.imwrite('test.png', image)

# Get the color of the pixel
#print(image[80,80])

# did that work?
#print(ret)

#cv2.waitKey(0)

# define the list of boundaries
boundaries = [
    ("red", [10, 0, 60], [30, 0, 70]), #red
    ("blue", [40, 30, 0], [55, 55,  0]),   #blue
    ("green", [40, 55, 6], [51, 56, 15]), #green
    ("orange", [0, 0, 10], [0, 0, 17]),
    ("pink", [120, 35, 240], [165, 70, 255]),
    ("purple", [250, 160, 145], [255, 190, 185]),
    ("yellow", [60, 170, 180], [100, 185, 207]),
]

# loop over the boundaries

color_tuples = []

for (name, lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)

    # raw datas
    #print(cv2.findNonZero(mask))

    # unpack
    points = unpack_triple_nested(cv2.findNonZero(mask))
    centroid = simple_centroid(points)
    if centroid is not None:  # None color was not found
        cen_x, cen_y = centroid
        color_tuples.append((name, cen_x, cen_y))

    # show the images
    output = cv2.bitwise_and(image, image, mask=mask)
    #cv2.imshow("images", np.hstack([image, output]))
    #cv2.waitKey(0)

# release back to os
cap.release()
cv2.destroyAllWindows()

# output the geometry
color_tuples.sort(key=lambda t: t[2])
print(color_tuples)

# post the data
r = requests.post('http://localhost:5000/changed', data=json.dumps(color_tuples))
