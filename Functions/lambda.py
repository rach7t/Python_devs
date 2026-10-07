# square = lambda x: x*x
# print(square(4))

numbers = [1,2,3,4,5]
squares = list(map(lambda x: x*x,numbers))
evens = list(filter(lambda x: x%2==0,numbers))
descending = sorted(numbers,reverse=True)

print(squares)
print(evens)
print(descending)

