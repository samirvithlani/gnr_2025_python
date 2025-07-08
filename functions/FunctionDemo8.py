# def findEvens(*args):
#     even =[]
#     for i in args:
#         if i %2==0:
#             even.append(i)
    
#     return even        

def findEvens(*args):
    return [i for i in args if i % 2 ==0]

x = findEvens(10,20,11,23,45,66,79,808)
print(x)
#[10,20,66,808]