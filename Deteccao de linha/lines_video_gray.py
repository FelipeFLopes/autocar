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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #low_yellow = np.array([18, 94, 140])
    #up_yellow = np.array([48, 255, 255])
    low_gray = np.array([0])
    up_gray = np.array([100])
    mask = cv2.inRange(gray, low_gray, up_gray)

    # Apply edge detection method on the image
    edges = cv2.Canny(mask,75,150)

    # This returns an array of r and theta values
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=80)

    # The below for loop runs till r and theta values
    # are in the range of the 2d array
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)


    ''' Teste a implementar como achar o contorno e centro de massa

    ret,thresh = cv2.threshold(gray,127,255,0)

    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (0,0,255), 3)


    M = cv2.moments(edges)

    xmedio = int(M['m10']/M['m00'])
    ymedio = int(M['m01']/M['m00'])

    print("O x medio eh " + str(xmedio))
    print("O y medio eh " + str(ymedio))


    dist1x = (width/4 - xmedio)
    dist2x = (3*width/4 - xmedio)


    cv2.line(frame, (int(width/4), int(height/2)), (int(xmedio), int(height/2)), (255, 0, 0), 3)
    cv2.line(frame, (int(3*width/4), int(height/2)), (int(xmedio), int(height/2)), (255, 0, 0), 3)


    cv2.circle(frame,(int(width/4),int(height/2) ), 20, (0,0,255), -1)
    cv2.circle(frame,( int(3*width/4), int(height/2) ), 20, (0,0,255), -1)


    print("A distancia em x1 eh " + str(dist1x) )
    print("A distancia em x2 eh " + str(dist2x))

    '''

    # Display the resulting frame
    cv2.imshow('mascara',mask)
    cv2.imshow('bordas',edges)
    cv2.imshow('gray',gray)
    cv2.imshow('imagem',frame)

    '''
    cv2.imshow('imagem',frame)
    cv2.imshow('hsv',hsv)
    '''

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
