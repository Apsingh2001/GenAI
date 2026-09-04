import numpy as np


sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])
total_sales = np.sum(sales)
average_sales = np.mean(sales)
highest_day = np.argmax(sales) + 1
lowest_day = np.argmin(sales) + 1
above_average_days = np.where(sales > average_sales)[0] + 1

print("Total weekly sales:", total_sales)
print("Average daily sales:", average_sales)
print("Highest sales day:", highest_day, "with sales of", sales[highest_day - 1])
print("Lowest sales day:", lowest_day, "with sales of", sales[lowest_day - 1])
print("Standard deviation of sales:", np.std(sales))
print("Days with sales above average:", above_average_days)
