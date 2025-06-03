users = ["amit","sumit","ajay","raj","ajay","parth"]
cnt = users.count("amit")
print("cnt",cnt)

ind = users.index("ajay")
print("ind",ind)


#users.reverse()
#users.sort() #alphabetical order
#users.sort(reverse=True) #reverse alphabetical order
#users.sort(key=len)
users.sort(key=len, reverse=True) #sort by length of names, longest first
print(users)
