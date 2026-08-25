'''Custom Exception: Age Validator
1. Write a function check_age(age) that:
- Raises a custom exception ValueError("Age must be between 1 and 120") if
age is out of range.
2. In your main code:
- Take age input from the user.
- Use try-except to catch and print the custom error message.'''


def check_age(age):
	if age < 1 or age > 120:
		raise ValueError("Age must be between 1 and 120")
	return True


try:
	age = int(input("Enter your age: "))
	check_age(age)
	print("Age is valid")
except ValueError as error:
	print(error)