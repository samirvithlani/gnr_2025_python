# chance =3

# while chance>0:
#     amount = int(input("enter balance"))
#     if amount<10000:
#         chance-=1
#     else:
#         print("amount = ",amount)
#         break  

# if chance ==0:
#     print("try again l....")      


for i in range(1,4):
    amount = int(input("enter bal"))
    if amount>=10000:
        print("amount = ",amount)
        break

if i ==3:
    print("try again,,")   