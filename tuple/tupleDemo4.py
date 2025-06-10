#team
#playername role
team = (("virat","batsman"),("pandya","all rounder"),("bummrah","bowler"))
# print(team)
# print(team[0][1])

# for i in range(0,len(team)):
#     #print(team[i]) # tuple("virat","bt")
#     for j in range(0,len(team[i])):
#         print(team[i][j],end=" ")
#     print()    


# for i in team:
#     for j in i:
#         print(j,end=" ")
#     print()    

for i,j in team:
    print(f"{i} {j}")