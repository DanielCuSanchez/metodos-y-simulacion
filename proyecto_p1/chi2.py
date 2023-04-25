# import the observed numbers
import math
import numpy as np
numbers = np.loadtxt("output.txt", dtype=float)


observed_counts = [0]*10
for number in numbers:
    interval = math.floor(number/13)
    observed_counts[interval] += 1

expected_counts = [50]*10
chi_squared = sum([((observed_counts[i]-expected_counts[i])
                  ** 2)/expected_counts[i] for i in range(10)])

critical_value = 16.92
if chi_squared < critical_value:
    print("The generated numbers are consistent with a uniform distribution.")
else:
    print("The generated numbers are not consistent with a uniform distribution.")
