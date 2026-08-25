'''Using filter(): Filter Expensive Products
Given the list:
prices = [100, 250, 400, 1200, 50, 2000, 850]
Use filter() to:
1. Create a list of prices greater than 500.
2. Create another list of prices less than or equal to 500.
Print both lists.'''

prices = [100, 250, 400, 1200, 50, 2000, 850]

prices_greater_than_500 = list(filter(lambda price: price > 500, prices))
prices_less_than_or_equal_to_500 = list(filter(lambda price: price <= 500, prices))

print("Prices greater than 500:", prices_greater_than_500)
print("Prices less than or equal to 500:", prices_less_than_or_equal_to_500)