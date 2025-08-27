# Defining a class
class Car:
    color = "red"  # Attribute

    
    # Method
    def drive(self):
        print("The car is driving 🚗")
    
    # __init__() : It initializes the class when it’s called in a Python class
#     def __init__(self, color, model):
#         self.color = color    # Instance variable
#         self.model = model    # Instance variable

# # Creating objects with unique attributes
# car1 = Car("blue", "Sedan")
# car2 = Car("red", "SUV")

# print(car1.color)  # Output: blue
# print(car2.model)  # Output: SUV

# Creating an object
my_car = Car()

print(my_car.color)
my_car.drive()
