data = {"Gujarat":"Gandhinagar","Karnatak":"Benglore","Mahrashtra":"Mumbai","Assam":"dispur","Goa":"Panji"}
#single kv pair

data["Rajsthan"]="jaipur"
print(data)
data["Gujarat"]="Ahmedabad"
print(data)


data.update({"UP":"Lucknow","Bihar":"Patna"})
print(data)