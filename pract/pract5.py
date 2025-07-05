lang = ["gujarati","hindi","english","marathi","tamil","telugu"]

# data= {"gujarati":8,....}
#x ={i:len(i) for i in lang}
#x ={i[0]:i for i in lang}

# for i in lang:
#     #print(i,len(i))
#     x[i] = len(i)
x = {}
for i in lang:
    x[i[0]] = i
print(x)    

#data = {"g":"gujarati","h":"hindi"...}