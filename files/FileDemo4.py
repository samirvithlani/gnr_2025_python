name = input("enter name :")
age = int(input("enter age :"))

with open("files/user.txt","a") as file:
    file.write(f"\nName = {name}")
    file.write(f"\nage = {age}")
    print("user data write successfully in file...")

#file.write("end")     #error file close...