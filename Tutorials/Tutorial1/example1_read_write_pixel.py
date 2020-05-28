import numpy as np
import cv2

# Load a color image from a png file
img=cv2.imread('C:\\Users\\User\\Desktop\\ComputerVision\\Tutorials\\Tutorial1\\ex1_image.png') # change the path for image location

height = len(img)
width = len(img[0])
depth = len(img[0,0])

# create a new image and fill with the arithmetic inverse
result = np.zeros((height, width, depth), dtype = "uint8")
for r in range(height):
    for c in range(width):
        for p in range(depth):
           result[r,c,p] = 255 - img[r,c,p];

# show images
cv2.namedWindow('INPUT', flags=cv2.WINDOW_NORMAL)
cv2.imshow('INPUT',img)
cv2.namedWindow('RESULT', flags = cv2.WINDOW_NORMAL)
cv2.imshow('RESULT', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("C:\\Users\\User\\Desktop\\ComputerVision\\Tutorials\\Tutorial1\\ex1_output.png", result) # change path for write location