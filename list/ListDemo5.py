sales = [100,20,233,45,67,890,289,901,987,89,56,28,9,78,1000,7654]
users= ["amit","sumit","ajay","raj","ajay","parth","amit"]
uniquie_users = []
duplicate_user=[]
for i in users:
    #amit
    #sumit
    #ajay
    #raj
    #ajay
    if i not in uniquie_users:
        uniquie_users.append(i)
    else:
        duplicate_user.append(i)    
print("users",uniquie_users)
print("duplicate_user",duplicate_user)

# bigger = max(sales)
# print("bigger", bigger)


sales.sort(reverse=True)
print("sales", sales[0])


users= ["amit","sumit","ajay","raj","ajay","parth","amit"]

users.remove("ajay")
print(users)
#please enter name to remove

for i in users:
    if "sumit" in i:
        users.remove("sumit")
    
            

print(users)    