numbers = [100,200,344,897,900,453]
#numbers.clear()
print(numbers)
#remvedELm = numbers.pop() # removes last element
if len(numbers) > 0:
    remvedELm = numbers.pop() # removes last element
    print("removing...",remvedELm)
    remvedELm = numbers.pop(3) # removes last element
    print("removing...",remvedELm)
print(numbers)
if 2000 in numbers:
    numbers.remove(2000)
else:
    print("2000 not found in the list")
        
print(numbers)