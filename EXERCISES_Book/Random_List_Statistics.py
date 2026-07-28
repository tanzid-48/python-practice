from random import randint

L = [randint(1, 100) for i in range(20)]
print('(a) List:', L)

average = sum(L) / len(L)
print('(b) Average:', average)

largest = max(L)
smallest = min(L)
print('(c) Largest:', largest, '| Smallest:', smallest)

sorted_L = sorted(L)
second_largest = sorted_L[-2]
second_smallest = sorted_L[1]
print('(d) Second largest:', second_largest, '| Second smallest:', second_smallest)

even_count = 0
for num in L:
    if num % 2 == 0:
        even_count = even_count + 1
print('(e) Even numbers count:', even_count)