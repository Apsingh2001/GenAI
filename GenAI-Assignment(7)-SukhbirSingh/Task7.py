'''Simple Inventory System (OOP Only)
Create two classes:
Class: Inventory
Attributes:
products -> list to store product objects
Methods:
add_product(product)
remove_product(name)
get_total_value() -> sums prices of all products
show_all_products() -> prints info for each product
Class: Store
Attributes:
store_name
inventory -> an Inventory object
Methods:
add_new_product() -> takes input & creates Product object
show_summary() - prints total items & value
Important: Use only OOP concepts - no file handling, no exceptions, no packages.
Test the system by:
1. Creating a Store object
2. Adding 3 products
3. Showing summary
4. Using ___add___ to combine prices of two products'''


class Product:
	def __init__(self, name, price, category):
		self.name = name
		self.price = price
		self.category = category

	def __str__(self):
		return f"Product({self.name}, {self.price}, {self.category})"

	def get_info(self):
		print(f"Name: {self.name}, Price: ${self.price:.2f}, Category: {self.category}")

	def __add__(self, other):
		return self.price + other.price


class Inventory:
	def __init__(self):
		self.products = []

	def add_product(self, product):
		self.products.append(product)

	def remove_product(self, name):
		for product in self.products:
			if product.name == name:
				self.products.remove(product)
				return

	def get_total_value(self):
		return sum(product.price for product in self.products)

	def show_all_products(self):
		for product in self.products:
			product.get_info()


class Store:
	def __init__(self, store_name):
		self.store_name = store_name
		self.inventory = Inventory()

	def add_new_product(self):
		name = input("Enter product name: ")
		price = float(input("Enter product price: "))
		category = input("Enter product category: ")
		self.inventory.add_product(Product(name, price, category))

	def show_summary(self):
		print(f"Store: {self.store_name}")
		print(f"Total items: {len(self.inventory.products)}")
		print(f"Total value: ${self.inventory.get_total_value():.2f}")


store = Store("Tech and More")
store.add_new_product()
store.add_new_product()
store.add_new_product()
store.inventory.show_all_products()
store.show_summary()
print(f"Combined price of first two products: ${store.inventory.products[0] + store.inventory.products[1]:.2f}")