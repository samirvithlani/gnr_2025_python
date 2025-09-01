#abstract base class

from abc import ABC,abstractmethod

#abstract class
class TRAI(ABC):
    
    @abstractmethod
    def call(self):
        pass
    
    @abstractmethod
    def message(self,x):
        pass
        

class JIO(TRAI):
    
    def call1(self):
        print("jio calling...")

class Airtel(TRAI):
    
    def call2(self):
        print("airtel calling..")        
        
    
    def call(self):
        print("airtel calling..")            
    
    
    def message(self,x):
        print("message from airtle")    

a = Airtel()
a.call()        