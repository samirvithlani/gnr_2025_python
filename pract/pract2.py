users = ["ram","bob","naman","amit","kunal","Nobody","aba","racecar"]
#palindromename =[]
#HINT :string slicing [::-1]
palindromes  =[i for i in users if i == i[::-1]]


# for i in users:
#     if i == i[::-1]:
#         palindromes.append(i)

print(palindromes)        