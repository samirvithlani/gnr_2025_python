# with open("files/user.txt","r") as file:
#     #x = file.read()
#     x = file.read(5)
#     print(x)


# with open("files/user.txt","r") as file:
#     x = file.readline()
#     print(x)

# count=0
# with open("files/user.txt","r") as file:
#     while True:
#         x = file.readline() #6
#         print(x,end="")
#         count+=1 #7
#         if not x: 
#             break
#     print("total lines =",count-1)    



with open("files/user.txt") as file:
    for i in file:
        print(i,end="")