sales = [100,222,345,678,900,1,987,1000,1200,154]
#{100:110,222:244}

salesprofit = {i:i+ (i*0.1) for i in sales}

# for i in sales:
#     salesprofit[i] = i + i * 0.10

print(salesprofit)    