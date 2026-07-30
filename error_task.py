try:
    def divide(a, b):
        return a/b

except ZeroDivisionError:
    print("Cannot divide by zero")


def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

# এখন কল করে টেস্ট করি
print(divide(10, 2))    # 5.0
print(divide(10, 0))    # Cannot divide by zero, তারপর None print হবে