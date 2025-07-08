def checkAllPalindromes(*args):
    flag = True
    for i in args:
        if type(i)!= str:
            flag =False
            break
        else:
            if i != i[::-1]:
                flag = False
                break
    return flag


x = checkAllPalindromes("naman","sam")        
print(x)