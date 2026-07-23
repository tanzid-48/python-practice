
for i in range(3):
     for j in range(2):
         print(f"i={i}, j={j}")
         
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")
    
for i in range(1,10):
    for j in range(i):
        print("*",end="")
    print() 
   
print("--------") 
for i in range(10, 1, -1):   
    for j in range(i):
        print("*", end="")
    print()