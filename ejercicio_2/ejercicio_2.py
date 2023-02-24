#Daniel Cu Sánchez - A01703613 - 23-02-23
from matplotlib import pyplot as plt #Library for graphs
import numpy as np #Library for managing data
# Input number
number = int(input("Choose a number\n1) data01.txt\n2) data02.txt\n3) data03.txt\nType:"))

# Text file data converted to integer data type
match number:
  case 1:
    file = "data01.txt"
    intervals=11
  case 2:
    file = "data02.txt"
    intervals=11
  case 3:
    file = "data03.txt"
    intervals=7
# Load array
array_data = np.loadtxt(file, dtype=float)
counts, edges, bars= plt.hist(array_data, bins=intervals, alpha=0.7, edgecolor='k', linewidth=1)
# Print histogram
plt.title("Histogram")
plt.xlabel("Intervals")
plt.ylabel('Frequency')
plt.bar_label(bars)
plt.show()
