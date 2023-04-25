import numpy as np
from scipy.stats import chisquare
# prueba de aleatoriedad (Prueba de Chi-cuadrada)
"""
La tabla de frecuencias (con C = 10 y W = 0.1), mostrando los intervalos, frecuencias observadas y esperadas (no es obligatorio mostrar las operaciones, aunque yo las muestre en mi ejemplo)
el valor de χ2
las hipótesis H0 and H1
la conclusión acerca de H0 (es decir, si fue rechazada o no y por qué)
"""
# Run the chi-squared test with the following numbers: chi_data.txt

# import the observed values
values = np.loadtxt("output.txt", dtype=float)
# round the values to 3 decimals
observed = np.around(values, 3)
# define the expected values
expected = np.repeat(3.0, 10)
# define the intervals
intervals = np.linspace(0, 1, 11)
# calculate the observed frequencies
observedfrequencies, _ = np.histogram(observed, intervals)
# we can not calculate the expected

# calculate the chi-square statistic and p-value
chisquared, pvalue = chisquare(observedfrequencies, expected)
# calculate the chi-square contributions for each interval
chisquaredcontributions = ((observedfrequencies - expected)**2) / expected

# print the table
print("Intervals  \t\t Observed  \t\t  Expected\t(O - E)^2 / E")
for i in range(len(intervals) - 1):
  print("[{:.3f} - {:.3f})\t{}\t\t{:.3f}\t\t{:.3f}"
    .format(
    intervals[i],
    intervals[i+1],
    observedfrequencies[i],
    expected[i],
    chisquaredcontributions[i]
    )
  )

print()
print("--------------------")
print()
print("χ2 = {: 0.3f}".format(chisquared))
print()

print("H0: Generated numbers are not different from the uniform distribution")
print("H1: Generated numbers are different from the uniform distribution")

#Conclusion
if chisquared > 16.91:
  print()
  print("Since {:0.3f} > 16.91, H0 is rejected".format(chisquared))
else:
  print()
  print("Since {:0.3f} <= 16.91, H0 is not rejected".format(chisquared))
