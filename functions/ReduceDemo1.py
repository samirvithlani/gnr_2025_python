from functools import reduce
marks = [10,20,30,40,50]

# total = 0
# for i in marks:
#     total+=i

#10,20 - 30
#30,40 ->70
#7050
total = reduce(lambda x,y:x+y,marks)

print(total)    

users = ["ram","shyam","amit","sumit"]

users1 = reduce(lambda x,y:x+"-"+y,users)
print(users1)
