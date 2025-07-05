#without return type without args
def test():
    print("test function called...")

#with param with return type..
def greet(name):
    print(f"Hello {name}")


test() #funcition calling part...    
greet("Virat")
greet(12)
greet(False)
greet([10,20])