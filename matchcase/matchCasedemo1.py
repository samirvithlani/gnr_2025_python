print("press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division")
choice = int(input("Enter your choice: "))


match choice:
    case 1:
        print("enter two numbers for addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = a + b
        print("Addition of", a, "and", b, "is", c)
    case 2:
        print("enter two numbers for subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = a - b
        print("Subtraction of", a, "and", b, "is", c) 
    case _:
        print("Invalid choice")       