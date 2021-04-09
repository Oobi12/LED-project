import RPi.GPIO as GPIO
from time import sleep

#import tkinter 
#from tkinter import messagebox

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)

#sleep(0.2)

#def init(win):
  #  win.title("LED application")
 #   win.minsize(500, 100)

# hide main window
#box = tkinter.Tk()
#box.withdraw()

# message box display
#messagebox.showinfo("User Info", "But there's more")

#sleep(0.2)


for i in range(0,5): 
    GPIO.output(25,True)
    GPIO.output(18,True)
    GPIO.output(13,True)
    sleep(0.03)
    GPIO.output(25,False)
    GPIO.output(18,False)
    GPIO.output(13,False)
    sleep(0.03)
for i in range(6,10):
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.03)
    GPIO.output(25,False)
    GPIO.output(18,False)
    sleep(0.04)
for i in range(11,16):
    GPIO.output(25,True)
    sleep(0.04)
    GPIO.output(25,False)
    sleep(0.04)
    
for i in range (21,26):
    GPIO.output(25,True)
    sleep(0.04)
    GPIO.output(25,False)
    sleep(0.04)
    GPIO.output(18,True)
    sleep(0.04)
    GPIO.output(18,False)
    sleep(0.04)
    GPIO.output(17,True)
    sleep(0.04)
    GPIO.output(17,False)
    sleep(0.04)
    GPIO.output(13,True)
    sleep(0.04)
    GPIO.output(13,True)

for i in range (27,32):
    GPIO.output(13,True)
    sleep(0.04)
    GPIO.output(13,False)
    sleep(0.04)
    GPIO.output(17,True)
    sleep(0.04)
    GPIO.output(17,False)
    sleep(0.04)
    GPIO.output(18,True)
    sleep(0.04)
    GPIO.output(18,False)
    sleep(0.04)
    GPIO.output(25,True)
    sleep(0.04)
    GPIO.output(25,False)
    sleep(0.04)
    
for i in range (33,43):
    GPIO.output(13,True)
    GPIO.output(25,True)
    GPIO.output(5,True)
    sleep(0.04)
    GPIO.output(13,False)
    GPIO.output(25,False)
    GPIO.output(5,False)
    sleep(0.07)
    GPIO.output(18,True)
    GPIO.output(17,True)
    sleep(0.07)
    GPIO.output(18,False)
    GPIO.output(17,False)
    sleep(0.07)
    GPIO.output(13,True)
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.1)
    GPIO.output(5,True)
    sleep(0.07)
    GPIO.output(5,False)
    sleep(0.01)
    GPIO.output(13,False)
    GPIO.output(25,False)
    GPIO.output(18,False)
    sleep(0.04)
    GPIO.output(5,True)
    sleep(0.04)
    GPIO.output(5,False)
    sleep(0.04)
    
    
for i in range (44,49):
    GPIO.output(18,True)
    sleep(0.05)
    GPIO.output(25,True)
    sleep(0.07)
    GPIO.output(16,True)
    sleep(0.09)
    GPIO.output(16,False)
    sleep(0.09)
    GPIO.output(25,False)
    sleep(0.10)
    GPIO.output(18,False)
    sleep(0.12)

