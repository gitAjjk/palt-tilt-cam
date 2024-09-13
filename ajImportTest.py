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
# pi@rpirtgZ:~/ $ /home/pi/rpi-deep-pantilt/.ajvenv/bin/python3.9 -- /home/pi/palt-tilt-cam/ ajImportTest.py

import numpy
print("numpy v" + numpy.__version__) #numpy v2.0.2
import cv2 # ModuleNotFoundError: No module named 'cv2
print("cv2 v" + cv2.__version__)
import os

