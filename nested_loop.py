rows = int(input('Enter number of rows: '))
columns = int(input('Enter number of columns: '))

symbol = input('Enter symbol: ')

for row in range(rows):
    for column in range(columns):
        print(symbol, end=' ')
    # The reason print here is like printf, so it will go to next col
    print()
