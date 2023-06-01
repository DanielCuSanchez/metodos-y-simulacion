import sys
import numpy as np

def atacar(matriz, grupos):
    while np.count_nonzero(grupos) > 1:
        atacante = np.random.choice(np.where(grupos > 0)[0])
        posibles_victimas = np.where(matriz[atacante] > 0)[0]
        if len(posibles_victimas) == 0:  # if there is no one to attack, skip
            continue
        victima = np.random.choice(posibles_victimas, p=matriz[atacante][posibles_victimas])
        grupos[victima] -= 1
        if grupos[victima] == 0:
            matriz = reconfigurar_matriz(matriz, victima)
            print(f"Grupo {victima + 1} es aniquilado!\n")
            print("Reconfigurando matriz estocástica\n")
            print_matriz(matriz)
        print(f"Grupo {atacante + 1} atacó al Grupo {victima + 1}!")
        print("Número de guerreros por cada grupo")
        print_grupos(grupos)
    print("El ganador es el Grupo", np.where(grupos > 0)[0][0] + 1, "\n")

def reconfigurar_matriz(matriz, indice):
    matriz = np.delete(matriz, indice, 0)
    matriz = np.delete(matriz, indice, 1)
    for i in range(len(matriz)):
        matriz[i] /= np.sum(matriz[i])
    return matriz

def print_matriz(matriz):
    for i in range(len(matriz)):
        print("\t", end="")
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()

def print_grupos(grupos):
    for i in range(len(grupos)):
        print(f"Grupo {i + 1}: {grupos[i]}")
    print("==================================\n")

def main():
    sys.stdout = open('output.txt', 'w')
    grupos = np.array([50, 40, 60])
    matriz = np.array([[0.0, 0.4, 0.6], [0.2, 0.0, 0.8], [0.15, 0.85, 0.0]])
    print("Matriz inicial:")
    print_matriz(matriz)
    print("Número de guerreros por cada grupo")
    print_grupos(grupos)
    atacar(matriz, grupos)

if __name__ == "__main__":
    main()
