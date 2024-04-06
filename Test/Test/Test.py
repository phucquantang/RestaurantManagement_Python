
from tkinter import *

mywindow = Tk() #Change the name for every window you make
mywindow.title("New Project") #This will be the window title
mywindow.geometry("780x640") #This will be the window size (str)
mywindow.minsize(540, 420) #This will be set a limit for the window's minimum size (int)
mywindow.configure(bg="blue") #This will be the background color

mywindow.mainloop() #You must add this at the end to show the window