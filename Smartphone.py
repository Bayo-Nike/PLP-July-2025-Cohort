# Import
import Product

# Subclass for Product
class Smartphone(Product):

    # Method
    def __init__(self,model,color,price):
        super().__init__(price) # Call constructor of Product
        # Instance variables
        self.model=model
        self.color=color
        # self.price=price

    def display_info(self):
        print(f"Smartphone-Model: ${self.model},${self.color}")
        self.display_price()
    
# # Creating objects with unique attributes
Smartphone1 = Smartphone("Samsung", "Red",162)
Smartphone2 = Smartphone("Iphone", "Blue",252)

print('Model1: '+Smartphone1.model +', Color: '+ Smartphone1.color +', Price: '+ str(Smartphone1.price))  # Output: Samsung
print('Model2: '+Smartphone2.model +', Color: '+ Smartphone2.color +', Price: '+ str(Smartphone2.price))  # Output: Iphone