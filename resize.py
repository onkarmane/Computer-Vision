import numpy as np
import imutils
import argparse
import cv2

arg = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True,
                help = "path of the image")
args = vars(arg.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)

r = 1000/image.shape[1]
dim = (1000,int(image.shape[0]*r))
resized = cv2.resize(image,dim,interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resized (width)",resized)
cv2.waitKey(0)
