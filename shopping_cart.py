goods = []
prices = []


while True:
    good = input('What is the product you would like to buy?')
    if good.lower == 'q':
        print('Please enter a product name.')
        break

    price = float(input(f'What is the price of the {good}?'))
    goods.append(good)
    prices.append(price)

for index, good in enumerate(goods):
    print(index, good)
    print(good)
for index, price in enumerate(prices):
    print(index, price)
    print(price)