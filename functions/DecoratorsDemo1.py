#decorators are pure python function which will accept other function as argument
#and return one function object
#decorators are used to add functionality to existing functions
#decorators denoted by @ symbol
noofpers = 10
def order_food(func): #3 func == throw_party function
    
    def inner(): #6
        
        if noofpers>=100:
            print("no party")
        else:    
            print("ordering food...") #7
            func() #throw_party() #8
            
    
    return inner #4   



@order_food #2 #5
def throw_party(): #9
    print("Let's throw a party!") #10

throw_party()#1    