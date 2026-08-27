'''Inheritance (Single-Level)
- Create a subclass ElectronicProduct that inherits from Product.
Additional attribute:
warranty_years
- Override the get_info() method to include warranty info.
- Create an object and demonstrate inheritance + overriding.'''


class Product:
	def __init__(self, name, price, category):
		self.name = name
		self._price = price
		self.category = category

	def get_price(self):
		return self._price

	def get_info(self):
		print(f"Name: {self.name}, Price: ${self.get_price():.2f}, Category: {self.category}")


class ElectronicProduct(Product):
	def __init__(self, name, price, category, warranty_years):
		super().__init__(name, price, category)
		self.warranty_years = warranty_years

	def get_info(self):
		print(
			f"Name: {self.name}, Price: ${self.get_price():.2f}, "
			f"Category: {self.category}, Warranty: {self.warranty_years} years"
		)


electronic_product = ElectronicProduct("Laptop", 999.99, "Electronics", 2)
electronic_product.get_info()