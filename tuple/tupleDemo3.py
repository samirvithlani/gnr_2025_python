doc = ("aadharcard","pancard")
#convert this to list...
docList = list(doc) #tuple to list
print(docList)
docList.append("passport") 
doc = tuple(docList) #list to tuple
print(doc)

x = (1,2,3)
y = (4,5,6)

ans = x + y
print("ans =" ,ans)