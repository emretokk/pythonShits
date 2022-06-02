import cv2
import numpy as np

#            B G R
rectColor = (0,255,0)

#                   H S V
boundary_white = ([0,0,155], [255,100,255])
boundary_yellow= ([25,150,50], [35,255,255])
boundary_blue  = ([90, 50, 50], [130, 255, 255])
boundary_red   = ([161, 155, 84], [179, 255, 255])
boundary_green = ([45, 100,100], [75, 255, 255])
boundary_orange= ([15,150,0], [25,255,255]) 

lowerWhite = np.array(boundary_white[0])
upperWhite = np.array(boundary_white[1])

lowerYellow = np.array(boundary_yellow[0])
upperYellow = np.array(boundary_yellow[1])

lowerBlue = np.array(boundary_blue[0])
upperBlue = np.array(boundary_blue[1])

lowerRed = np.array(boundary_red[0])
upperRed = np.array(boundary_red[1])

lowerGreen = np.array(boundary_green[0])
upperGreen = np.array(boundary_green[1])

lowerOrange = np.array(boundary_orange[0])
upperOrange = np.array(boundary_orange[1])




borderCoors = [
    ((200,200), (300,300)),       ((300,200), (400,300)),         ((400,200), (500,300)),
    ((200,300), (300,400)),       ((300,300), (400,400)),         ((400,300), (500,400)),
    ((200,400), (300,500)),       ((300,400), (400,500)),         ((400,400), (500,500))
]

screen = cv2.VideoCapture(0)

while True:
    value, frame = screen.read()
    frame = cv2.resize(frame, (720, 576))
    frame = cv2.flip(frame, 1)

    for i in range(0, 9):
        cv2.rectangle(frame, borderCoors[i][0], borderCoors[i][1], rectColor, 1)

    lefttop = frame[borderCoors[0][0][0]:borderCoors[0][1][0], borderCoors[0][0][1]:borderCoors[0][1][1]]

    
    hsvlefttop = cv2.cvtColor(lefttop, cv2.COLOR_BGR2HSV)
    
    maskWhite = cv2.inRange(hsvlefttop, lowerWhite, upperWhite)
    maskYellow = cv2.inRange(hsvlefttop, lowerYellow, upperYellow)
    maskBlue = cv2.inRange(hsvlefttop, lowerBlue, upperBlue)
    maskRed = cv2.inRange(hsvlefttop, lowerRed, upperRed)
    maskGreen = cv2.inRange(hsvlefttop, lowerGreen, upperGreen)
    maskOrange = cv2.inRange(hsvlefttop, lowerOrange, upperOrange)

    contourWhite = cv2.findContours(maskBlue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    contourYellow = cv2.findContours(maskYellow.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    contourBlue = cv2.findContours(maskBlue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    contourRed = cv2.findContours(maskRed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    contourGreen = cv2.findContours(maskGreen.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    contourOrange = cv2.findContours(maskOrange.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    

    if len(contourBlue)>0:
        print("mavi")
        # blue_area = max(contourBlue, key=cv2.contourArea)
        # (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
        # cv2.rectangle(output,(xg,yg),(xg+wg, yg+hg),(0,255,0),2)
    elif len(contourYellow) > 0:
        print("sari")
    elif len(contourRed) > 0:
        print("kirmizi")
    elif len(contourGreen) > 0:
        print("yesil")
    elif len(contourOrange) > 0:
        print("turuncu")
    elif len(contourWhite) > 0:
        print("beyaz")

        # PRINTING STUFF
    #result = np.hstack([cropped, output])
    #output = cv2.bitwise_and(cropped, cropped, mask=maskBlue)
    #cv2.imshow('RGB',output)
        

    # hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
    # cv2.imshow("frame", hsv)
    # lower_blue = np.array([90, 50, 50])
    # upper_blue = np.array([130, 255, 255])
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # result = cv2.bitwise_and(cropped, cropped, mask=mask)
    # cv2.imshow("frame", result)

    # # loop over the boundaries
    # for (lower, upper) in boundaries:
    #     # create NumPy arrays from the boundaries
    #     lower = np.array(lower, dtype="uint8")
    #     upper = np.array(upper, dtype="uint8")

    #     # find the colors within the specified boundaries and apply
    #     # the mask
    #     mask = cv2.inRange(cropped, lower, upper)
    #     output = cv2.bitwise_and(cropped, cropped, mask=mask)

    #     imageOut = np.hstack([cropped, output])

    # # Display the resulting frame
    # cv2.imshow('RGB',imageOut)
    cv2.imshow("LOOK AT MEEE", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
screen.release()
cv2.destroyAllWindows()