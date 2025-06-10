data = [100,2,-90,87,-100,56]
#[positive,pos,nef,pos,neg,pos]
datamsg =["POSITIVE" if i>0 else "NEGETIVE" for i in data]
# for i in data:
#     #i=100
#     #2 = 
#     #90
#     if i>0:
#         datamsg.append("POSITIVE")
#     else:
#         datamsg.append("NEGETIVE")    

print(datamsg)        


data2 = [1,2,3,4,5,6,7,8,9,10]
datamsg2 = ["even" if i %2==0 else "odd" for i in data2]
print(datamsg2)