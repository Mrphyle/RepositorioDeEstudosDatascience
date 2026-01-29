from statistics import variance
from statistics import stdev
from statistics import mean
import numpy as np
data = [1.90, 1.69, 1.53, 1.57, 1.66, 1.66, 1.76, 1.58, 1.81, 1.80, 1.75, 1.65, 1.75, 1.60, 1.64, 1.58, 1.75, 1.90, 1.78, 1.73, 1.83, 1.68, 1.84, 1.76, 1.65, 1.78, 2.13, 1.78]
range_of_data = np.max(data) - np.min(data)
data.sort(reverse=False)
print(data)
print(f"the range of list is {range_of_data}")
variance_of_data = variance(data)
print(f"the variance of list is {variance_of_data}")
standard_deviation = stdev(data)
print(f"the standard deviation of list is {standard_deviation}")
variation_percent = standard_deviation/mean(data)*100
print(f"the variation percent of list is {variation_percent}%")