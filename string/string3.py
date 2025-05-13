#ord chr
#assici value 'A'=65 'a'=97 space 32


x  = 65
print(chr(x))

y ='A'
print(ord(y))

#32

name = input("enter name") #amit
uppername = ""
#uppercase

for  i in name:
    #ord(i) = 97 -32 -->int ->65 --> chr
    #A
    if(ord(i)>=97 and ord(i)<=121):
        uppername = uppername +  chr(ord(i)-32)
    else:    
        uppername = uppername + chr(ord(i))

print(uppername)    
    

