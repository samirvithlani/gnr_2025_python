class Parent:
    
    def __init__(self):
        self.amount =1000 #instance variable...
        
    def calling(self):
        print("calling function of parent class called !!")



class Child(Parent):
    
    def __init__(self):
        #parent class const...
        print("default const..")
        super().__init__() # parent class const calling...
    
    def message(self):
        print("child class message called..",self.amount) 


c = Child() #child class obj..               
c.message()