#args is not keywords
def getStudents(*args):
    #args dt --> tuple
    print(args)

#getStudents("parth","raj","amit","sumit")    
getStudents("raj",12,"ram",[],())    


# def getStudentDat1(*students,x):
#     print(students)
#     print(x)

# getStudentDat1("ram","shyam")    error

# def getStudentDat1(x,*students):
#     print(students)
#     print(x)

# getStudentDat1("ram","shyam","jay")    

def getStudentDat1(*students,x):
    print(students)
    print(x)

getStudentDat1("ram","shyam",x="jay")   

 