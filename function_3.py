# সাধারণ function
def square(x):
    return x**2


print(square(5))  # 25


students = [("Tanzid", 85), ("Rahim", 92), ("Karim", 78)]

# Marks অনুযায়ী sort করতে চাইলে
students.sort(key=lambda x: x[1])
print(students)

Skills = ["MERN", "Next.js", "TS", "Flutter", "Java", "python"]
Skills.sort(key=lambda skill : len(skill))
print(Skills)