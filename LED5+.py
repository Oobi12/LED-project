
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

#sleep(0.2)

#def init(win):
   # win.title("LED application")
    #win.minsize(500, 100)

# hide main window
#win = Tk()
#win.withdraw()

# message box display
#messagebox.showinfo("User Info", "But there's more")

#sleep(0.2)

for i in range(0,7): 
    GPIO.output(25,True)
    sleep(0.01)
    GPIO.output(25,False)
    sleep(0.01)
    GPIO.output(18,True)
    sleep(0.01)
    GPIO.output(18,False)
    sleep(0.01)
    GPIO.output(13,True)
    sleep(0.01)
    GPIO.output(13,False)
    sleep(0.01)
    
for i in range(8,9):
    GPIO.output(25,True)
    sleep(0.01)
    GPIO.output(25,False)
    sleep(0.01)
    GPIO.output(18,True)
    sleep(0.01)
    GPIO.output(18,False)
    sleep(0.01)
for i in range(10,18): 
    GPIO.output(25,True)
    sleep(0.01)
    GPIO.output(25,False)
    sleep(0.01)
    GPIO.output(18,True)
    sleep(0.01)
    GPIO.output(18,False)
    sleep(0.01)
    GPIO.output(13,True)
    sleep(0.01)
    GPIO.output(13,False)
    sleep(0.01)
    
for i in range(19,29):
    GPIO.output(25,True)
    sleep(0.01)
    GPIO.output(25,False)
    sleep(0.01)
    GPIO.output(18,True)
    sleep(0.01)
    GPIO.output(18,False)
    sleep(0.01)
    
for i in range(30,35):
    GPIO.output(16,True)
    sleep(0.01)
    GPIO.output(16,False)
    sleep(0.01)
    GPIO.output(5,True)
    sleep(0.01)
    GPIO.output(5,False)
    sleep(0.01)

for i in range(36,41):
    GPIO.output(16,True)
    sleep(0.01)
    GPIO.output(16,False)
    sleep(0.01)
    GPIO.output(18,True)
    sleep(0.01)
    GPIO.output(18,False)
    sleep(0.01)
    GPIO.output(25,True)
    sleep(0.01)
    GPIO.output(25,False)
    sleep(0.01)
    GPIO.output(17,True)
    sleep(0.01)
    GPIO.output(17,False)
    sleep(0.01)
    
for i in range(42,50):
    GPIO.output(25,True)
    GPIO.output(18,True)
    GPIO.output(13,True)
    sleep(0.019)
    GPIO.output(25,False)
    GPIO.output(18,False)
    GPIO.output(13,False)
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.019)
    GPIO.output(25,False)
    GPIO.output(18,False)
    sleep(0.02)
    GPIO.output(25,True)
    sleep(0.01)
    GPIO.output(25,False)
    sleep(0.01)
    GPIO.output(18,True)
    sleep(0.01)
    GPIO.output(18,False)
    sleep(0.01)
    GPIO.output(13,True)
    sleep(0.01)
    GPIO.output(13,False)
    sleep(0.01)
    GPIO.output(13,True)
    GPIO.output(25,True)
    GPIO.output(5,True)
    sleep(0.02)
    GPIO.output(13,False)
    GPIO.output(25,False)
    GPIO.output(5,False)
    sleep(0.019)
    GPIO.output(18,True)
    GPIO.output(17,True)
    sleep(0.019)
    GPIO.output(18,False)
    GPIO.output(17,False)
    sleep(0.019)
    GPIO.output(13,True)
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.019)
    GPIO.output(5,True)
    sleep(0.02)
    GPIO.output(5,False)
    sleep(0.01)
    
sleep(0.2)

def init(win):
    win.title("LED application")
    win.minsize(500, 100)

# hide main window
box = tkinter.Tk()
box.withdraw()

# message box display
messagebox.showinfo("User Info", "Starting slowdown")

sleep(0.2)

for i in range(51,56): 
    GPIO.output(25,True)
    sleep(0.05)
    GPIO.output(25,False)
    sleep(0.05)
    GPIO.output(18,True)
    sleep(0.05)
    GPIO.output(18,False)
    sleep(0.05)
    GPIO.output(13,True)
    sleep(0.05)
    GPIO.output(13,False)
    sleep(0.05)
    
for i in range(57,61):
    GPIO.output(25,True)
    sleep(0.05)
    GPIO.output(25,False)
    sleep(0.05)
    GPIO.output(18,True)
    sleep(0.05)
    GPIO.output(18,False)
    sleep(0.05)
    
for i in range(62,66): 
    GPIO.output(25,True)
    sleep(0.05)
    GPIO.output(25,False)
    sleep(0.05)
    GPIO.output(18,True)
    sleep(0.05)
    GPIO.output(18,False)
    sleep(0.05)
    GPIO.output(13,True)
    sleep(0.05)
    GPIO.output(13,False)
    sleep(0.05)
    
