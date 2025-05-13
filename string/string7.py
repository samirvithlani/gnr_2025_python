name ="ram#"

x = name.startswith("rm")
#x = name[0]=="r"
print("x == ",x)
x = name.endswith("m")

#r a m -3
#0 1 2
#2==m
#name[2]=m
#name[3-1]=="m"
#chr(2) =
x = name[len(name)-1] == "m"

print("x ==!! ",x)

name="Abc or"
print("alnum",name.isalnum())
print("alpha",name.isalpha())
print("isdigit",name.isdigit()) #html --> input -->string age = "12" -->convert -->"12"
print("is lower",name.islower())
print("is upper",name.isupper())
print(name.isspace())
print("is printable",name.isprintable())
print(name.istitle())