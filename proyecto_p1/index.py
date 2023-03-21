from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# método lineal congruencial (L.C.G.)
#Linear congruential method: Generate 10 numbers with the following parameters: X0 = 6, a = 32, c = 3, m = 80.
def lcg(seed):
    while True:
        seed = ((32 * seed + 3) % 80)
        yield seed / 80
rand = lcg(6)
values = [next(rand) for _ in range(10)]
print(values)

plt.hist(values, bins=10, edgecolor='k', color = '#0c1881', histtype = 'bar')
plt.show()

#prueba de aleatoriedad (Prueba de Rachas)
"""
Los signos generados (en caso de que sean muchos, el usuario decidirá si se muestran todos o no)
La cantidad de Rachas calculadas
Los parámetros μ, σ y Zr
Las hipótesis H0 and H1
La conclusión acerca de H0 (es decir, si fue rechazada o no y por qué)
"""




#prueba de aleatoriedad (Prueba de Chi-cuadrada)
"""
La tabla de frecuencias (con C = 10 y W = 0.1), mostrando los intervalos, frecuencias observadas y esperadas (no es obligatorio mostrar las operaciones, aunque yo las muestre en mi ejemplo)
el valor de χ2
las hipótesis H0 and H1
la conclusión acerca de H0 (es decir, si fue rechazada o no y por qué)
"""
#Run the chi-squared test with the following numbers: chi_data.txt
#Run the chi-squared test with the following numbers: runs_data.txt


# defining the table
data = [[6, 2, 13], [49, 26, 14], [170, 134, 112], [132, 159, 128], [12, 19, 24]]
stat, p, dof, expected = chi2_contingency(data)
# print(expected)
print("Chi-Square Value is :", stat)
# interpret p-value
alpha = 0.01
print("p value is " + str(p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (H0 holds true)')
