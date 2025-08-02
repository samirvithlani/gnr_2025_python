user = {"id":1,"name":"amit","age":23,"status":"Active"}

with open("files/userdata.txt","a") as file:
    for i,j in user.items():
        file.write(f"{i} = {j}\n")