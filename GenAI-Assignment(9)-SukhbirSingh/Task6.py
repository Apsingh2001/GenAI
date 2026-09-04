import numpy as np


marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
sorted_marks = np.sort(marks)
average_marks = np.mean(marks)
above_average_count = np.sum(marks > average_marks)

print("Sorted array:", sorted_marks)
print("25th percentile:", np.percentile(marks, 25))
print("50th percentile:", np.percentile(marks, 50))
print("75th percentile:", np.percentile(marks, 75))
print("Students above average:", above_average_count)
