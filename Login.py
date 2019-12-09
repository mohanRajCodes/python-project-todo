from tkinter import *
from tkinter import messagebox
from datetime import *

import passwordCheck
import dbIntiate
import saveToDo

master = Tk();
master.geometry("500x500");
master.title("Todo App")

def loginCheck():
    UserLabel.place(relx=0.2 ,rely=0.2 ,x=10,y=10)
    User.place(relx=0.2 ,rely=0.2 ,x=70,y=10)
    pwdLabel.place(relx=0.2 ,rely=0.2 ,x=10,y=40)
    pwd.place(relx=0.2 ,rely=0.2 ,x=70,y=40)
    submitButton.place(relx=0.2 ,rely=0.2 ,x=70,y=70)

def name():
    #print("I am in");
    #print(User.get());
    #print(pwd.get());
    Username = User.get();
    greeting = Label(master,text="Welcome, " + Username + "!");
    
    authenticate = passwordCheck.authentication(User.get(),pwd.get());
    result = authenticate.checkUsername();
    #print(result);
    if result == "200":
        result = authenticate.checkpwd();
        if result == "404":
            messagebox.showinfo("Error","Password incorrect");
        else:
            destroy();
            show(greeting);
    else:
        messagebox.showinfo("Error","Invalid User");
        
    #print(result);

def destroy():
    UserLabel.destroy();
    User.destroy();
    pwdLabel.destroy();
    pwd.destroy();
    submitButton.destroy();

def show(greeting):
    greeting.place(relx=0.1 ,rely=0.1 ,x=1,y=1)
    datedisp.place(relx=0.1 ,rely=0.1 ,x=10,y=30)
    
    getToDo.place(relx=0.2 ,rely=0.2 ,x=10,y=20)
    addButton.place(relx=0.7 ,rely=0.2 ,x=10,y=20)
    
    listToDo.place(relx=0.2 ,rely=0.3 ,x=10,y=20)
    saveButton.place(relx=0.2 ,rely=0.8 ,x=10,y=20)
    

def addToDo():
    #print("hellllo" + str(listcount))
    #listcount=listcount+1;
    #print(listcount)
    print(listToDo.size());
    listToDo.insert(listToDo.size()+1,getToDo.get());
    print(listToDo.get(0,listToDo.size()))

def saveWrk():

    if listToDo.size():
        save = saveToDo.saveList(listToDo.get(0,listToDo.size()))
    
loginButton=Button(master,text="Log in",command=loginCheck);
loginButton.place(relx=0.8,anchor=NW);

###LOGIN####
listcount=0;
UserLabel=Label(master,text="Username")
User=Entry(master);

pwdLabel=Label(master,text="Password")
pwd=Entry(master,show="*");

submitButton=Button(master,text="Submit",command=name);

datedisp = Label(master,text="Date: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"));

listToDo = Listbox(master ,bg="white" , font="Arial")

getToDo = Entry(master,bg="#33FFBD", font="vedanta")

addButton = Button(master,text="Add",command=addToDo);
saveButton = Button(master,text="Save",command=saveWrk);
    

