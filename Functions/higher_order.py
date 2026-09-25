def calculate(func, a, b):
    return func(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(calculate(add, 2, 3))       # Output: 5
print(calculate(subtract, 5, 2))  # Output: 3
