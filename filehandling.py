Skills = ["MERN", "Next.js", "TS", "Flutter", "Java", "python"]

# ফাইলে লেখা
with open("skills.txt", "w") as file:
    for skill in Skills:
        file.write(skill + "\n")

# ফাইল থেকে পড়া
with open("skills.txt", "r") as file:
    content = file.read()
    print(content)


with open("file.txt", "w") as file:  # লিখে (মুছে নতুন করে)
    file.write("text")

with open("file.txt", "a") as file:  # যোগ করে (আগেরটা রেখে)
    file.write("more text")

with open("file.txt", "r") as file:  # পড়ে
    content = file.read()
    print(content)
