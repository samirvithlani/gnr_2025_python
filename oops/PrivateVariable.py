class Demo:

    def __init__(self):
        print("demo class const called..")
        self.pub = 100 #public
        self.__pvt = 200 #private variable..
    
    
    def display(self):
        print("pub  = ",self.pub)    #same class
        print("private = ",self.__pvt) #same class
        self.__getData() #same class
    
    def __getData(self):
        print("this is pvt method")    

d = Demo()
d.display()
print(d.pub) #outside of class 
#print(d.__pvt) error 
d.__getData()