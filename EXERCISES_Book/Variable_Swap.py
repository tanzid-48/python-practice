x, y, z = 1, 2, 3
print('Before:', x, y, z)

temp = x
x = y
y = z
z = temp

print('After:', x, y, z)