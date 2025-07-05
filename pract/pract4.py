#find max element from list
sales = [100,222,345,678,900,1,987,1000,1200,154]
maxno = sales[0]

for i in sales:
    if i>maxno:
        maxno = i

print(maxno)        

print(f"max = {max(sales)}")

