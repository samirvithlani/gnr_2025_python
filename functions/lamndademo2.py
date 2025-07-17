# def findMax(a,b):
#     if a >b:
#         return a
#     else:
#         return b

# maxno = findMax(10,20)    
# print(maxno)


x1 =lambda a,b : a if a > b else b
maxno = x1(100,20)
print(maxno)

x2 = lambda name : True if name == name[::-1] else False
print(x2("namana"))


x3 = lambda str1,str2: True if len(str1) == len(str2) else False
print(f"{x3("abc","pqrs")}")


#checkNo = lambda no : "POS" if no >0 else "NEG"
checkNo = lambda no : "POS" if no > 0  else ("ZERO" if no ==0 else "NEG")
print(checkNo(-10))
