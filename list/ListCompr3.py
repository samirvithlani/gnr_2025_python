data = [100,2,-90,0,87,0,-100,56]
#[positive,pos,nef,pos,neg,pos]
#datamsg =["POSITIVE" if i>0 else "NEGETIVE" for i in data]
datamsg =["PSOITIVE" if i > 0 else("NEGETIVE" if i<0 else "ZERO") for i in data]
print(datamsg)