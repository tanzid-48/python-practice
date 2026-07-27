num_str = input("Enter a large integer: ")
result = ""
count = 0

for i in range(len(num_str) - 1, -1, -1):
    result = num_str[i] + result
    count = count + 1
    if count % 3 == 0 and i != 0:
        result = "," + result

print(result)
