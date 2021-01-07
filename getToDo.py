import dbIntiate
import json

class getList:
    def __init__(self,user):
        self.usr = user;
        self.save = dbIntiate.dbConnect("ToDo_details","lists");
        self.output = {};
    def getData(self,dateIn):
        print(dateIn);
        self.output = self.save.findOne(dateIn,"date",self.usr);
        return self.output['listing']
        
        
        
        
