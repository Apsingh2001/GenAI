'''Bill Calculator with Error Handling
Given a list of product prices:
prices = [120, 350, 'abc', 500, -200, 800]
Write code that:
1. Iterates through the list.
2. Tries to add only valid (positive numerical) prices to the total.
3. Handles:
o TypeError if value is not a number
o Custom exception using raise ValueError("Negative price not allowed")
4. Prints the running total.
Expected behavior:
Skip invalid items but continue processing.'''

prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for price in prices:
	try:
		if not isinstance(price, (int, float)):
			raise TypeError("Price must be a number")
		if price < 0:
			raise ValueError("Negative price not allowed")
		if price > 0:
			total += price
	except TypeError as error:
		print(f"Skipping invalid price: {error}")
	except ValueError as error:
		print(f"Skipping invalid price: {error}")
	finally:
		print(f"Running total: {total}")