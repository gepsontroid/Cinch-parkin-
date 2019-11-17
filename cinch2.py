# Cinch Parkin python code for raspii

#importing libraries
import RPi.GPIO as gpio
import time as t
import datetime
from firebase import firebase
import json
import os
from functools import partial

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

#defining output pins for 8 slots

a = 16 #slotTrue
b = 18 #slot2
c = 19 #slot3
d = 21 #slot4
e = 22 #slot5
f = 23 #slot6
g = 24 #slot7
h = 26 #slot8

#setting up input pins
gpio.setup(29,gpio.IN)
gpio.setup(31,gpio.IN)
gpio.setup(7,gpio.IN)
gpio.setup(8,gpio.IN)
gpio.setup(10,gpio.IN)
gpio.setup(11,gpio.IN)
gpio.setup(12,gpio.IN)
gpio.setup(13,gpio.IN)
gpio.setup(15,gpio.IN)

#setting up output pins for green leds
gpio.setup(a,gpio.OUT)
gpio.setup(b,gpio.OUT)
gpio.setup(c,gpio.OUT)
gpio.setup(d,gpio.OUT)
gpio.setup(e,gpio.OUT)
gpio.setup(f,gpio.OUT)
gpio.setup(g,gpio.OUT)
gpio.setup(h,gpio.OUT)

#defining sensor pins for 8 slots
slot_1 = 29
slot_2 = 31
slot_3 = 7
slot_4 = 8
slot_5 = 10
slot_6 = 11
slot_7 = 12
slot_8 = 13
camera_ir = 15
empty = 1
filled = 0



#linking database to sensors
firebase = firebase.FirebaseApplication('https://cinch-parkin.firebaseio.com',None)

#initiating table
print("Initiating Database.....have patience")
firebase.put("/Cinchparkin", "/slot_1", empty) 
firebase.put("/Cinchparkin", "/slot_2", empty)
firebase.put("/Cinchparkin", "/slot_3", empty)
firebase.put("/Cinchparkin", "/slot_4", empty)
firebase.put("/Cinchparkin", "/slot_5", empty)
firebase.put("/Cinchparkin", "/slot_6", empty)
firebase.put("/Cinchparkin", "/slot_7", empty)
firebase.put("/Cinchparkin", "/slot_8", empty)

def slot1():

    if(gpio.input(slot_1) == 1):
       firebase.post('/Cinchparkin/slot_1',filled)
       gpio.output(a,False)
       print("Slot_1: Filled")
    elif(gpio.input(slot_1) == 0):
       firebase.post('/Cinchparkin/slot_1',empty)
       gpio.output(a,True)
       print("Slot_1: Empty")
       
    
def slot2():

    if(gpio.input(slot_2) == True):
       firebase.post('/Cinchparkin/slot_2',filled)
       gpio.output(b,False)
       print("Slot_2: Filled")
    elif(gpio.input(slot_2) == False):
       firebase.post('/Cinchparkin/slot_2',empty)
       gpio.output(b,True)
       print("Slot_2: Empty")

def slot3():

    if(gpio.input(slot_3)== True):
       firebase.post('/Cinchparkin/slot_3',filled)
       gpio.output(c,False)
       print("Slot_3: Filled")
    elif(gpio.input(slot_3) == False):
       firebase.post('/Cinchparkin/slot_3',empty)
       gpio.output(c,True)
       print("Slot_3: Empty")

def slot4():

    if(gpio.input(slot_4) == True):
       firebase.post('/Cinchparkin/slot_4',filled)
       gpio.output(d,False)
       print("Slot_4: Filled")
    elif(gpio.input(slot_4) == False):
       firebase.post('/Cinchparkin/slot_4',empty)
       gpio.output(d,True)
       print("Slot_4: Empty")

def slot5():

    if(gpio.input(slot_5) == True):
       firebase.post('/Cinchparkin/slot_5',filled)
       gpio.output(e,False)
       print("Slot_5: Filled")
    elif(gpio.input(slot_5) == False):
       firebase.post('/Cinchparkin/slot_5',empty)
       gpio.output(e,True)
       print("Slot_5: Empty")
    
def slot6():

    if(gpio.input(slot_6) == True):
       firebase.post('/Cinchparkin/slot_6',filled)
       gpio.output(f,False)
       print("Slot_6: Filled")
    elif(gpio.input(slot_6) == False):
       firebase.post('/Cinchparkin/slot_6',empty)
       gpio.output(f,True)
       print("Slot_6: Empty")

def slot7():

    if(gpio.input(slot_7) == True):
       firebase.post('/Cinchparkin/slot_7',filled)
       gpio.output(g,False)
       print("Slot_7: Filled")
    elif(gpio.input(slot_7) == False):
       firebase.post('/Cinchparkin/slot_7',empty)
       gpio.output(g,True)
       print("Slot_7: Empty")

def slot8():

    if(gpio.input(slot_8) == True):
       firebase.post('/Cinchparkin/slot_8',filled)
       gpio.output(h,False)
       print("Slot_8: Filled")
    elif(gpio.input(slot_8) == False):
       firebase.post('/Cinchparkin/slot_8',empty)
       gpio.output(h,True)
       print("Slot_8: Empty")
       print("________________________________________________________")


#integrating fuctions
def update_slots():
       slot1()
       slot2()
       slot3()
       slot4()
       slot5()
       slot6()
       slot7()
       slot8()
       

#updating values in real time
while True:
       update_slots()
       t.sleep(15)

       


