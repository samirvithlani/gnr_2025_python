seasons = {"SUMMER":{"morningTemp:":20,"noonTem":40,"eveningtemp":18},"WINTER":{"morningTemp:":5,"noonTem":20,"eveningtemp":12},
           "MONSOON":{"morningTemp:":12,"noonTem":25,"eveningtemp":20}}
average =0
sum=0
seasonavg ={}
for i,j in seasons.items():
    #print(f"{i}") #i ="" j ={}
    for x,y in j.items():
        #print(f"{x} {y}")
        sum = (sum + y) 
    #print(sum) 
    average = sum //3
    #print(f"avarage of  {i} = {average}")
    seasonavg[i] = average
    sum=0   
    average=0

print(seasonavg)    
        
    
    