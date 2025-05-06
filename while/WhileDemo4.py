# 153
# 1 + 5 + 3
#1 + 125 + 27 = 153

no = 1634
ans =0

#count
count=0
temp1 =no

while temp1>0:
    temp1 = temp1//10
    count+=1

print(count)    


while no>0:
    rem = no %10 
    ans = ans + (rem**count)
    no = no //10

print(ans)    

#1634
#1 + 1296 _+ 81 + 256 = 1634