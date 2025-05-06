#123 - 1 + 2+ 3 =6
no=123
sum =0
rem =0
#//True
while no>0:
    rem = no % 10 # 123 %10 = 3 12 %10 =2 1
    sum = sum + rem # 0 = 0 + 3 =3 # 3 = 3 + 2 =5 5 +1
    no = no //10 #12 1 0

print("sum",sum)    