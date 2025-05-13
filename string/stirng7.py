name = "java is programming language"

ind = name.index("a")
#ind = name.index("a",4)
print("index of chr ",ind)

#manual approch 
#if char found --> index
#if not --> -1


flag = -1
name = "java"
for i in range(0,len(name)):
    if name[i] == "a":
        flag = i #1
        #break

print(flag)        