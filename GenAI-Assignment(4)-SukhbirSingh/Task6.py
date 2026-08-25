'''Read File Safely (Error Handling Inside File Handling Only)
You must not use exceptions beyond file-related safeguards here.
1. Ask the user for a filename to open.
2. If the file exists, read and print it.
3. If it does not exist, print:
"File not found. Please check the filename."'''

import os

filename = input("Enter the filename to open: ").strip()

if os.path.exists(filename):
	with open(filename, "r") as file:
		print(file.read())
else:
	print("File not found. Please check the filename.")