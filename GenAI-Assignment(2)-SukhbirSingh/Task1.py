# Discount Rules (if / elif / else)
'''
Write a program that reads an integer order_amount from the user using input().
'''
def calculate_discount(order_amount):
    if order_amount >= 2000:
        return 0.15
    elif order_amount >= 1500:
        return 0.10
    elif order_amount >= 1000:
        return 0.07
    else:
        return 0.0


if __name__ == "__main__":
    order_amount = input("Enter the order amount: ")

    try:
        order_amount = int(order_amount)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit()

    discount = calculate_discount(order_amount)
    final_amount = order_amount - (order_amount * discount)

    print(f"Final amount after discount: {final_amount}")

    tax_rate = 0.05
    subtotal = final_amount
    tax = subtotal * tax_rate
    final_total = subtotal + tax

    print(f"Subtotal: {subtotal}")
    print(f"Tax: {tax}")
    print(f"Final Total: {final_total}")