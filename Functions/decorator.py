def my_decorator(func):
    def wrapper():
        print("Before Function")
        func()   # call the original function
        print("After Function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
