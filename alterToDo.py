import dbIntiate

class alterList:
    def __init__(self,listTodo,user,date):
        self.listTodo = listTodo;
        self.dte = date;
        self.usr = user;
        self.save = dbIntiate.dbConnect("ToDo_details","lists")
        print(self.listTodo)
    def updateList(self):
        self.save.updateOne(self.listTodo,self.usr,self.dte);
    
        
    