for i in range(67,69):
    GPIO.output(25,True)
    sleep(0.05)
    GPIO.output(25,False)
    sleep(0.05)
    GPIO.output(18,True)
    sleep(0.05)
    GPIO.output(18,False)
    sleep(0.05)
    
for i in range(70,75):
    GPIO.output(16,True)
    sleep(0.05)
    GPIO.output(16,False)
    sleep(0.05)
    GPIO.output(5,True)
    sleep(0.05)
    GPIO.output(5,False)
    sleep(0.05)

for i in range(76,81):
    GPIO.output(16,True)
    sleep(0.05)
    GPIO.output(16,False)
    sleep(0.05)
    GPIO.output(18,True)
    sleep(0.05)
    GPIO.output(18,False)
    sleep(0.05)
    GPIO.output(25,True)
    sleep(0.05)
    GPIO.output(25,False)
    sleep(0.05)
    GPIO.output(17,True)
    sleep(0.05)
    GPIO.output(17,False)
    sleep(0.05)
    
for i in range(82,90):
    GPIO.output(25,True)
    GPIO.output(18,True)
    GPIO.output(13,True)
    sleep(0.19)
    GPIO.output(25,False)
    GPIO.output(18,False)
    GPIO.output(13,False)
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.19)
    GPIO.output(25,False)
    GPIO.output(18,False)
    sleep(0.15)
    GPIO.output(25,True)
    sleep(0.05)
    GPIO.output(25,False)
    sleep(0.05)
    GPIO.output(18,True)
    sleep(0.05)
    GPIO.output(18,False)
    sleep(0.05)
    GPIO.output(13,True)
    sleep(0.05)
    GPIO.output(13,False)
    sleep(0.05)
    GPIO.output(13,True)
    GPIO.output(25,True)
    GPIO.output(5,True)
    sleep(0.15)
    GPIO.output(13,False)
    GPIO.output(25,False)
    GPIO.output(5,False)
    sleep(0.19)
    GPIO.output(18,True)
    GPIO.output(17,True)
    sleep(0.19)
    GPIO.output(18,False)
    GPIO.output(17,False)
    sleep(0.19)
    GPIO.output(13,True)
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.19)
    GPIO.output(5,True)
    sleep(0.15)
    GPIO.output(5,False)
    sleep(0.05)
    
for i in range(91,100):
    GPIO.output(25,True)
    GPIO.output(18,True)
    GPIO.output(16,True)
    sleep(0.29)
    GPIO.output(25,False)
    GPIO.output(18,False)
    GPIO.output(16,False)
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.29)
    GPIO.output(25,False)
    GPIO.output(18,False)
    sleep(0.3)
    GPIO.output(25,True)
    sleep(0.1)
    GPIO.output(25,False)
    sleep(0.1)
    GPIO.output(18,True)
    sleep(0.1)
    GPIO.output(18,False)
    sleep(0.1)
    GPIO.output(16,True)
    sleep(0.1)
    GPIO.output(16,False)
    sleep(0.1)
    GPIO.output(13,True)
    GPIO.output(25,True)
    GPIO.output(5,True)
    sleep(0.3)
    GPIO.output(13,False)
    GPIO.output(25,False)
    GPIO.output(5,False)
    sleep(0.29)
    GPIO.output(18,True)
    GPIO.output(17,True)
    sleep(0.29)
    GPIO.output(18,False)
    GPIO.output(17,False)
    sleep(0.29)
    GPIO.output(13,True)
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.29)
    GPIO.output(5,True)
    sleep(0.3)
    GPIO.output(5,False)
    sleep(0.1)

for i in range(101,105): 
    GPIO.output(25,True)
    GPIO.output(18,True)
    GPIO.output(16,True)
    sleep(0.4)
    GPIO.output(25,False)
    GPIO.output(18,False)
    GPIO.output(16,False)
    sleep(0.45)
for i in range(106,110):
    GPIO.output(25,True)
    GPIO.output(18,True)
    sleep(0.5)
    GPIO.output(25,False)
    GPIO.output(18,False)
    sleep(0.55)
for i in range(111,116):
    GPIO.output(25,True)
    sleep(0.6)
    GPIO.output(25,False)
    sleep(0.65)
    
    
for i in range (117,123):
    GPIO.output(25,True)
    sleep(0.7)
    GPIO.output(25,False)
    sleep(0.65)
    GPIO.output(18,True)
    sleep(0.85)
    GPIO.output(18,False)
    sleep(0.9)
    GPIO.output(17,True)
    sleep(0.95)
    GPIO.output(17,False)
    sleep(1)
   
   



    
