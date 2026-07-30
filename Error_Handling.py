try:
    result = 10 / 0     # এটা error দিবে (division by zero)
except:
    print("কিছু একটা ভুল হয়েছে!")

print("প্রোগ্রাম চলতে থাকলো...")



try:
    result = 10 / 0
except ZeroDivisionError:
    print("শূন্য দিয়ে ভাগ করা যায় না!")
    
    
    
try:
    age = int("hello")     # এটা error দিবে, "hello" কে সংখ্যা বানানো যায় না
except ValueError:
    print("এটা সংখ্যা না!")