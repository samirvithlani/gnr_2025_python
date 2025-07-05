marks = [12,22,0,23,45,66,78]

# even list
# odd list

even=[i for i in marks if i%2==0]
odd =[i for i in marks if i%2==1]

# for i in marks:
#     if i %2 ==0:
#         even.append(i)
#     else:
#         odd.append(i)    

print(even)        
print(odd)