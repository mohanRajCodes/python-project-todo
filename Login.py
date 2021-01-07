from tkinter import *
from tkinter import messagebox
from datetime import *
from tkcalendar import *
from xlsxwriter import Workbook

import passwordCheck
import dbIntiate
import saveToDo
import getToDo
import alterToDo
import re
import getQuoteWeb

class login:
	
	def __init__(self):
	
		def loginPlace():
		
			self.UserLabel.place(relx=0.2 ,rely=0.2 ,x=10,y=10)
			self.User.place(relx=0.2 ,rely=0.2 ,x=70,y=10)
			self.pwdLabel.place(relx=0.2 ,rely=0.2 ,x=10,y=40)
			self.pwd.place(relx=0.2 ,rely=0.2 ,x=70,y=40)
			self.submitButton.place(relx=0.2 ,rely=0.2 ,x=70,y=70)
			
		def name():
	
			self.Username = self.User.get();
			
			
			self.greeting = Label(self.master,text="Welcome, " + self.Username + "!");
			
			authenticate = passwordCheck.authentication(self.User.get(),self.pwd.get());
			result = authenticate.checkUsername();
		
			if result == "200":
				result = authenticate.checkpwd();
				if result == "404":
					messagebox.showinfo("Error","Password incorrect");
				else:
					destroy();
					show();
					clrWrk();
			else:
				messagebox.showinfo("Error","Invalid User");
		
		
		def addToDo():
			self.listToDo.insert(self.listToDo.size()+1,self.entryToDo.get());
		
		def saveWrk():
			if self.listToDo.size():
				save = saveToDo.saveList(self.listToDo.get(0,self.listToDo.size()),self.Username,self.datepicker.get());
				save.insertList();
		def delWrk():
			self.listToDo.delete(ANCHOR)
			alter = alterToDo.alterList(self.listToDo.get(0,self.listToDo.size()),self.Username,self.datepicker.get());
			alter.updateList()
			
		def clrWrk():
			self.listToDo.delete(0,END);
			self.User.delete(0,END); self.pwd.delete(0,END);
                    
		def getWrk():
	
			self.listToDo.delete(0,self.listToDo.size());
			get = getToDo.getList(self.Username);
			todo = get.getData(self.datepicker.get());
		
			for lis in todo:
				self.listToDo.insert(self.listToDo.size()+1,lis);
				
		def destroy():
			self.UserLabel.place(relx=1 ,rely=1);
			self.User.place(relx=1 ,rely=1);
			self.pwdLabel.place(relx=1 ,rely=1);
			self.pwd.place(relx=1 ,rely=1);
			self.submitButton.place(relx=1 ,rely=1);
	
		def show():
			for widget in self.master.winfo_children():
				widget.place(relx=1 ,rely=1);
			
			self.quote.place(relx=0.5,rely=0.05)

			self.greeting.place(relx=0.1 ,rely=0.2 ,x=1,y=1)
			self.datedisp.place(relx=0.1 ,rely=0.2 ,x=10,y=30)
		
			self.datepickLabel.place(relx=0.1 ,rely=0.2 ,x=180,y=30);
			self.datepicker.place(relx=0.1 ,rely=0.2 ,x=250,y=30);
			self.getButton.place(relx=0.1 ,rely=0.2 ,x=360,y=30);
		
		
			self.entryToDo.place(relx=0.2 ,rely=0.3 ,x=10,y=20)
			self.addButton.place(relx=0.2 ,rely=0.35 ,x=100,y=30)
		
			self.listToDo.place(relx=0.2 ,rely=0.45 ,x=10,y=15)
			self.saveButton.place(relx=0.2 ,rely=0.8 ,x=10,y=40)
			self.deleteButton.place(relx=0.2 ,rely=0.8,x=180,y=40)

			self.addUser.place(relx=0.3 ,rely=0.4 ,x=250,y=50);
			self.switchUser.place(relx=0.3 ,rely=0.5 ,x=250,y=50);
			self.export.place(relx=0.3 ,rely=0.6 ,x=250,y=50);		
		def addUser():
			for widget in self.master.winfo_children():
				widget.place(relx=1 ,rely=1);
			loginPlace();
			
			def newname():
				newuser = dbIntiate.dbConnect("user_details","authenticate");
				exists = newuser.findUser(self.User.get(),"name");
				if exists:
					messagebox.showinfo("Error","User already Exist");
					
				else:
					newuser.insertUser(self.User.get(),self.pwd.get());
					destroy();
					self.loginButton=Button(self.master,text="Log in",command=loginPlace);
					self.loginButton.place(relx=0.8,anchor=NW);
					self.submitButton.destroy()
					self.submitButton=Button(self.master,text="Submit",command=name);
					self.cancelButton.destroy()
					
			self.submitButton.destroy()
			self.submitButton=Button(self.master,text="Submit",command=newname);
			self.submitButton.place(relx=0.2 ,rely=0.2 ,x=70,y=70)
			self.cancelButton=Button(self.master,text="Cancel",command=show);
			self.cancelButton.place(relx=0.4 ,rely=0.2 ,x=40,y=70)
			
		def switchUser():
			self.UserLabel=Label(self.master,text="Username")
			self.User=Entry(self.master);
			self.pwdLabel=Label(self.master,text="Password")
			self.pwd=Entry(self.master,show="*");
			self.submitButton=Button(self.master,text="Submit",command=name);
			for widget in self.master.winfo_children():
				widget.place(relx=1 ,rely=1);
			loginPlace();
			self.listToDo.delete(0,self.listToDo.size());
		
		def export2Excel():
			print ("todo_" + str(self.Username) + "_" + str(self.datepicker.get()));
			filename = "todo_" + self.Username + "_" + self.datepicker.get() + ".xlsx"; 
			print(filename);
			actual_filename = re.sub('/',  '_', filename)
			
			if self.listToDo.size():
				ex_work = self.listToDo.get(0,self.listToDo.size())
				workbook = xlsxwriter.Workbook(actual_filename); 

				worksheet = workbook.add_worksheet() 
				
				worksheet.write('A1', 'User:' + str(self.Username) ) 
				worksheet.write('B1', 'Date:' + str(self.datepicker.get()));
				worksheet.write('A2', "To Do"); 
				i=3;
				for listing in ex_work:
					worksheet.write('A' + str(i), listing) 
					i=i+1;
					
				workbook.close();
				
		def getQuote():
			print("i am in quote");
			rand = getQuoteWeb.getQuote();
			quote = rand.getRandomQuote();
			print(quote)
			return quote;
			
		
			

		
			
		self.master = Tk();
		self.master.geometry("500x700");
		self.master.title("Todo App")
		
		self.loginButton=Button(self.master,text="Log in",command=loginPlace);
		self.loginButton.place(relx=0.8,anchor=NW);
		
		self.Username="Anonymous"
		self.UserLabel=Label(self.master,text="Username")
		self.User=Entry(self.master);
		
		self.pwdLabel=Label(self.master,text="Password")
		self.pwd=Entry(self.master,show="*");
		
		self.submitButton=Button(self.master,text="Submit",command=name);
		
		self.datedisp = Label(self.master,text="Date: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"));
		
		self.datepickLabel  = Label(self.master,text="Date Picker");
		self.datepicker = DateEntry(self.master);
		self.getButton = Button(self.master,text="Get",command=getWrk);
		
		self.listToDo = Listbox(self.master ,bg="white" , font="Arial")
	
		self.entryToDo = Entry(self.master,bg="#33FFBD", font="vedanta")
		
		self.addButton = Button(self.master,text="Add",command=addToDo);
		self.saveButton = Button(self.master,text="Save",command=saveWrk);
		self.deleteButton = Button(self.master,text="Delete",command=delWrk);

		self.addUser = Button(self.master,text=   "  Add User " ,command=addUser);
		self.switchUser = Button(self.master,text="Switch User" ,command=switchUser);

		self.export  = Button(self.master,text=   "  Export   ",command=export2Excel);

		self.quote = Label(self.master,text="Quote of the day:\n" + getQuote());
		
			
###LOGIN OBJECT####
login();




				
                     
                     
                    
                     
                
                     
    

