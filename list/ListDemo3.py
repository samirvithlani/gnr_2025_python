sales  =[100,20,30,45,67]
print(sales)
#removedELm = sales.pop() #it will remove last
if len(sales)>0:
    removedELm = sales.pop(2) #it will remove last
    print("removing...",removedELm)
else:
    print("list is empty,,")    

print(sales)

sales.remove(45)
print(sales)