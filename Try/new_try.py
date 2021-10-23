import cv2 , time

#1 Create a video object
video=cv2.VideoCapture(0)
#8.  a variable
a = 0

while True:
	a =  a+1

	#3 Create a frame object
	check, frame = video.read()

	print(check)
	print(frame) #Representing image

	#6. Converting to grayscale
	#gray=cv2.cvtColor(frame, cv2.COLOR_BRG2GRAY)

	#4. Show the frame
	cv2.imshow("Capturing",frame)

	#5. For press any key to out (millisecond)
	cv2.waitKey(12)

	#7. For playing
	key=cv2.waitKey(1)

	if key == ord('q'):
		break

print(a)
#2 Define Shutdown for camera
video.release()

cv2.destroyAllWindows()