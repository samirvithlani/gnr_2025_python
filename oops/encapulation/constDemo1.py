class User:
    
    def __init__(self): #self == u
        self.name = "amit" #u.name = "amit"
        self.age = 22
        self.salary=12000
        print("user class default const called...")

    def getUserDetail(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"salary = {self.salary}")

u = User() #default const..        
#u = User(u) #default const..
u.getUserDetail()        

u1 = User()
u1.getUserDetail()
