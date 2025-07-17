
def science(name):
    print(f"{name} your admission has been confirmed in science")
    return "science"
    
    

def comm(name):
    print(f"{name} your admission has been confirmed in comm")
    return "comm"

def arts(name):
    print(f"{name} your admission has been confirmed in arts")    
    return "arts"


def admission(cb,name):
    print(f" {name} welcome to admission window")
    # stream = cb(name)
    # #print("selected stream  was ",stream)
    # return stream
    return cb(name)



name = input("enter name :")
pers = int(input("enter pers : "))
selectedStream  = None

if pers>80:
    selectedStream = admission(science,name)
elif pers>70:
    selectedStream = admission(comm,name)    
elif pers>60:
    selectedStream = admission(arts,name)    
else:
    print("no admissino")    


print(selectedStream)