'''Safe Division Utility
Write a program that:
1. Takes two inputs from the user: numerator and denominator.
2. Uses try-except to handle:
o ValueError (if input is not a number)
o ZeroDivisionError (if denominator = 0)
3. If no error occurs, print the result inside the else block.
4. In the finally block, print:
"Operation Complete"'''

try:
	numerator = float(input("Enter numerator: "))
	denominator = float(input("Enter denominator: "))
	result = numerator / denominator
except ValueError:
	print("Please enter numbers only.")
except ZeroDivisionError:
	print("Cannot divide by zero.")
else:
	print(f"Result: {result}")
finally:
	print("Operation Complete")