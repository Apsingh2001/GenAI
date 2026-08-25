'''Mini Program: Safe Shopping Cart
Create a program that:
1. Has a cart list - cart = []
2. Runs a loop asking user to enter prices.
3. Stops when user enters 'q'.
4. Inside the loop:
- Convert input to a float
- Handle ValueError if user enters invalid input
- Raise custom exception if price is negative
5. At the end, print:
- Total items
- Total bill'''

cart = []

while True:
	price_input = input("Enter item price or 'q' to quit: ")

	if price_input.lower() == "q":
		break

	try:
		price = float(price_input)
		if price < 0:
			raise ValueError("Negative prices are not allowed")
		cart.append(price)
	except ValueError as error:
		print(f"Invalid price: {error}")

print(f"Total items: {len(cart)}")
print(f"Total bill: {sum(cart):.2f}")