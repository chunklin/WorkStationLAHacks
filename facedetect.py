# OpenCV program to detect face in real time 
# import libraries of python OpenCV 
# where its functionality resides 
import cv2
import serial
from firebase import firebase
firebase = firebase.FirebaseApplication('https://lahworkstation2019.firebaseio.com/')
ard = serial.Serial('/dev/tty96B0', 9600)
result = firebase.put(
    '',
    '/user',
    {
        "boss": "false",
        "door": "false",
        "light": 69,
        "temperature": 420
    }
)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# https://github.com/Itseez/opencv/blob/master 
# /data/haarcascades/haarcascade_eye.xml 
# Trained XML file for detecting eyes 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 

# capture frames from a camera 
cap = cv2.VideoCapture(1)

# loop runs if capturing has been initialized.
facePresent = False
counter = 0;
while 1:

    #sensors
    ardOut = ard.readline()
    #format for string is XXXYYYZABBB (11 chars)
    #order is light (x), Sound (y), Ultrasound/boolean (z), lock status/boolean (a), Temperature(b)
    light = ardOut[:3]
    sound = ardOut[3:6]
    ultrasound = ardOut[6:7]
    if ultrasound == 1:
        ultraBool = True
    else:
        ultraBool = False
    lock = ardOut[7:8]
    if lock == 1:
        lockBool = True
    else:
        lockBool = False
    lock = ardOut[7:8]
    temperature = ardOut[8:11]
    # reads frames from a camera
    ret, img = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detects eyes of different sizes in the input image
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # To draw a rectangle in eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 127, 255), 2)

        facePresent = True
    # Display an image in a window
    cv2.imshow('img', img)
    if facePresent and counter == 0:
        result = firebase.put(
            '',
            '/user',
            {
                "boss": "false",
                "door": ultraBool,
                "light": light,
                "lock": lockBool,
                "sound": sound,
                "temperature": temperature
            }
        )
        counter = 100
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    facePresent = False
    if counter > 0:
        counter -= 1
    result = firebase.put(
        '',
        '/user',
        {
            "boss": "false",
            "door": ultraBool,
            "light": light,
            "lock": lockBool,
            "sound": sound,
            "temperature": temperature
        }
    )
    print(counter)

# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
