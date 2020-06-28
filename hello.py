import cv2
image = cv2.imread('jena.jpg', 0)
cv2.imshow('', image)
cv2.waitKey(0)
print(image.ndim)
