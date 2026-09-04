import numpy as np


marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

mean = np.mean(marks)
median = np.median(marks)
variance = np.var(marks)
standard_deviation = np.std(marks)
minimum = np.min(marks)
maximum = np.max(marks)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard deviation:", standard_deviation)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Range:", maximum - minimum)
