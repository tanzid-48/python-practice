L = eval(input('Enter list L: '))
M = eval(input('Enter list M: '))

N = []
for i in range(len(L)):
    N.append(L[i] + M[i])

print('N =', N)