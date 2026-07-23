# *args
def add_all(*numbers):
    print(numbers)
    return sum(numbers)


print(add_all(1, 2, 3))  # 6
print(add_all(1, 2, 3, 4, 5))  # 15


def print_profile(**info):
    print(info)


print_profile(name="Tanzid", university="PUB", semester=7)
# {'name': 'Tanzid', 'university': 'PUB', 'semester': 7}


def student_info(name, *skills, **details):
    print(f"Name: {name}")
    print(f"Skills: {skills}")
    print(f"Details: {details}")


student_info("Tanzid", "Python", "JS", cgpa=3.80, semester=7)


print("-----------------")


def total_marks(*marks):
    total = sum(marks)
    count = len(marks)
    average = total / count

    print(f"Total: {total}")
    print(f"Average: {average}")


total_marks(80, 90, 70, 85)


def total_marks(*marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg


result, avg = total_marks(80, 90, 70, 85)
print(f"Total Sum = {result}")
print(f"Average = {avg}")
