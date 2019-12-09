import dbIntiate
import json
class authentication:

    
    def __init__(self,usr,pwd):
        self.pwd = pwd
        self.usr = usr
        self.output = {};

    def checkpwd(self):
        print(self.pwd);
        #print(self.output);
        print(self.output['password'])
        if self.pwd == self.output['password'] :
            return "200"
        else:
            return "404"
    
    def checkUsername(self):
        #print(self.usr);
        checkuser = dbIntiate.dbConnect("user_details","authenticate")
        print ("here i come")
        
        self.output = checkuser.findOne(self.usr)
        if self.output:
            if self.output['name'] == self.usr:
                return "200"
        else:
            return "404"
        #print(output['password'])
        #print(json.dump(output))
        #print("Hello " + str(checkuser.findOne(self.usr)))
        #return "OK"
    

        
