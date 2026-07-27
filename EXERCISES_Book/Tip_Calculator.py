price = eval(input('Enter the price of the meal: '))
tip_percent = eval(input('Enter the percent tip you want to leave: '))
tip = price * tip_percent / 100
total = price + tip
print('Tip amount:', tip)
print('Total bill with tip:', total)