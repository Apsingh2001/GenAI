'''
Loop Control with Conditions (break & continue)
1. Given a list of daily sales: daily = [200, 150, 0, 400, 50, -1, 300], iterate through it with
a for loop and:
o If a day's value is -1, treat it as corrupted data and break the loop (stop
processing).
o If a day's value is 0, treat it as a day with no sales and continue (skip adding to
revenue).
o For valid positive sales, add to total_sales and print the running total.
2. Print the final total after the loop completes (or stops due to corrupted data).
'''

daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sales in daily:
    if sales == -1:
        print("Corrupted data found. Stopping sales processing.")
        break

    if sales == 0:
        continue

    total_sales += sales
    print(f"Running total: {total_sales}")

print(f"Final total sales: {total_sales}")