'''User Menu (while loop + break/continue)
1. Implement a simple while-loop driven menu that keeps asking the user to choose an
action until they press q to quit.
Menu options:
    1 - Add order amount to a running list (use input())
    2 - Show all orders and totals after applying discounts
    q - Quit
2. Use continue to re-show the menu after invalid input and break to exit on q.
Constraints: Keep the loop logic simple and use only lists and loops (no functions required).'''

orders = []

while True:
    print("\n1 - Add order amount")
    print("2 - Show all orders and totals")
    print("q - Quit")
    choice = input("Choose an action: ").lower()

    if choice == "1":
        order_input = input("Enter order amount: ")
        try:
            order_amount = int(order_input)
            orders.append(order_amount)
            print("Order added.")
        except ValueError:
            print("Invalid order amount.")
        continue

    if choice == "2":
        total = 0
        if not orders:
            print("No orders have been added.")
        else:
            for order_amount in orders:
                if order_amount >= 2000:
                    discount = 0.15
                elif order_amount >= 1500:
                    discount = 0.10
                elif order_amount >= 1000:
                    discount = 0.07
                else:
                    discount = 0.0

                final_amount = order_amount - (order_amount * discount)
                total += final_amount
                print(f"Order Amount: {order_amount} -> Discount: {discount * 100}% -> Final Amount: {final_amount}")

            print(f"Total after discounts: {total}")
        continue

    if choice == "q":
        print("Goodbye.")
        break

    print("Invalid choice. Please choose 1, 2, or q.")
    continue

