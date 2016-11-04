import cv2
import sys
import numpy as np
import collections
import os

faceCascade = cv2.CascadeClassifier("../api/haarcascade_frontalface_alt.xml")
video_capture = cv2.VideoCapture(0)
counter = 0
imgname = 0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )


    # Draw a rectangle around the faces

    for (x, y, w, h) in faces:
		print faces.shape[0]
		sys.stdout.flush()
		#cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		counter+=1;
		#reduce the frequency of snapshots
		if counter%2 == 0 :
			imgname+=1
			cv2.imwrite('tmp\\'+str(imgname)+'.jpg',frame[y:(y+h), x:(x+w)])

    # Display the resulting frame
    #cv2.imshow('Video', frame)
	#Quit after taking 10 snaps or pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q') or counter == 20 :
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
