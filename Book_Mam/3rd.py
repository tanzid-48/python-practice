import random

# 1. 50 random integers, each between 3 and 6
for _ in range(50):
    print(random.randint(3, 6))

# 2. Random number x between 1 and 50, y between 2 and 5, computes x^y
x = random.randint(1, 50)
y = random.randint(2, 5)
result = x**y
print(f"x = {x}, y = {y}, x^y = {result}")

# 3. Random number between 1 and 10, prints your name that many times
count = random.randint(1, 10)
for _ in range(count):
    print("Tanzid")

# 4. Random decimal number between 1 and 10 with two decimal places of accuracy
dec_num = round(random.uniform(1, 10), 2)
print(dec_num)

# 5. 50 random numbers where the i-th number is between 1 and i + 1
for i in range(1, 51):
    print(random.randint(1, i + 1))

# 6. Asks user to enter two numbers, x and y, and computes |x - y| / (x + y)
x_val = float(input("Enter number x: "))
y_val = float(input("Enter number y: "))
if (x_val + y_val) != 0:
    ans = abs(x_val - y_val) / (x_val + y_val)
    print(f"Result: {ans}")
else:
    print("Error: Division by zero (x + y cannot be 0).")

# 7. Asks user to enter an angle between -180 and 180, converts to 0 to 360 using modulo
angle = float(input("Enter an angle between -180 and 180: "))
equivalent_angle = angle % 360
print(f"Equivalent angle between 0 and 360: {equivalent_angle}")
