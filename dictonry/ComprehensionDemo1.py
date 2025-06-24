#{1:1,2:2,3:3,4:4,5:5}

# data ={}

# for i in range(1,6):
#     data[i]=i

# print(data)    

#i key : i value
# data = {i:i for i in range(1,6)}
# print(data)

# data = {i:i**2 for i in range(1,6)}
# print(data)


# users = ["ram","shyam","amit","kunal","jay","sumit"]
# #{r:"ram":"s":"shyam"}

# data = {i[0]:i for i in users}
# print(data)


# users = ["ram","shyam","amit","kunal","jay","sumit"]

# #{"ram":3,"shyam":5,"amit":4}
# data = {i:len(i) for i in users}
# print(data)


users = ["ram","shyam","naman","amit","kunal","racecar","bob","jay","sumit"]

data = {i:len(i) for i in users if len(i)>4}
print(data)


data = {i:i for i in users if i==i[::-1]}
print(data)


# sales = {"mobile":10000,"charger":2000,"cover":100}
# #
# #salesafterdis = {"mobile":"9000","charger":"1800"} 

# salesAfterdis = {i:sales[i] - sales[i]*0.1 for i in sales}
# print(salesAfterdis)


numbsers = [1,2,3,4,50,-1,2-3,-8,-7]
#{1:"pos"}

data= {i:"pos" if i>0 else "neg" for i in numbsers}
print(data)

users = ["ram","shyam","naman","amit","kunal","racecar","bob","jay","sumit"]

data = {i:"yes" if i == i[::-1] else "no" for i in users}
print(data)


att = {"raj":1,"parth":0,"jay":1,"kunal":1}

x = {i: "present" if att[i] == 1 else "absent" for i in att}
print(x)
#att = {"raj":"presnet"}

x



