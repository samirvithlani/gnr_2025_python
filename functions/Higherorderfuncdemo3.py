
def science(name):
    print(f"{name} your admission has been confirmed in science")
    

def comm(name):
    print(f"{name} your admission has been confirmed in comm")

def arts(name):
    print(f"{name} your admission has been confirmed in arts")    


def admission(cb,name):
    print(f" {name} welcome to admission window")
    cb(name)



name = input("enter name :")
pers = int(input("enter pers : "))

if pers>80:
    admission(science,name)
elif pers>70:
    admission(comm,name)    
elif pers>60:
    admission(arts,name)    
else:
    print("no admissino")    
