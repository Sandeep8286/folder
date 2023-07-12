Pract 1:

#To install Python, open terminal and give the below command:
sudo apt update
sudo apt install python3 idle3
#Then set the variable path:
 Echo ‘export PATH=”$PATH:/home/admin/.local/bin”’>> ~/bashrc
#To install Node.js give the below command in the terminal:
sudo apt-get install nodejs

#Source Code: Python Code:
num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
For nodejs to execute type node on terminal.

#Pract 2

#Source Code:
import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

RELAY1 = 20
RELAY2 = 16

FAN = RELAY1
LIGHT = RELAY2

GPIO.setwarnings(False)
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
# set up GPIO output channel
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)


# Your Telegram token key variable.
telegramBotToken = '6212499066:AAEjXEFaH_LQV8OQ6SFn_ZYpa0RbhDQyHe8'


# function to on and off devices
def on(pin):
    GPIO.output(pin,GPIO.HIGH)
    return "on"

def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return "off"


def handle(msg):
    chat_id = msg['chat']['id']
    print str(chat_id)
    command = str(msg['text'])

    print 'Receive message from Telegram: %s' % command

    if 'Fan' in command or 'fan' in command:
        if 'on' in command:
            bot.sendMessage(chat_id, str("Fan " + on(FAN)))
        elif 'off' in command:
            bot.sendMessage(chat_id, str( "Fan " + off(FAN)))

    elif 'Light' in command or 'light' in command:
        if 'on' in command:
            bot.sendMessage(chat_id, str("Light " + on(LIGHT)))
        elif 'off' in command:
            bot.sendMessage(chat_id, str("Light " + off(LIGHT)))
bot = telepot.Bot(telegramBotToken)
bot.message_loop(handle)
print 'I am listening...'

while 1:
    time.sleep(10)


#pract 3
#Install Flask package with the below command in the terminal:

#sudo pip install Flask

#service1.py
from flask import Flask
app = Flask(__name__)
@ app.route('/')
def hello():
    return "hello from microservices1"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#service2.py
import requests
// replace the url in below statement with the url that you get
// after running the service1.py
response=requests.get("http://0.0.0.0:5000")
print (response.text)

#pract 4

import RPi.GPIO as GPIO
from flask import Flask, request

# Define GPIO pin
led_pin = 21

# set GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Create Flask app
app = Flask(__name__)

# Define route to handle HTTP POST request
@app.route('/',methods=['POST'])
def handle_post():
    message = request.get_data(as_text=True)
    if message == "ON":
        GPIO.output(led_pin, GPIO.HIGH)
    elif message == "OFF":
        GPIO.output(led_pin, GPIO.LOW)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
#Command Line code
#chmod +X Practname.py
#sudo ch
#sudo chmod +X practname.py
#sudo python practname.py
#new terminal
#curl -X POST -d "ON" http://127.0.0.1:8080


#Pract5

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