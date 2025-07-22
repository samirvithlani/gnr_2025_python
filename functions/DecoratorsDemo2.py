no1 = int(input("enter no 1"))
no2 = int(input("enter no 2"))


def safeDiv(func): #func == div
    
    def inner():
        if no2 ==0:
            print("can not divide by zero")
        else:
            func() #div   

    return inner

@safeDiv
def div():
    print(f"div = {no1/no2}")


div()    