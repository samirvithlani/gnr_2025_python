scores = (["virat",10,20,30,10],["ms",120,30,30,45],["rohit",25,45,0,23,34])
sum=0
players =[]
for i in range(0,len(scores)): #["virat",10,20,30,10],["ms",120,30,30,45]
    for j in range(1,len(scores[i])):#[10,20,30,10],[120,30,30,45]
        sum = sum + scores[i][j] #10,20,30,10 ,120,30,30,45
    players.append([scores[i][0],sum]) #[["virat",70],["ms",225]]
    sum=0

print(tuple(players))    