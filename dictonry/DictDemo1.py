# data= {} #empty dict #[] , ()
# print(data)

data = {1:"ram",2:"shyam",3:"krihna"}
print(data)


#print(data.get(11))
#print(data[1])
# print(data[11]) #keyerror

k = data.keys() # object of all keys
#print(k)
print(list(k))

v = data.values()
print(v)
print(list(v))


kv = data.items() #kv [(),(),(),(),()]
print(kv)

for i,j in data.items():
    print(f"{i} {j}")
