cricketers ={"virat":[78,89,101,123,44],"rohit":[176,12,0,56,90]}
sum=0
score={}
for i,j in cricketers.items():
    #print(f"{i} {j}") #virat rohit ,[] j == list
    for runs in j:
        print(runs)
        sum = sum+runs
    #print(f"sum of {i} = {sum}")    
    score[i]=sum
    sum=0

#score={""virat:435,roho:}    
print(score)
    