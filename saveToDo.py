import dbIntiate

class saveList:
    def __init__(self,listTodo):
        self.listTodo = listTodo;
        self.save = dbIntiate.dbConnect("ToDo_details","lists")
    
