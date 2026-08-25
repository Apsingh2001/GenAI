'''Mini Project - Export Discounted Prices
Create a dictionary:
prices = {
"Mouse": 500,
"Keyboard": 800,
"Monitor": 7000,
"Pendrive": 400,
"Camera": 5000
}
Ask the user for a discount percentage.
Write discounted prices into discount_report.txt using:
Product | Original Price | Discounted Price
After writing, read the file and print it to the terminal.
- Write a summary at the bottom of the file:
Total Items: X
Average Discounted Price: Y'''

prices = {
	"Mouse": 500,
	"Keyboard": 800,
	"Monitor": 7000,
	"Pendrive": 400,
	"Camera": 5000
}

discount_percentage = float(input("Enter the discount percentage: "))
discounted_prices = {
	product: price * (1 - discount_percentage / 100)
	for product, price in prices.items()
}

with open("discount_report.txt", "w") as file:
	file.write("Product | Original Price | Discounted Price\n")
	for product, price in prices.items():
		file.write(
			f"{product} | {price:.2f} | {discounted_prices[product]:.2f}\n"
		)

	average_discounted_price = sum(discounted_prices.values()) / len(discounted_prices)
	file.write(f"\nTotal Items: {len(prices)}\n")
	file.write(f"Average Discounted Price: {average_discounted_price:.2f}\n")

with open("discount_report.txt", "r") as file:
	print(file.read())