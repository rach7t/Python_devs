def numbers():
    yield 10
    yield 20
    yield 30

g = numbers()
print(next(g))  # Output: 10
print(next(g))  # Output: 20
print(next(g))  # Output: 30