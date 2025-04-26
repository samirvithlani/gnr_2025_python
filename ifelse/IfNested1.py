age = int(input("enter age"))

if age>=18:
    print("you are eligible for voting...")
    
    if age>=21:
        print("you are eligible for marrige..")
        
        if age>=60:
            print("you are eligible for retirement...")
        else:
            print("you are Not eligible for retirement...")           
    else:
        print("you are not eligible for marrige..")    
else:
    print("you are not eligible for voting..")
    
    if age>14:
        print("you are eligible for learning lic..")    
    else:
        print("stay at home...")    