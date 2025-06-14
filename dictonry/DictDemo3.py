# users={} #name:a

# while True:
#     choice = input("enter y for con... and n for exit..")
#     if choice == 'y':
#         name = input("Enter Name :")
#         age = int(input("Enter AGe :"))
#         users[name]=age
#     elif choice =="n":
#         print("Thanks...")        
#         break
#     else:
#         print("invalid choice...")    
#         break

# print(users)    
    
users={} #name:a

while True:
    choice = input("enter y for con... and n for exit..")
    if choice == 'y':
        name = input("Enter Name :")
        age = int(input("Enter AGe :"))
        #check key is already there or not..
        if name in users:
            print("name is already taken....")
        else:    
            users[name]=age
    elif choice =="n":
        print("Thanks...")        
        break
    else:
        print("invalid choice...")    
        break

print(users)    
        