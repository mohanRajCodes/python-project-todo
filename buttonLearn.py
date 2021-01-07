#####Button#####

from tkinter import *
import tkinter
#import tkMessageBox
from tkinter import messagebox


top = Tk("Hello","Hello")



def sayHello():
    #messagebox = "Hello World !!!"
    #Text = "Hello "
    #Message = "Hello Message"
    #tkinter.messagebox.showinfo("Hellow", "World");
    messagebox.showinfo("Heelo","Heelllo");
    

B = Button(top,text="Hello",command=sayHello);
B.pack()
B.flash();
top.mainloop()    

# Importing tkinter module 
from tkinter import *
from tkinter.ttk import *

# creating Tk window 
master = Tk() 

# setting geometry of tk window 
master.geometry("200x200") 

# button widget 
b1 = Button(master, text = "Absolute !") 
b1.place( x =100, y = 10 )

b3 = Button(master, text = "Relative !") 
b3.place( relx =0.5, y = 50 ,anchor= NW)

# label widget 
l = Label(master, text = "I'm a Label") 
l.place(anchor = NW) 

# button widget 
b2 = Button(master, text = "GFG") 
b2.place(relx = 0.5, rely = 0.5, anchor = CENTER) 

# infinite loop which is required to 
# run tkinter program infinitely 
# until an interrupt occurs 
mainloop() 
