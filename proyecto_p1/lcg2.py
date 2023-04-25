import math
def lcg(x0, a, c, m, n):
    result = []
    x = x0
    for i in range(n):
        x = (a * x + c) % m
        result.append(x)
    return result


generated_numbers = lcg(7, 3, 1, 127, 500)


observed_counts = [0]*10
for number in generated_numbers:
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


def runs_test(sequence):
    n = len(sequence)
    runs = [sequence[0]]
    for i in range(1, n):
        if sequence[i] != sequence[i-1]:
            runs.append(sequence[i])
    k = len(runs)
    pi = float(sum(sequence))/n
    v = float(2*n-1-k)/3
    s = float(n-pi*n*(1-pi))/math.sqrt(pi*(1-pi)*n)
    z = (v-s)/math.sqrt(2*v)
    critical_value = 1.96
    if abs(z) < critical_value:
        print("The generated numbers have a random distribution.")
    else:
        print("The generated numbers do not have a random distribution.")


runs_test(generated_numbers)
