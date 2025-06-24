#list
#tuple index ...
#dict key:value...
#homg.. address 101-->104
#set: set hashtable.. DS : set unordered
#set does not allow duplicate elm...
#set is not subscriptable..
#list [], tuple (),dict ={}, set() -> {}

data = {100,20,30,40,111,234,678,20,40}
print(data)
print(type(data))
print(type(data).__name__)

# for i in range(0,len(data)):
#     print(data[i])


for i in data:
    print(i)