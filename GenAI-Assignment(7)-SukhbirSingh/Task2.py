'''Constructor & Encapsulation
Modify the Product class:
Make price a private attribute (_price).
Create getter & setter methods:
- get_price()
- set_price(new_price) - should update only if new_price > 0
Test modifying price using the setter.'''


class Product:
	def __init__(self, name, price, category):
		self.name = name
		self._price = price
		self.category = category

	def get_price(self):
		return self._price

	def set_price(self, new_price):
		if new_price > 0:
			self._price = new_price

	def get_info(self):
		print(f"Name: {self.name}, Price: ${self.get_price():.2f}, Category: {self.category}")


product = Product("Laptop", 999.99, "Electronics")
product.get_info()

product.set_price(899.99)
print(f"Updated price: ${product.get_price():.2f}")

product.set_price(0)
print(f"Price after invalid update: ${product.get_price():.2f}")