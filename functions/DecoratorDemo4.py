def checkString(func):
    def inner(name): #amit
        if len(name)>0: #true
            func(name.upper()) #getName("amit")
        else:
            print("name is not valid")        
    
    return inner


@checkString
def getName(name):   #line 4 "AMIT"     
    print("name - ",name)

getName("abc")    