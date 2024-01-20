from unittest import result
import cv2
import mediapipe as mp
import math
import time 

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import numpy 

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

cap= cv2.VideoCapture(0)
mpDraw= mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands()

volRange = volume.GetVolumeRange()
minvol = volRange[0]
maxvol = volRange[1]
vol=0
volBar=400
volPer=0 

pTime = time.time()

while True:  
    success, img =cap.read() 
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results=hands.process(imgRGB)
    

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])

            if lmList:
                x1,y1 = lmList[4][1], lmList[4][2]  
                x2,y2 = lmList[8][1], lmList[8][2]

                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED) 
                cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED) 

                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED) 
                z1,z2 = (x1+x2)//2 , (y1+y2)//2
                length = math.hypot(x2-x1, y2-y1)

            if length<=50:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED) 
            
            vol= numpy.interp(length, [50,100], [minvol,maxvol])
            volPer = numpy.interp(length, [50,100], [0,100])
            volBar = numpy.interp(length,[50,300], [400,150])

            volume.SetMasterVolumeLevel(vol, None)
            cv2.putText(img, str(int(volPer)),(40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 0, 0),3)
            cv2.rectangle(img, (50,150),(85,400),(255, 0, 0),3)
            cv2.rectangle(img, (50, int(volBar)),(85,400),(0,231,23),cv2.FILLED)

    cTime =time.time()

    fps=1/(cTime-pTime)
    pTime = cTime 
    cv2.putText(img,f'FPS: {int(fps)}',(40,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0), 3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
    

