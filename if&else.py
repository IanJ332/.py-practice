age = int(input("Whats your age?"))
isAdult= True
if age >= 18:
    isAdult = True
else:
    isAdult = False

if isAdult:
    print("You are adults")
else:
    print("You are not adults")
