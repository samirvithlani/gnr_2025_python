#named param func

def getUserData(x,name,age,salary,city):
    print(f"name = {name}")
    print(f"age = {age}")
    print(f"salary = {salary}")
    print(f"city = {city}")
    print(f"x = {x}")

#getUserData("ram",23,2300)    
#getUserData(23,2300,"ram")    
#getUserData(name="ram",salary=2300,age=23,"ahmedbad") error
getUserData(100,name="ram",salary=2300,age=23,city="ahm")