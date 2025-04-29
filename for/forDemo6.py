#fibonacci sequence
a = 0
b = 1

# 0  1  1  2  3  5 
print(a, " ",b, end=" ") # 0 1
for i in range(1,10):
    sum = a + b # 0 + 1 = 1 # 1 + 1 =2 # 1 + 2 = 3 # 2 + 3 = 5 , # 3 + 5 = 8
    print(" ", sum, end=" ")   # 1 # 2 # 3 5 8
    a = b # a = 1 , a =1 , a = 2 , a = 3
    b = sum #b = 1 , b = 2 , b = 3 , b = 5
   