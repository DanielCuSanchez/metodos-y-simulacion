#Daniel Cu Sánchez - A01703613 - 23-02-23
from matplotlib import pyplot as plt #Library for graphs
import pandas as pd
import math
import numpy as np #Library for managing data
# Input number
number = int(input("Choose a number\n1) data01.txt\n2) data02.txt\n3) data03.txt\nType:"))

# Text file data converted to integer data type
match number:
  case 1:
    file = "numbers01.txt"
  case 2:
    file = "data02.txt"
  case 3:
    file = "data03.txt"
# Load array
array_data = np.loadtxt(file, dtype=float)

classes = math.ceil(1 + (3.3 * math.log10(array_data.size)))
w = array_data.size / classes
print("c = ",classes)
print("max = ",array_data.max())
print("min = ",array_data.min())
print("w = ", (array_data.max() - array_data.min()) / classes) #data - menor / clasess
table = np.histogram(array_data,classes)

n, bins, bars= plt.hist(array_data, bins=classes, alpha=0.7, edgecolor='k', linewidth=1)
print("table = ", bins)
print("sum of frequencies = ",  np.array(n).sum())
# Print histogram
plt.title("Histogram")
plt.xlabel("Intervals")
plt.ylabel('Frequency')
plt.bar_label(bars)
plt.show()
