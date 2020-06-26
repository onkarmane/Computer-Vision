import numpy as np
import argparse
import cv2

image = cv2.imread('path/to/image')
cv2.imshow("image",image)
cv2.waitKey(0)

#Mean or Average blur.Each pixel value is replace by average pixel values of desired neighborwood  
blurred = np.hstack([cv2.blur(image,(3,3)),
                     cv2.blur(image,(5,5)),cv2.blur(image,(7,7))])
cv2.imshow("blurred",blurred)
cv2.waitKey(0)

#Gaussian Blur
blurred1 = np.hstack([cv2.GaussianBlur(image,(3,3),0),
                      cv2.GaussianBlur(image,(5,5),0),cv2.GaussianBlur(image,(7,7),0)])
cv2.imshow("blurred1",blurred1)
cv2.waitKey(0)

#Median Blur
blurred2 = np.hstack([cv2.medianBlur(image,3),cv2.medianBlur(image,5),cv2.medianBlur(image,7)])
cv2.imshow("blurred2",blurred2)
cv2.waitKey(0)

#Bilateral Blur
blurred3 = np.hstack([cv2.bilateralFilter(image,3,21,21),
                      cv2.bilateralFilter(image,5,31,31),cv2.bilateralFilter(image,7,41,41)])
cv2.imshow("blurred3",blurred3)
cv2.waitKey(0)
