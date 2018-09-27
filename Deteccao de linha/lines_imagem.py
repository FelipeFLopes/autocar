
# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np

# Reading the required image in
# which operations are to be done.
# Make sure that the image is in the same
# directory in which this python program is
#img = cv2.imread('sudoku-original.jpg')
img = cv2.imread('index.jpeg')


# filter colour range we want
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low_yellow = np.array([18, 94, 140])
up_yellow = np.array([48, 255, 255])
mask = cv2.inRange(hsv, low_yellow, up_yellow)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply edge detection method on the image
edges = cv2.Canny(mask,75,150)

# This returns an array of r and theta values
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)


# The below for loop runs till r and theta values
# are in the range of the 2d array
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow('bexiga',edges)
cv2.imshow('imagem',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
