def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        print("ভাগ সফল হয়েছে!")   # error না হলে এটা চলবে
        return result
    finally:
        print("এই লাইন সবসময় চলবে")   # error হোক বা না হোক, সবসময় চলবে