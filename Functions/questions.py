# create a decorator that prints "Function Started" before as an arguments
# Create a list iterator and print its values using next()
# Create a calculator.py module with add(),subtract(),multiply()
def my_decorator(func):
    def wrapper():
        print("Function Started")
        func()   # call the original function
       
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# List Iterator 
numbers = [10,20,30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))

# Question Three
def calculate(func, a, b):
    return func(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a,b):
    return a*b

def modulus(a,b):
    return a%b

print(calculate(add, 2, 3))       # Output: 5
print(calculate(subtract, 5, 2))  # Output: 3
print(calculate(multiply,4,5))
