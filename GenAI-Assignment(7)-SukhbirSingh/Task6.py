'''Magic Methods & Operator Overloading
- Add the following to your Product class:
1. __str__
    Returns a readable string:
    Product(name, price, category)
2. Operator Overloading (__add__)
    Allow:
    product1 + product2
- To return the total combined price.
- Test this with two product objects.'''


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    def __add__(self, other):
        return self.price + other.price


product1 = Product("Laptop", 999.99, "Electronics")
product2 = Product("Coffee Mug", 14.99, "Kitchen")

print(product1)
print(product2)
print(f"Combined price: ${product1 + product2:.2f}")