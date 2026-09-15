def say_hello():
    print("Hello, World!")

def welcome_Student(name):
    print(f"Welcome, {name}!")

def add_numbers(a, b):
    return a + b

def cube(n):
    return n ** 3

def is_positive(num):
    if num > 0:
        return True
    else:
        return False

def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def calculate_area(length, width):
    return length * width

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

convert_to_fahrenheit(32)