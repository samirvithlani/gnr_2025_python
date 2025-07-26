data = [1,2,3,4,5]
sqrdata = []

# for  i in data:
#     sqrdata.append(i**2)


#sqrdata = [i**2 for i in data]

sqrdata = map(lambda x:x**2,data)
#lambda x:x**2
#return x**2 --> predicate ---> True False
print(list(sqrdata))    


users = ["ram","shyam","amit","sumit","ajay"]

userUpper = map(lambda x:x.upper(),users)
print(list(userUpper))
