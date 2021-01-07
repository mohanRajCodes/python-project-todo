import re
import requests
import random
from bs4 import BeautifulSoup

class getQuote:
    def __init__(self):
        self.url = "https://www.brainyquote.com/topics/only-quotes";
        self.respons = requests.get(self.url);
        self.Page = self.respons.content
        self.content = BeautifulSoup(self.Page,'html.parser');
        self.raw_quotes = self.content.find_all('a',attrs={'title':'view quote'});
        self.quoteLen  = len(self.raw_quotes);
        self.i=0;
        self.y="";
        self.count=0
    def checkInternet(self):
        if self.respons:
            pass
        else:
            return "No internet conection";
    def getRandomQuote(self):
        
        rndm=random.randrange(0,self.quoteLen);
        
        for x in re.sub('<a|</a>',' ',str(self.raw_quotes[rndm])):
            self.count = self.count+1;
            
            if x == ">":
                self.i=1;
            if self.i == 1:
                if self.count > 30 and x == " ":
                    self.count=0
                    self.y = self.y + '\n' + x;
                else:
                    self.y = self.y+x;

        return re.sub('>','',self.y);
                
        
        
