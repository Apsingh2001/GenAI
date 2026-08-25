'''Read File in Different Ways
Using the same sales_data.txt:
1. Read the entire file using .read() and print it.
2. Read the first line using .readline().
3. Read all lines using .readlines() and convert them into a list of integers.
Ensure proper formatting and cleanup of newline characters.'''

with open("sales_data.txt", "r") as file:
	print("Entire file:")
	print(file.read(), end="")

with open("sales_data.txt", "r") as file:
	first_line = file.readline().strip()
	print(f"\nFirst line: {first_line}")

with open("sales_data.txt", "r") as file:
	sales = [int(line.strip()) for line in file.readlines()]
	print(f"All sales as integers: {sales}")