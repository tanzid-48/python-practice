L = eval(input('Enter a list: '))

result = []
for item in L:
    if item not in result:
        result.append(item)

print('After removing duplicates:', result)