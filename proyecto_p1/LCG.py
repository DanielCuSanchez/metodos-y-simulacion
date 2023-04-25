import matplotlib.pyplot as plt

# método lineal congruencial (L.C.G.)
#Linear congruential method: Generate 500 numbers with the following parameters: X0 = 7, a = 3, c = 1, m = 127.
def lcg(seed):
    while True:
        seed = ((3 * seed + 1) % 127)
        yield seed / 100
rand = lcg(7)
values = [next(rand) for _ in range(500)]
print(values)

with open('output.txt', 'w') as f:
    for value in values:
        f.write(format(value))
        f.write('\n')

plt.hist(values, bins=500, edgecolor='k', color = '#0c1881', histtype = 'bar')
plt.show()



