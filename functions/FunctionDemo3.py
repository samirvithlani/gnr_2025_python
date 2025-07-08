x1 = [1,2,3]
x2 = [4,5,6]

#x3 = x1 + x2
#print(x3)
x3 =[]
for i in range(0,len(x1)):
    sum = x1[i]+x2[i]
    x3.append(sum)
    sum =0

print(x3)    
    