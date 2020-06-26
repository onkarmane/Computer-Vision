#Read the image from given path and display its dimensions.

import cv2
import numpy as np
im = np.ones(200, 200, 3)
image = cv2.imread(im)
print("width: % d pixels", image.shape[1])
print("height: %d pixels", image.shape[0])
print("channels: %d", image.shape[2])
cv2.imshow("Image", image)
cv2.waitKey(0)
