# Parent class (Base class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Child class (Person এর সব feature পাবে, plus extra)
class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)  # Parent এর __init__ কল করা
        self.university = university

    def show(self):
        super().show()  # Parent এর show() কল করলাম
        print(f"University: {self.university}")


s1 = Student("Tanzid", 22, "Pundra University")
s1.show()


class Project:
    def __init__(self, name, tech_stack, status="In Progress"):
        self.name = name
        self.tech_stack = tech_stack
        self.status = status

    def mark_done(self):
        self.status = "Completed"

    def show(self):
        tech = " , ".join(self.tech_stack)
        print(f"{self.name} | Tech: {tech} | Status: {self.status}")


class AIProject(Project):
    def __init__(self, name, tech_stack, ai_model, status="In Progress"):
        super().__init__(name, tech_stack, status)
        self.ai_model = ai_model

    def show(self):
        super().show()
        print(f"AI Model: {self.ai_model}")

project1 = AIProject("CampusCart", ["Next.js", "TypeScript", "BetterAuth", "MongoDB"],"Gemini")

project1.show()