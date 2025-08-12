#class name must starts with cap
class Test:
    
    def demo(self):
        print("demo function called..")
        print(self)
    def display(self,a,b):
        print(a,b)    
    
    def add(self,a,b):
        return a+b    
    

t = Test() #t -- obejct 
t.demo()  # t.demo(t)   
print(t)   
t.display(100,200) 
print(t.add(10,20))