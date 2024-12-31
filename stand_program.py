menu = {
    "beef": 100,
    "pork": 200,
    "lamb": 300
}
cart = []
total = 0

print("Menu")
print("---------")
for item, price in menu.items():
    print(f"{item}, {price}")

selected_foods = ""  # To store the selected foods

while True:
    food = input("What food do you want to buy? (Enter 'q' to quit): ")
    food = food.lower()
    if food == "q":
        break
    elif menu.get(food) is None:
        print("Please enter a valid food.")
    else:
        cart.append(food)
        total += menu.get(food)
        selected_foods += food + " "  # Add the food to the string

print(f"\nYou selected: {selected_foods}")
print(f"The total is: {total} bucks")
