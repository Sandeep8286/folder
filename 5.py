import cv2 
import numpy as np 
import datetime 
import time 
 
# Initialize the camera capture object 
cap = cv2.VideoCapture(0) # 0 represents the default camera 
 
# Load the pre-trained face detection model 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
 
# Start the main loop to capture frames from the camera 
while True:
     ret, frame = cap.read() # Read a frame from the camera 
 
# Convert the frame to grayscale for face detection
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
 
# Perform face detection     
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5) 
 
# Draw rectangles around the detected faces
     for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
         timestamp = datetime.datetime.now()
         ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
         cv2.imwrite("images/" + str(ts) + ".jpg", frame)
         print "Image save with name = " + "images/" + str(ts) + ".jpg"  
 
# Display the frame with detected faces
     cv2.imshow('Face Detection', frame) 
 
# Break the loop if 'q' is pressed     
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break 
 
# Release the camera and close the windows 
cap.release()
cv2.destroyAllWindows() 