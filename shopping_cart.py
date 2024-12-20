goods = []
prices = []

while True:
    good = input('What is the product you would like to buy?')
    if good.lower() == 'q':  # Corrected here
        print('You have exited the input process.')
        break

    price = float(input(f'What is the price of the {good}?'))
    goods.append(good)
    prices.append(price)

# Print the goods and prices
for index, good in enumerate(goods):
    print(f'{index}: {good}')
for index, price in enumerate(prices):
    print(f'{index}: {price}')
