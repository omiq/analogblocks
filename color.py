# import the necessary packages
import numpy as np
import cv2


# load the image
image = cv2.imread("blocks.jpg")

# define the list of boundaries
boundaries = [
    ([17, 15, 100], [50, 56, 200]), #red
    ([100, 0, 0], [255, 50, 50]),   #blue
    ([25, 146, 190], [62, 174, 250]), #yellow
    ([0, 60, 0], [50, 255, 50]) #green
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)

cv2.destroyAllWindows()