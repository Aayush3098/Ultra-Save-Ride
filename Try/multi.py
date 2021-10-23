import cv2
import sys

cascPath = sys.argv[0]
#faceCascade = cv2.CascadeClassifier(cascPath)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 


video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )


    print (faces)
 
    if len(faces) == 0:
        print ("No faces found")
 
    else:
        print (faces)
        print (faces.shape)
        print ("Number of faces detected: " + str(faces.shape[0]))
 

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.putText(video_capture, "Number of faces detected: " + str(faces.shape[0]), (0,video_capture.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()