# Two dictionaries with item prices
shop1 = {"Pen": 10, "Notebook": 40}
shop2 = {"Pen": 12, "Pencil": 5}

# Task: Merge both dictionaries. If same item exists, keep the lowest price.

#x = shop1 | shop2
#print(x)

x = {}
for key in shop1:
    x[key] = shop1[key]


for key in shop2:
    
    if key in x:
        if shop2[key]<x[key]:          
            x[key] = shop2[key]
        else:
            x[key] = shop1[key]
            print(x[key])

print(x)                           
