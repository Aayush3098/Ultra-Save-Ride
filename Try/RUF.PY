import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")


image = cv2.imread("1.jpg")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
faces = face_cascade.detectMultiScale(grayImage)
 
print (faces)
 
if len(faces) == 0:
    print ("No faces found")
 
else:
    print (faces)
    print (faces.shape)
    print ("Number of faces detected: " + str(faces.shape[0]))
 
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
 
    cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
    cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
 
    cv2.imshow('Image with faces',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()