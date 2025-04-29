sp =int(input("Enter starting point: "))
ep =int(input("Enter ending point: ")) #20

for i in range(sp,ep+1):
    if i %2 ==0:
        print(i,end=" ")