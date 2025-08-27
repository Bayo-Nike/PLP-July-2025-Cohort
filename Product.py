# Base class
class Product:
    def __init__(self,price):
        self.price=price
    
    def display_price(self):
        print(f"Price:${self._price}")
