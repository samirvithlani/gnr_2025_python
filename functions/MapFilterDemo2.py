users = ["ram","shyam","amit","sumit","ajay"]
#s

#uppersname = [i.upper() for i in users if i.startswith("s")]

# for  i in users:
#     if i.startswith("s"):
#         uppersname.append(i.upper())
uppersname = map(lambda x:x.upper(),filter(lambda x:x.startswith("s"),users))
print(list(uppersname))


numbers = [12,11,33,45,67,88,91]

#sqrnum = map(lambda x:x**2,numbers)
sqrnum = map(lambda x:x**2,filter(lambda x:x>50,numbers))
print(list(sqrnum))

#map, filter,reduce
#map --> 
#condition filter
#10 sb=ubhect --reduce