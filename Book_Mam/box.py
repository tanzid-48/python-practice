width = int(input("Enter width: "))
height = int(input("Enter height: "))

for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")
        
for i in range(5,0,-1):
    print('*'*i)
    