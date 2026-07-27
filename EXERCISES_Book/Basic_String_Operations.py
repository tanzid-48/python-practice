s = input('Enter a string: ')

print('(a) Length:', len(s))
print('(b) Repeated 10 times:', s*10)
print('(c) First character:', s[0])
print('(d) First three chars:', s[:3])
print('(e) Last three chars:', s[-3:])
print('(f) Reversed:', s[::-1])
if len(s) >= 7:
    print('(g) Seventh character:', s[6])
else:
    print('(g) String is not long enough.')
print('(h) Without first and last char:', s[1:-1])
print('(i) All caps:', s.upper())
print('(j) a replaced with e:', s.replace('a', 'e'))
print('(k) Every letter replaced by space:', ' '*len(s))