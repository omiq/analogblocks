# import the necessary packages
import numpy as np
import cv2


def unpack_triple_nested(tn):
    '''
    [[[x1, y1]], [x2, y2]], ...] --> [(x1, y1), (x2, y2), ...]
    '''
    tuples = []
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
image = cv2.imread("blocks.jpg")

# define the list of boundaries
boundaries = [
    ("red", [17, 15, 100], [50, 56, 200]), #red
    ("blue", [100, 0, 0], [255, 50, 50]),   #blue
    ("yellow", [25, 146, 190], [62, 174, 250]), #yellow
    ("green", [0, 60, 0], [50, 255, 50]), #green
    ("orange", [20, 50, 100], [50, 100, 255]) #orange
]

# loop over the boundaries

color_tuples = []

for (name, lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    points = unpack_triple_nested(cv2.findNonZero(mask))
    cen_x, cen_y = simple_centroid(points)
    color_tuples.append((name, cen_x, cen_y))

    # show the images
    # output = cv2.bitwise_and(image, image, mask=mask)
    #cv2.imshow("images", np.hstack([image, output]))
    #cv2.waitKey(0)

cv2.destroyAllWindows()

color_tuples.sort(key=lambda t: t[2])
print(color_tuples)
