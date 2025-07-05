def add(a,b):
    print("add function called...")
    c = a+b
    return c


x= 100
y =200
ans = add(x,y)
print(f"ans = {ans}")

def getFullName(fname,lname):
    return fname + " " +lname


fullName = getFullName("rohit","sharma")
print(fullName)
print(getFullName("virat","kohli"))


#function returning boolean True False

def isValid(age):
    if age>=18:
        return True
    else:
        return False


flag = isValid(20)    
print(flag)

print(isValid(2))



if isValid(1):
    print("user is valid..")
else:
    print("user is not valid...")    

