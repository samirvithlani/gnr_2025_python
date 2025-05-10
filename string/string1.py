data = "amit kumar"
print(data)
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])

#how to find length of string

length = len(data)
print("lenth of string is", length)

#for i in range(0,length):
for i in range(0,len(data)):
    print(data[i])

#string is immutable
data[0] = "A"
print(data)    