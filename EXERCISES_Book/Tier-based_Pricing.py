items = eval(input('How many items are you buying? '))

if items < 10:
    price_per_item = 12
elif items < 100:
    price_per_item = 10
else:
    price_per_item = 7

total = items * price_per_item
print('Total cost: $' + str(total))