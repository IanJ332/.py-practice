
goods = [] #List to store the goods name
prices = [] #List to store the price

while True:
    good =  input("Would you like to buy? ")
    if good.lower() == "q":
        break
    price = float(input(f"What price of {good}? "))
    goods.append(good)
    prices.append(price)
# print("Goods list", goods)
# print("Prices list", prices)
for index, good in enumerate(goods):
    # print('index: ', index)
    # print("Good's name: " , good)
    print(f"The  {index + 1} is: {good}, the price is {prices[index]}: .2f") #.2f means I only want 2 figures after the . which is
    print(f"The total is {sum(prices)}.")