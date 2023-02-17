#Daniel Cu Sánchez - A01703613
from random import randint
import matplotlib.pyplot as plot
import numpy as np

#Input number of simulations for the dice (Example 1000)
quantity = int(input("Type how many simulations do you want for the dice: "))
simulation = []
for i in range(quantity):
  simulation.append(randint(1,6))
print(simulation)

# Generate histogram with mathplotlib
intervalos = (1,2,3,4,5,6,7)
plot.hist(x=simulation, bins=intervalos, color='#6da7f2', rwidth=0.9)
plot.title('Histograma de simulación de caras de dados - Daniel Cu')
plot.xlabel('Caras')
plot.ylabel('Frecuencia')
plot.show() # Show the histogram

#Generate histogram with numpy as a comprobation
frecuencias, extremos = np.histogram(simulation, bins=intervalos, range=(0,6))
print(frecuencias, extremos)