import numpy as np
import cv2



cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()

    #grayvc = cv2.cvtColor(vc, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(rval)
 
    print (faces)
 
    if len(faces) == 0:
        print ("No faces found")
 
    else:
        print (faces)
        print (faces.shape)
        print ("Number of faces detected: " + str(faces.shape[0]))
 
    for (x,y,w,h) in faces:
        cv2.rectangle(vc,(x,y),(x+w,y+h),(0,255,0),1)
 
    cv2.rectangle(vc, ((0,vc.shape[0] -25)),(270, vc.shape[0]), (255,255,255), -1)
    cv2.putText(vc, "Number of faces detected: " + str(faces.shape[0]), (0,vc.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
 
    cv2.imshow('vc with faces',vc)
    cv2.waitKey(0)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
        vc.release()
    cv2.destroyWindow("preview")


#vc = cv2.imread("1.jpg")


 

cv2.destroyAllWindows()