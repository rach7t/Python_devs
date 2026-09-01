#count()
numbers = (10, 20, 30, 20, 40)
print(numbers.count(20)) 

#index()
print(numbers.index(30)) 

#all()
print(all(numbers))  # Output: True

#ANY()
print(any(numbers))  # Output: True

#enumerate()
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")