# Histogram equalization

from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

image = cv2.imread('path/to/image')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("image",image)
cv2.waitKey(0)

eq = cv2.equalizeHist(image)
##hist = cv2.calcHist([image],[0],None,[256],[0,256])
hist2 = cv2.calcHist([eq],[0],None,[256],[0,256])
cv2.imshow("Histogram Equalization", np.hstack([eq]))
cv2.waitKey(0)
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist2)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
