'''Basic Class & Object Creation
- Create a class Product with:
Attributes: name, price, category
Method: get_info() -> prints product details
- Create two objects and call get_info().
- Add a method apply_discount(percent) that returns the discounted price.'''


class Product:
	def __init__(self, name, price, category):
		self.name = name
		self.price = price
		self.category = category

	def get_info(self):
		print(f"Name: {self.name}, Price: ${self.price:.2f}, Category: {self.category}")

	def apply_discount(self, percent):
		return self.price * (1 - percent / 100)


product1 = Product("Laptop", 999.99, "Electronics")
product2 = Product("Coffee Mug", 14.99, "Kitchen")

product1.get_info()
product2.get_info()