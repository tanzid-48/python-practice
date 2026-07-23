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


# তিনটা object বানানো
project1 = Project("CampusCart", ["Next.js", "TypeScript", "BetterAuth", "MongoDB"])
project2 = Project("HireLoop", ["Next.js", "Express", "Stripe", "MongoDB"])
project3 = Project("MealMind AI", ["Next.js", "Express", "TypeScript", "Gemini AI"])

# একটাকে done মার্ক করা
project2.mark_done()

# সবগুলো দেখানো
project1.show()
project2.show()
project3.show()
