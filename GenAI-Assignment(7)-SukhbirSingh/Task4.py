'''Polymorphism
- Create two classes:
    Laptop(Product)
    Mobile(Product)
- Both override:
    def get_info(self):
# Print details in their own style
- Write a loop that iterates over objects of Laptop and Mobile and calls get_info() on each to
show polymorphism.'''


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self._price = price
        self.category = category

    def get_price(self):
        return self._price


class Laptop(Product):
    def get_info(self):
        print(f"Laptop: {self.name} | ${self.get_price():.2f} | {self.category}")


class Mobile(Product):
    def get_info(self):
        print(f"Mobile phone: {self.name} | ${self.get_price():.2f} | {self.category}")


products = [
    Laptop("ThinkPad", 1299.99, "Computers"),
    Mobile("Galaxy S24", 799.99, "Phones"),
]

for product in products:
    product.get_info()