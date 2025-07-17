
def toBeCalled():
    print("to be called........")

def demo(a):
    print("value of a ",a)
    #a == toBeCalled()
    a()


# demo(10)    
# demo("abc")    
# demo(False)    
# demo([])
# demo(())
demo(toBeCalled)
        
        