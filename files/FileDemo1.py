# file = open("files\\demo1.txt","a")
# file.write("Hello this is second line....")
# file.close()


# with open("files\\demo2.txt","a") as file:
#     file.write("hi this is with block..")


# with open("userdata.txt","a") as file:
#     name = "amit"
#     age=23
#     city ="ahmedbad"
    
#     file.write(f"name ={name}")
#     file.write(f"\nage ={age}")
#     file.write(f"\ncity ={city}")
    
with open("userdata.txt","a") as file:
    user = {"name":"raj","age":23,"city":"mumbai"}
    for i,j in user.items():
    
        file.write(f"{i} ={j}\n")
        
    