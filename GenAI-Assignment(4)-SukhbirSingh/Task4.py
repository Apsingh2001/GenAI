'''Generate Summary Report from File
Using only file reading operations:
1. Read all sales values from sales_data.txt.
2. Convert them into integers.
3. Calculate and print:
- Total Sales
- Highest Sale
- Lowest Sale
- Average Sale'''

with open("sales_data.txt", "r") as file:
	sales = [int(line.strip()) for line in file.readlines()]

print(f"Total Sales: {sum(sales)}")
print(f"Highest Sale: {max(sales)}")
print(f"Lowest Sale: {min(sales)}")
print(f"Average Sale: {sum(sales) / len(sales)}")