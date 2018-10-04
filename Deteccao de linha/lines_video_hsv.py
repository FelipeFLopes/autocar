import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):


    width = cap.get(3)  # float
    height = cap.get(4) # float


    # Capture frame-by-frame
    ret, frame = cap.read()

    # filter colour range we want
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_black = np.array([0, 0, 0])
    up_black = np.array([180, 255, 15])
    mask = cv2.inRange(hsv, low_black, up_black)

    # Apply edge detection method on the image
    edges = cv2.Canny(mask,75,150)

    # This returns an array of r and theta values
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=80)

    res = cv2.bitwise_and(hsv,hsv,mask = mask)

    # The below for loop runs till r and theta values
    # are in the range of the 2d array
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)


    #Transforma em escala de cinza
    rgb = cv2.cvtColor(res, cv2.COLOR_HSV2RGB)
    gray = cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)

    #Binariza a imagem
    ret,thresh = cv2.threshold(gray,127,255,0)

    #Acha contornos
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    M = cv2.moments(contours[0])

    if M["m00"] != 0:
        xmedio = int(M['m10']/M['m00'])
        ymedio = int(M['m01']/M['m00'])
    else:
        xmedio = 0
        ymedio = 0

    print("O x medio eh " + str(xmedio))
    print("O y medio eh " + str(ymedio))

    cv2.circle(frame, (xmedio, ymedio), 5, (255, 255, 255), -1)


    dist1x = (width/4 - xmedio)
    dist2x = (3*width/4 - xmedio)


    cv2.line(frame, (int(width/4), int(height/2)), (int(xmedio), int(height/2)), (255, 0, 0), 3)
    cv2.line(frame, (int(3*width/4), int(height/2)), (int(xmedio), int(height/2)), (255, 0, 0), 3)


    cv2.circle(frame,(int(width/4),int(height/2) ), 20, (0,0,255), -1)
    cv2.circle(frame,( int(3*width/4), int(height/2) ), 20, (0,0,255), -1)


    print("A distancia em x1 eh " + str(dist1x) )
    print("A distancia em x2 eh " + str(dist2x))


    # Display the resulting frame
    cv2.imshow('mascara',mask)
    cv2.imshow('bordas',edges)
    cv2.imshow('res',res)
    cv2.imshow('imagem',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
