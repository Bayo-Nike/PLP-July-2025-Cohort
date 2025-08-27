class Car:
    def move(self):
        return "The car is driving 🚗"

class Plane:
    def move(self):
        return "The Plane is Flying ✈️"
class Boat:
    def move(self):
        return "The Plane is sailing 🚤"
    
class Bicycle:
    def move(self):
        return "The Plane is pedaling 🚴"

# Polymorphism in action
for vehicle in [Car(), Plane(),Boat(),Bicycle()]:
    print(vehicle.move())