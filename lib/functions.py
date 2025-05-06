# lib/functions.py

# 1. Function that takes no arguments and prints a greeting
def greet_programmer():
    print("Hello, programmer!")

# 2. Function that takes one argument and prints a personalized greeting
def greet(name):
    print(f"Hello, {name}!")

# 3. Function that takes an optional argument and prints a greeting
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# 4. Function that returns the sum of two numbers
def add(num1, num2):
    return num1 + num2

# 5. Function that returns half the value of a number
def halve(number):
    return number / 2
