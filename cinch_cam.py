import RPi.GPIO as gpio
import time as t;
from picamera import PiCamera
from firebase import firebase
import json
import os
from functools import partial
camera = PiCamera()

cam_ir = 15
count = 1
gpio.setmode(gpio.BOARD)
gpio.setup(cam_ir, gpio.IN)

def pictures():
    if(gpio.input(cam_ir) == True):
        camera.capture('Desktop/image'+str(count)+'.jpg')
        print("Car detailed captured...Uploading on database")
        t.sleep(1)
        count+=1
        print("done")

while(True):
    pictures()
    
