class Student:  # এটা হলো "নকশা" - কেমন হবে একটা Student
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def show_info(self):
        print(f"Name: {self.name}, CGPA: {self.cgpa}")


# এখন এই নকশা থেকে "আসল" জিনিস (object) বানাই:
student1 = Student("Tanzid", 3.80)  # একটা real object
student2 = Student("Rahim", 3.50)  # আরেকটা real object

student1.show_info()  # Name: Tanzid, CGPA: 3.8
student2.show_info()  # Name: Rahim, CGPA: 3.5



class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def show(self):
        print(f"{self.name} - {self.level}")
        
skill1 = Skill("MERN", "Expert")
skill1.show()
skill2 = Skill("Python", "Intermediate")
skill2.show()

skill3 = Skill("TypeScript", "Advanced")
skill3.show()