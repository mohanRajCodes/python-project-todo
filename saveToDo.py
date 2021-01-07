import dbIntiate

class saveList:
    def __init__(self,listTodo,user,date):
        self.listTodo = listTodo;
        self.dte = date;
        self.usr = user;
        self.save = dbIntiate.dbConnect("ToDo_details","lists")
        print(self.listTodo)
    def insertList(self):
        exists = self.save.findOne(self.dte,'date',self.usr);
        if exists:
            self.save.updateOne(self.listTodo,self.usr,self.dte);
        else:
            self.save.insertMany(self.listTodo,self.usr);
    
        
    
