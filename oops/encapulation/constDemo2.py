class User:
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def getUserDetail(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"salary = {self.salary}")    

u1 = User("amit",22,1200)        
u1.getUserDetail()

u2 = User("raj",30,60000)
u2.getUserDetail()
        