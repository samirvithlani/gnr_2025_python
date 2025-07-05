#remove duplicate element from list

users = ["raj","jay","parth","raj","jay","amit","jay"]

uniqueelm =[]

for  i in users:
    if i not in uniqueelm: #raj,jay,parth,raj,amit
        uniqueelm.append(i) #["raj","jay","parth","amit"]

print(uniqueelm)    
    