# Write your code here :-)
import sys
import os
from time import sleep
from tkinter import *
from tkinter import messagebox
 
# initialise main window
def init(win):
    win.title("LED application")
    win.minsize(500, 100)
    btn.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()


# button callback
def option1():
    os.system('python LED+.py')

# button callback
def option2():
    messagebox.showinfo("option2", "you got the wrong one.")

# button callback
def option3():
    messagebox.showinfo("option3", "playing variation 2.")
    os.system('python LED2+.py')
    
# button callback
def option4():
    messagebox.showinfo("option3", "playing long version.")
    os.system('python LED+.py')
    os.system('python LED2+.py')
    
# button callback
def option4():
    messagebox.showinfo("option4", "playing faster")
    os.system('python LED3+.py')

# button callback
def option5():
    messagebox.showinfo("option5", "playing even faster")
    os.system('python LED4+.py')
    sleep(0.2)
    messagebox.showinfo("User Info", "But there's more")
    sleep(0.2)
    os.system('python LED5+.py')
    sleep(0.1)
    messagebox.showinfo("User Info", "Starting slowdown")
    os.system('python LED6+.py')

# create top-level window
win = Tk()

 
# Gets the requested values of the height and widht.
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(win.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(win.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
win.geometry("+{}+{}".format(positionRight, positionDown))
 
btn = Button(win, text="This is my LED project", command=option1)

btn2 = Button(win, text="You chose the wrong one", command=option2)

btn3 = Button(win, text="Playing Variation 2", command=option3)

btn4 = Button(win, text="Playing Faster", command=option4)

btn5 = Button(win, text="Playing Even Faster", command=option5)

# initialise and start main loop
init(win)
mainloop()

messagebox.showinfo("Final", "Thank you.")
os.system('Final.py')

