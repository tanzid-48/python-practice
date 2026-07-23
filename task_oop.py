class Task:
    def __init__(self, title, priority, is_completed=False):
        self.title = title
        self.priority = priority
        self.is_completed = is_completed  

    def mark_complete(self):
        self.is_completed = True  

    def show(self):
        print(f"{self.title} - Priority: {self.priority} - Completed: {self.is_completed}")
        
task1 = Task("Finish thesis proposal", "High")
task2 = Task("Push code to GitHub", "Medium")
task3 = Task("SCIC assignment submit", "High")

task1.mark_complete()

task1.show()
task2.show()
task3.show()