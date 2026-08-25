'''Write Sales Records to a File
1. Create a list of sales amounts:
2. sales = [1200, 450, 980, 1500, 3000]
3. Open a file named sales_data.txt in write mode.
4. Write each sale on a new line in the file.
5. Close the file, then reopen it and print its contents.
Extra (optional): Write the data in comma-separated format instead of separate lines.'''

sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as file:
	for sale in sales:
		file.write(f"{sale}\n")

with open("sales_data.txt", "r") as file:
	print(file.read())