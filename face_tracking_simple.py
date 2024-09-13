#aj 240913:
""" pi@rpirtgZ:~/palt-tilt-cam $  
    cd /home/pi/palt-tilt-cam ; 
    /usr/bin/env 
    /home/pi/.virtualenvs/ajcv/bin/python 
    /home/pi/.vscode-server/extensions/ms-python.debugpy-2024.10.0/bundled/libs/debugpy/adapter/../../debugpy/launcher 
    54633 
    -- 
    /home/pi/palt-tilt-cam/face_tracking_simple.py """ #> #numpy v2.0.2 + ModuleNotFoundError: No module named 'cv2
""" pi@rpirtgZ:~/palt-tilt-cam $  
    /usr/bin/env /home/pi/rpi-deep-pantilt/.ajvenv/bin/python3.9 
    /home/pi/.vscode-server/extensions/ms-python.debugpy-2024.10.0/bundled/libs/debugpy/adapter/../../debugpy/launcher 
    35175 
    -- /home/pi/palt-tilt-cam/face_tracking_simple.py """ #> numpy v1.26.4 + cv2 v4.6.0
#>>> SELECT DUS JUISTE virtual environment (rechtsonder, of met [ctrl][shift][p] Python: select interpreter)
# pi@rpirtgZ:~/ $ /home/pi/rpi-deep-pantilt/.ajvenv/bin/python3.9 -- /home/pi/palt-tilt-cam/face_tracking_simple.py
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:33:26 2020

@author: nguye
"""

import numpy
print("numpy v" + numpy.__version__) #numpy v2.0.2
import cv2 # ModuleNotFoundError: No module named 'cv2
print("cv2 v" + cv2.__version__)
import os

# Load the cascade
# faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
# faceCascade.load('data/haarcascade_frontalface_default.xml')

cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml" #/home/pi/rpi-deep-pantilt/.ajvenv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml
faceCascade = cv2.CascadeClassifier(cascPath)
# Read the input image

# https://techvidvan.com/tutorials/face-recognition-project-python-opencv/
video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('Video', frame) # Can't initialize GTK backend in function 'cvInitSystem' 
    # >> In terminal hieronder: $ export DISPLAY=:0 >> Met hard aangesloten monitor EN met (Real)VNC-viewvideo zichtbaar.
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #Na aanklick videoschermpje: 'q'
        break
    
    
video_capture.release()
cv2.destroyAllWindows()