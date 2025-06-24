employees = {
    1: "Raj",
    2: "Simran",
    3: "Raj",
    4: "Aman"
}

# Task: Find and print names that are assigned to multiple employee IDs.

uniqueNames =[]
duplicateName=[]
for i,j in employees.items():
    if j not in uniqueNames:
        uniqueNames.append(j)
    else:
       #print("else...",j)
        duplicateName.append(j)    
        

print(uniqueNames)
print(duplicateName)        
    