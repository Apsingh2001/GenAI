# Process Multiple Orders (for loop)

# Given a list of order amounts: orders = [1200, 2500, 800, 1750, 3000], use a for loop to apply the discount rules from Task 1 to each order and print a summary table showing: order_amount -> discount% -> final_amount.

from Task1 import calculate_discount

orders = [1200, 2500, 800, 1750, 3000]

'''
Also compute and print the total revenue after discounts.
'''
total_revenue = 0
for order_amount in orders:
    discount = calculate_discount(order_amount)
    final_amount = order_amount - (order_amount * discount)
    total_revenue += final_amount
    print(f"Order Amount: {order_amount} -> Discount: {discount * 100}% -> Final Amount: {final_amount}")
    print(f"Total revenue after discounts: {total_revenue}")

'''
Print the number of orders that received a discount (discount > 0).
'''
discounted_orders = sum(1 for order_amount in orders if calculate_discount(order_amount) > 0)
print(f"Number of orders that received a discount: {discounted_orders}")