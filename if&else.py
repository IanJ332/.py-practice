# age = int(input("Whats your age?"))
# isAdult= True
# if age >= 18:
#     isAdult = True
# else:
#     isAdult = False
#
# if isAdult:
#     print("You are adults")
# else:
#     print("You are not adults")

num1 = float(input("Whats first number?"))
num2 = float(input("Whats second number?"))

symbol = str(input("What operation you would like to do?"))
if symbol == "+": print(f"the sum is {int(num2 + num1)}")
elif symbol == "-": print(f"the difference is {num1 - num2}")
elif symbol == "x" or symbol == "*": print(f"the great is {num1 * num2}")
elif symbol == "/": print(f"the division is {num1 / num2}")

else: print("pleas enter valid operation symbol: add, sub, multi, div")