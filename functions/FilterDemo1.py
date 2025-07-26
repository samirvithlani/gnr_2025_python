users = ["ram","shyam","amit","sumit","ajay"]

userwithlen =  filter(lambda x:len(x)>3,users)
print(list(userwithlen))


userwiths = filter(lambda x:x.startswith("s"),users)
print(list(userwiths))

