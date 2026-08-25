'''Mini Problem: Menu Using Functions
Create the following three small functions:
1. add_price(prices_list, price) -> adds price to the list.
2. get_average_price(prices_list) -> returns average price.
3. get_max_price(prices_list) -> returns the maximum price.
Then create a simple menu:
1 - Add price
2 - Show average price
3 - Show highest price
q - Quit
Use only loops + function calls (no OOP).'''

def add_price(prices_list, price):
	prices_list.append(price)


def get_average_price(prices_list):
	if not prices_list:
		return 0
	return sum(prices_list) / len(prices_list)


def get_max_price(prices_list):
	if not prices_list:
		return None
	return max(prices_list)


prices = []

while True:
	print("\n1 - Add price")
	print("2 - Show average price")
	print("3 - Show highest price")
	print("q - Quit")

	choice = input("Choose an option: ").lower()

	if choice == "1":
		try:
			price = float(input("Enter a price: "))
			add_price(prices, price)
			print("Price added.")
		except ValueError:
			print("Please enter a valid number.")
	elif choice == "2":
		print("Average price:", get_average_price(prices))
	elif choice == "3":
		highest_price = get_max_price(prices)
		if highest_price is None:
			print("No prices have been added.")
		else:
			print("Highest price:", highest_price)
	elif choice == "q":
		print("Goodbye!")
		break
	else:
		print("Invalid option.")