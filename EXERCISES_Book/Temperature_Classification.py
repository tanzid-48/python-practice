temp = eval(input('Enter temperature in Celsius: '))

if temp < -273.15:
    print('Invalid temperature - below absolute zero.')
elif temp == -273.15:
    print('Temperature is at absolute zero.')
elif temp < 0:
    print('Temperature is below freezing.')
elif temp == 0:
    print('Temperature is at the freezing point.')
elif temp < 100:
    print('Temperature is in the normal range.')
elif temp == 100:
    print('Temperature is at the boiling point.')
else:
    print('Temperature is above the boiling point.')