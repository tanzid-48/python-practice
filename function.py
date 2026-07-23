def greet(name):
    print(f"Hello, {name}!")
    
greet("Tanzid")

def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # 8


def add(a,b):
    return a+b
print(add(7,4))



def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()            # Hello, Guest!
greet("Tanzid")    # Hello, Tanzid!


def calculate_grade(marks):
    if marks >= 80:
        return "A++"
    elif marks >= 60:
        return "A"
    elif marks >=40:
        return "Pass"
    else:
        return "fail"
    
print(calculate_grade(74))
print(calculate_grade(84))
print(calculate_grade(45))
print(calculate_grade(40))
print(calculate_grade(30))