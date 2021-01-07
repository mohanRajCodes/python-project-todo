import dbIntiate

class deleteList:
    def __init__(self,listTodo,user):
        self.listTodo = listTodo;
        self.usr = user;
        self.save = dbIntiate.dbConnect("ToDo_details","lists")
        print(self.listTodo)
    def insertList(self):
        self.save.insertMany(self.listTodo,self.usr);
    
        
    
