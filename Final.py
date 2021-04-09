import RPi.GPIO as GPIO
from time import sleep


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

for i in range (0,1):
    GPIO.output(17,True)
    GPIO.output(5,True)
    GPIO.output(13,True)
    sleep(0.3)
    GPIO.output(17,False)
    GPIO.output(5,False)
    GPIO.output(13,False)
    sleep(0.3)
    GPIO.output(18,True)
    GPIO.output(25,True)
    GPIO.output(16,True)
    sleep(0.3)
    GPIO.output(18,False)
    GPIO.output(25,False)
    GPIO.output(16,False)

for i in range(2,3):
    GPIO.output(17,True)
    GPIO.output(5,True)
    GPIO.output(13,True)
    sleep(0.3)
    GPIO.output(18,True)
    GPIO.output(25,True)
    GPIO.output(16,True)

    
    
    