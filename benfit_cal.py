# Total = Principal * (1 + (rate / 100)) * Time

principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

while principal <= 0:
    print("Please enter a positive number.")
    principal = float(input("Enter the principal: "))

while rate <= 0:
    print("Please enter a positive number.")
    rate = float(input("Enter the rate: "))

while time <= 0:  # Corrected from `Time` to `time`
    print("Please enter a positive number.")
    time = float(input("Enter the time: "))

total = principal * (1 + (rate / 100)) * time
print(f'The total is: {total}')
