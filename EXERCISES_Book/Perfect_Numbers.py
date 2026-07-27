for num in range(1, 10000):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total = total + i
    if total == num:
        print(num, 'is a perfect number')