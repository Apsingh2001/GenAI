# GenAI Assignment

This project contains four Python tasks demonstrating conditionals, loops, menu interaction, and loop control.

## Requirements

- Python 3.x
- No external packages are required.

## Running the Tasks

Run each task from this folder:

```bash
python Task1.py
python Task2.py
python Task3.py
python Task4.py
```

## Task 1: Discount Rules

`Task1.py` reads one order amount and applies the discount rules below:

| Order amount | Discount |
| --- | ---: |
| 2000 or more | 15% |
| 1500 to 1999 | 10% |
| 1000 to 1499 | 7% |
| Less than 1000 | 0% |

It prints the discounted amount, subtotal, 5% tax, and final total. The reusable `calculate_discount()` function is also imported by Task 2.

## Task 2: Multiple Orders

`Task2.py` processes the list:

```python
[1200, 2500, 800, 1750, 3000]
```

It uses a `for` loop and Task 1's discount calculation to print each order's discount and final amount. It also prints the total revenue after discounts and the number of discounted orders.

## Task 3: User Menu

`Task3.py` provides a `while`-loop menu:

- `1` adds an order amount to the running list.
- `2` displays all orders and their discounted totals.
- `q` quits the program.

Invalid choices use `continue` to return to the menu, and `break` exits the loop when the user selects `q`.

## Task 4: Daily Sales Loop Control

`Task4.py` processes daily sales using a `for` loop:

```python
[200, 150, 0, 400, 50, -1, 300]
```

- A value of `0` is skipped with `continue`.
- A value of `-1` is treated as corrupted data and stops processing with `break`.
- Positive sales are added to the running total.

The final total is printed after processing stops.
