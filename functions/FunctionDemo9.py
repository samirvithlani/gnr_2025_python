# def getData(**kwargs):
#     #kwargs  data dict
#     print(kwargs)

# #getData()
# #getData(100) error
# getData(a=100,b="java",c=200,d=[])


# def getData(**kwargs,x): #error
#     #kwargs  data dict
#     print(kwargs)

# #getData()
# #getData(100) error
# getData(a=100,b="java",c=200,d=[])


def getData(x,**kwargs):
    #kwargs  data dict
    print(kwargs)

#getData()
#getData(100) error
getData(100,a=100,b="java",c=200,d=[])
getData(x =100,a=100,b="java",c=200,d=[])