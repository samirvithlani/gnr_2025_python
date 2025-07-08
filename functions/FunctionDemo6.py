def checkData(*args):
    flag =True
    for i in args:
        if type(i)!= int:
            flag =False
            break
    return flag

x = checkData(10,20,30,"kk",22,345,6)    
print(x)


#same task: all data should be string and all name must palindrome..        