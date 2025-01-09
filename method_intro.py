# def say_hello(name):
#     print(f"Hello {name}")
#
# name = input("Enter your name: ")
# say_hello(name)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
symbol = str(input("Enter operation symbol: "))

if symbol == "+":
    print(add(num1, num2))

if symbol == "-":
    print(sub(num1, num2))

if symbol == "x" or symbol == "*":
    print(mul(num1, num2))

if symbol == "/":
    print(div(num1, num2))

