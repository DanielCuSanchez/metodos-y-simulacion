from scipy.stats import norm
import numpy as np

# prueba de aleatoriedad (Prueba de Rachas)
"""
Los signos generados (en caso de que sean muchos, el usuario decidirá si se muestran todos o no)
La cantidad de Rachas calculadas
Los parámetros μ, σ y Zr
Las hipótesis H0 and H1
La conclusión acerca de H0 (es decir, si fue rechazada o no y por qué)
"""

numbers = np.loadtxt("runs_data.txt", dtype=float)

# Generate the signs
signs = np.sign(numbers - np.mean(numbers))
signs[signs == 0] = 1

# Calculate the total number of signs and runs
total_signs = len(signs)
total_runs = len(np.where(np.diff(signs) != 0)[0]) + 1

# Calculate the mean and standard deviation of the number of runs
miu = (2 * total_signs - 1) / 3
sigma = np.sqrt((16 * total_signs - 29) / 90)

# Calculate the z-score and p-value
z_score = (total_runs - miu) / sigma
p_value = 2 * (1 - norm.cdf(abs(z_score)))

# Print the results
print("Generated signs:\n", " ".join(["+" if s == 1 else "-" for s in signs]))
print()
print("Total signs:", total_signs)
print("Total runs:", total_runs)
print()
print("Statistics")
print("Miu =", miu)
print("Sigma =", sigma)
print("Z-score =", z_score)
print()
print("H0: Appearance of the numbers is random")
print("H1: Appearance of the numbers is not random")
if abs(z_score) < 1.96:
    print("Since |{}| < |1.96|, H0 is not rejected".format(z_score))
else:
    print("Since |{}| >= |1.96|, H0 is rejected".format(z_score))

