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



