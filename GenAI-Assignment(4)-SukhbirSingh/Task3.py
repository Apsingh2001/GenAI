'''Append New Sales
1. Append these new sales to the same file:
5000, 2500, 1700
2. After appending, reopen and print the entire updated file.
3. Print the total number of lines after appending.'''

new_sales = [5000, 2500, 1700]

with open("sales_data.txt", "a") as file:
	for sale in new_sales:
		file.write(f"{sale}\n")

with open("sales_data.txt", "r") as file:
	lines = file.readlines()
	print("Updated file:")
	print("".join(lines), end="")
	print(f"Total number of lines: {len(lines)}")