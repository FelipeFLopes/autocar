import cv2
import numpy as np

#Detectar a cor preta
bgr = [204, 72, 63]
thresh = 40

lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])


img = cv2.imread('circles2.png', 1)

#img = cv2.imread('estrada.jpeg', 1)


maskLAB = cv2.inRange(img, minLAB, maxLAB)

cv2.imshow('mask',maskLAB)
cv2.imshow('image', img)


cv2.waitKey(0)


cv2.destroyAllWindows()
