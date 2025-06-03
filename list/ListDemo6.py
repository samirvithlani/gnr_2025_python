data = [["virat",100],["sachin",200],["ms",183]]

# for i in range(0,len(data)):
#    # print(data[i])#[],[],[]
#     for j in range(0,len(data[i])):
#         print(data[i][j],end=" ")
#     print()  # for new line after each inner list

# for i in data: 
#     for j in i:
#         print(j, end=" ")
#     print()  # for new line after each inner list

for i,j in data:
    print(i, j, end=" ")
    print()    

print(data[0][0])
print(data[1][1])
    