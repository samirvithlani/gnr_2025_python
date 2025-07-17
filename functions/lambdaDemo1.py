# def test():
#     print("test called...")

# test()    


x = lambda : print("test function called...")
x()

# def test(a,b):
#     print(f"ans = {a+b}")
# test(10,20)    

x1 = lambda a,b : print(f"ans = {a+b}")
x1(100,20)


# def add(a,b,c):
#     return a + b + c

# ans = add(10,20,30)
# print(f"ans1 = {ans}")
# #print(f"ans2 = {add(1,2,3)}")
# print("ans = ",add(5,6,7))
    

x3 = lambda a,b,c : a+b+c
ans = x3(100,1,2)
print(ans)
print(f"addition = {x3(1000,2000,3000)}")

