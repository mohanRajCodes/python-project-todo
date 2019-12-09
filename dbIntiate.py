import pymongo 

class dbConnect:
    def __init__(self,db,coll):
        print (db,coll)
        client = pymongo.MongoClient();
        self.database = client[db];
        self.collection = self.database[coll]
        #self.collection = coll = self.database.posts;
        #col = self.database.posts
        #user = {
        #    "name" : "mohan",
        #    "password" : "raj"
        #    }
        #self.collection.insert_one(user)
        
    def findOne(self,value):
        #print("hello i am finding "+str(value) + " "  + str(self.collection)
              
        #print(self.collection.find_one({'name': value }))
        return self.collection.find_one({'name': value })
            

    def insertMany(self,):    
