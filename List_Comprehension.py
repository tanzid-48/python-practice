# Traditional way
squares = []
for x in range(5):
    squares.append(x**2)

print(squares)  # [0, 1, 4, 9, 16]


# List Comprehension
# syntax
# [expression for item in iterable]
# Condition
# [expression for item in iterable if condition]
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


# শুধু জোড় সংখ্যা নিতে চাইলে
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

Skills = ["MERN", "Next.js", "TS", "Flutter", "Java", "python"]

# সব skill এর নাম বড় হাতের অক্ষরে (uppercase) করতে চাইলে
upper_skills = [skill.upper() for skill in Skills]
print(upper_skills)
# ['MERN', 'NEXT.JS', 'TS', 'FLUTTER', 'JAVA', 'PYTHON']


print("Tanzid")


skills = ["MERN", "Next.js", "TS", "Flutter", "Java", "python"]


add = [skill + " - Learned" for skill in skills]
print(add)

long_skills = [skill for skill in skills if len(skill) > 4]
print(long_skills)


