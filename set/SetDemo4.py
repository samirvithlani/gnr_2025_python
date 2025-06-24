user1 ={"ram","krishna","seeta","meera"}
user2 = {"ram","krishna","arjun","sahdev","seeta","meera"}

#x = user1.union(user2)
#x = user1 | user2
#x = user1.difference(user2)
#x = user1- user2
#x = user2 - user1
#x = user1.intersection(user2)
#x = user1 & user2

#x = user1.symmetric_difference(user2)
#print(x)

#user1.difference_update(user2)
#print(user1)

#x = user1.issubset(user2)
#x = user1.issuperset(user2)
x = user1.isdisjoint(user2)
print(x)



