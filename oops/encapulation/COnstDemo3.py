class Employee:
    
    def __init__(self,*args):
        self.args = args
    
    def getEmployees(self):
        print(self.args)    


emp = Employee("ram","shyam","amit")        
emp.getEmployees()