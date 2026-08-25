'''Basic Function: Price After Discount
Write a function apply_discount(price, discount_percent) that:
1. Returns the price after discount.
2. If discount_percent is missing, apply a default discount of 5%.
3. Test the function with:
4. apply_discount(1000, 10)
5. apply_discount(500) # uses default discount
6. Add a condition inside the function to ensure discount never exceeds 60%.'''

def apply_discount(price, discount_percent=5):
	discount_percent = min(discount_percent, 60)
	return price * (1 - discount_percent / 100)


print(apply_discount(1000, 10))
print(apply_discount(500))
