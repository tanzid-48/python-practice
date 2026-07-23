class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print(f"{self.brand} - {self.speed}")


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    # def show(self):

    #         print(f"{self.brand} - {self.speed} - {self.fuel_type}")


# Approach ২ (super() দিয়ে reuse) - কম duplicate
def show(self):
    super().show()  # Parent এর show() ব্যবহার করলাম (brand, speed অংশ)
    print(f"Fuel Type: {self.fuel_type}")  # শুধু extra অংশ নিজে লিখলাম


Vehicle1 = Car("Tsala", "100km/h", "gas")

Vehicle1.show()
