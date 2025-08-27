# Import
# import Product

# Base class
class Product:
    def __init__(self,price):
        self._price = price #Encapsulated (protected)
     
    def display_price(self):
        print(f"Price:${self._price}")

# Subclass for Product
class Book(Product):

    # Method
    def __init__(self,author,title,price):
        super().__init__(price)  # Call constructor of Product
        # Instance variables
        self.author=author
        self.title=title
        # self.price=price
    
    def display_info(self):
        print(f"Book-Author: {self.author},{self.title}")
        self.display_price()

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
        print(f"Smartphone-Model: {self.model},{self.color}")
        self.display_price()

        
# Create Book objects with unique attributes
book1 = Book("Bayisa", "Rich Dad and Poor Dad",162)
book2 = Book("Bedasa", "Anti_corruption",252)

# Create Smartphone objects
phone1 = Smartphone("Samsung", "Red", 162)
phone2 = Smartphone("iPhone", "Blue", 252)

# Display information
book1.display_info()
book2.display_info()

phone1.display_info()
phone2.display_info()



# print('Author1: '+Book1.author +', title: '+ Book1.title +', Price: '+ str(Book1.price))  # Output: Samsung
# print('Author2: '+Book2.author +', title: '+ Book2.title +', Price: '+ str(Book2.price))  # Output: Iphone