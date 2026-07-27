n = eval(input('Enter height (odd part) of diamond: '))

# Upper half (including middle) 
for i in range(n):
    print(' ' * (n-1-i) + '*' * (2*i+1))

# Lower half 
for i in range(n-2, -1, -1):
    print(' ' * (n-1-i) + '*' * (2*i+1))