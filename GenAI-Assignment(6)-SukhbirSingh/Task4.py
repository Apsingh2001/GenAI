'''File Reader with Exception Handling
1. Ask the user for a filename.
2. Try to open and read the file.
3. Handle:
- FileNotFoundError
- PermissionError
4. If successful, print first 3 lines of the file.
5. Use finally to print:
"File operation attempted."'''

filename = input("Enter filename: ")

try:
	with open(filename, "r", encoding="utf-8") as file:
		first_three_lines = file.readlines()[:3]
	print("".join(first_three_lines), end="")
except FileNotFoundError:
	print("File not found.")
except PermissionError:
	print("Permission denied.")
finally:
	print("File operation attempted.")