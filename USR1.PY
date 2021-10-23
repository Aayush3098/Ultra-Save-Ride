import cv2
import sys
import time

# playsound is used for creating sound.......................................................... 
from playsound import playsound       



cascPath = sys.argv[0]
#faceCascade = cv2.CascadeClassifier(cascPath)
#face_cascade = cv2.CascadeClassifier('lbp_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


# Video capture is start from the here.........................................................
video_capture = cv2.VideoCapture(0)


# a is the temp. variable ....................................................
a = 0



while True:

    a = a+1
    # Capture frame-by-frame......................................................
    ret, frame = video_capture.read()

    # Converting color of image 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        #minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE.......................................
    )


    print (faces)
 
    if len(faces) == 0:     # Condition is start from the here for getting result..............................................
        print ("No faces found")

    elif len(faces) >=4:    # Alert sound start here if the given condition get false..........................................
        time.sleep(5)
        print("You are at risk")
        playsound('1.mp3')

 
    else:
        print (faces)
        print (faces.shape)
        print ("Number of faces detected: " + str(faces.shape[0]))
    


    #while len(faces) >=1:
     #   playsound('1.mp3')

    
    #\ Draw a rectangle around the faces.................................................................................................
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #cv2.putText(video_capture, "Number of faces detected: " + str(faces.shape[0]), (0,video_capture.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # Display the resulting frame......................................................................................................
    cv2.imshow('Video', frame)


    #5. For press any key to out (millisecond)............................................................................................
    cv2.waitKey(50)

    #7. For playing..........................................................................................................................
    key=cv2.waitKey(50)

    if key == ord('q'):
        break
print(a)
# When everything is done, release the capture..........................................................................................
video_capture.release()
cv2.destroyAllWindows() # All the window destroy here.......................................................................................................