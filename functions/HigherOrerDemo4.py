def add(*args):
    #(add--address..,10,20,30,40)
    sum = 0
    for i in args[1:]:  # start from index 
        sum += i
    print("sum:", sum)

def sub(*args):
    #(add--address..,10,20,30,40)
    sub = 0
    for i in args[1:]:  # start from index 
        sub += i
    print("sub:", sub)

def calc(*args):
    #(add--address..,10,20,30,40)
    args[0](*args)


calc(add,10,20,30,40)
calc(sub,1000,20,30,40,56,90)