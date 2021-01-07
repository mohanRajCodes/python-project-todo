import pymongo
from datetime import *
from tkinter import messagebox

class dbConnect:
    def __init__(self,db,coll):
        print (db,coll)
        client = pymongo.MongoClient();
        self.database = client[db];
        self.collection = self.database[coll]
        #self.collection = coll = self.database.posts;
        #col = self.database.posts
        #user = {
         #   "name" : "mohan",
          #  "password" : "raj"
           # }
        #self.collection.insert_one(user)

    def findUser(self,value,key):
        #print("hello i am finding "+str(value) + " "  + str(self.collection)
              
        #print(self.collection.find_one({'name': value }))
        return self.collection.find_one({key: value})

    def insertUser(self,user,pwd):
            
            col = self.database.posts
            user = {
                "name" : user,
                "password" : pwd
                }
            self.collection.insert_one(user)
                
    def findOne(self,value,key,usr):
        #print("hello i am finding "+str(value) + " "  + str(self.collection)
              
        #print(self.collection.find_one({'name': value }))
        return self.collection.find_one({key: value ,'user':usr})
            

    def insertMany(self,listto,usr):
        
        listing = {
            "user" : usr,
            "listing" : listto,
            "date" : datetime.now().strftime("%m/%d/%y")
            }
        self.collection.insert_one(listing)

    def updateOne(self,listto,usr,date):

        print("update")
        print(listto);
        newvalues = { "$set": { "listing" : listto} }
        print(newvalues)
        self.collection.update_one({'user': usr,'date':date},newvalues);
        
