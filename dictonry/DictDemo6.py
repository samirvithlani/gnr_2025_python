users = {"raj":87,"parth":83,"jay":77,"ajay":54,"kunal":88}

maxValue = max(users.values())
print(maxValue) #88
userName =""
#print(users["parth"])
for i,j in users.items():#i = "raj" j = 87 i = kunal j = 88
    if j == maxValue: #87 == 88 88 ==88
        userName = i #kunal
print(userName)        