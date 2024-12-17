weight = int(input('Enter weight in pounds: '))
units = input('Enter lb or kg: ').upper()

if units == 'KG':
    print(f'Your weight is {weight}, convert to pounds is {weight * 2.20462} pounds')
elif units == 'LB':
    print(f'Your weight is {weight}, convert to kilograms is {weight / 2.20462} kilograms')
else:
    print('Invalid input, please enter lbs or kg')