data = {1:"ram",2:"amit",3:"raj"}
data[4]="ajay"

data.update({5:"kunal",6:"seeta",2:"AMIT"})

k = data.keys()
print("keys = ",k) # object[]

v = data.values()
print(f"values = {v}")

kv = data.items()
print(f"kv ={kv}")

#iter

for i,j in data.items():
    print(f"{i} {j}")