'''Create Product Info File (User Input)
1. Ask the user for 3 product names & their prices.
2. Write them into a new file products.txt in this format:
3. ProductName | Price
4. Read the file and print each line with proper formatting.'''

with open("products.txt", "w") as file:
	for product_number in range(1, 4):
		product_name = input(f"Enter product {product_number} name: ")
		price = input(f"Enter product {product_number} price: ")
		file.write(f"{product_name} | {price}\n")

with open("products.txt", "r") as file:
	print("Product information:")
	for line in file:
		print(line.strip())