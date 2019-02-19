# import the necessary packages
import numpy as np
import cv2


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
for (name, lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    points = cv2.findNonZero(mask)
    print(name)
    print(points)
    output = cv2.bitwise_and(image, image, mask=mask)

    # show the images
    #cv2.imshow("images", np.hstack([image, output]))
    #cv2.waitKey(0)

cv2.destroyAllWindows()