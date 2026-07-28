L = eval(input('Enter a list of integers: '))

print('(a) Total items:', len(L))
print('(b) Last item:', L[-1])
print('(c) Reversed:', L[::-1])
print('(d) Contains 5?', 'Yes' if 5 in L else 'No')
print('(e) Number of fives:', L.count(5))

L2 = L[1:-1]
L2.sort()
print('(f) Middle sorted:', L2)

count_less_5 = 0
for item in L:
    if item < 5:
        count_less_5 = count_less_5 + 1
print('(g) Count less than 5:', count_less_5)