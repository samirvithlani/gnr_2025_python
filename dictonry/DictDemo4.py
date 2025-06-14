employees= {"raj":34567,"parth":98765,"jay":12456}

#remove 
#1 y key

print(employees)
# x= employees.pop("parth") #keyerror ignore alway check if key present..
# print("removed value...",x)

x =employees.popitem() #it will remove last key value pair...
print("removing...",x)
print(employees)

