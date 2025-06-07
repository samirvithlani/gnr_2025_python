# data=[] #empty

# for i in range(1,11):
#     data.append(i)

# print(data)    

data = [i for i in range(1,11)]
print(data)

users = ["amit","sumit","ram","seeta","shyam","sneha","dev"]
# slist =[]

# # for i in users:
# #     if i.startswith("s"):
# #         slist.append(i)

slist =[i for i in users if i.startswith("s")]
print(slist)        

users = ["bob","naman","madam","ajay","raj","aa"]
palindrome=[i for i in users if i == i[::-1]]

# for i in users:
#     #bob == bob
#     #ajay == yaja
#     if i == i[::-1]:
#         palindrome.append(i)

print(palindrome)

# name = "bob"
# # x = name[::-1]
# # print(x)

# if name == name[::-1]:
#     print("name is palindrome..")