# def outer():
#     print("outer called..")
    
#     def inner():
#         print("inner function called..")

#     inner()

# outer()


def outer(x):
    
    def inner(no1):
        inner1 = 1000
        print(f"x = {x}")
        print(f"innder1 = {inner1}")
    inner(100)
    
    #print("iiner1 =",inn)    error..

outer(1000)    
        
        
        