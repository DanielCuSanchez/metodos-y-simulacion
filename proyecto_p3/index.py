import sys
import numpy as np

# Función que representa un ataque de un grupo a otro
def atacar(matriz, grupos):
    # Creamos un vector para registrar el número original de cada grupo
    grupo_numeros = np.arange(len(grupos)) + 1
    while np.count_nonzero(grupos) > 1: # Mientras exista más de un grupo vivo
        # Seleccionamos aleatoriamente el grupo atacante de los grupos que aún tienen guerreros y tienen posibles víctimas
        posibles_atacantes = np.where((grupos > 0) & (np.sum(matriz > 0, axis=1) > 0))[0]
        if len(posibles_atacantes) == 0:  # Si no hay posibles atacantes, se sale del bucle
            break
        atacante = np.random.choice(posibles_atacantes)
        # Seleccionamos las posibles víctimas del ataque (aquellos grupos a los que el grupo atacante puede atacar)
        posibles_victimas = np.where(matriz[atacante] > 0)[0]
        # Seleccionamos aleatoriamente la víctima del ataque en base a las probabilidades de la matriz estocástica
        victima = np.random.choice(posibles_victimas, p=matriz[atacante][posibles_victimas])
        # Reducimos el número de guerreros del grupo víctima
        grupos[victima] -= 1
        print(f"Grupo {grupo_numeros[atacante]} ataco al Grupo {grupo_numeros[victima]}!")
        # Si el grupo víctima ha sido aniquilado, reconfiguramos la matriz estocástica y el vector de grupos
        if grupos[victima] == 0:
            print(f"Grupo {grupo_numeros[victima]} ha sido aniquilado!\n")
            matriz = reconfigurar_matriz(matriz, victima)
            grupos = np.delete(grupos, victima)  # Elimina la entrada correspondiente al grupo aniquilado
            grupo_numeros = np.delete(grupo_numeros, victima)  # Actualiza el vector de números de grupo
            print("Reconfigurando matriz estocastica\n")
            imprimir_matriz(matriz)
        print("Numero de guerreros por cada grupo")
        imprimir_grupos(grupos)
    print("===============================\n")
    ganador = np.where(grupos > 0)[0]
    if ganador.size > 0:
        print("El ganador es el Grupo", grupo_numeros[ganador[0]], "\n")
    else:
        print("No hay ganadores\n")
    print("===============================\n")





# Función para reconfigurar la matriz estocástica cuando un grupo es aniquilado
def reconfigurar_matriz(matriz, indice):
    matriz = np.delete(matriz, indice, 0) # Eliminamos la fila correspondiente al grupo aniquilado
    matriz = np.delete(matriz, indice, 1) # Eliminamos la columna correspondiente al grupo aniquilado
    # Normalizamos las filas de la matriz para que sigan siendo estocásticas
    for i in range(len(matriz)):
        suma_de_fila = np.sum(matriz[i])
        # Si la suma total de la fila es diferente de cero, dividimos cada elemento por la suma total
        if suma_de_fila != 0:
            matriz[i] /= suma_de_fila
    return matriz



# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(round(matriz[i][j], 2), end="\t")
        print()

# Función para imprimir los grupos
def imprimir_grupos(grupos):
    for i in range(len(grupos)):
        print(f"Grupo {i + 1}: {grupos[i]}")
    print("==================================\n")


# Función para generar la matriz estocástica de forma aleatoria
def generar_matriz_aleatoria(n):
    matriz = np.random.random((n, n)) # Genera una matriz nxn con números aleatorios entre 0 y 1
    np.fill_diagonal(matriz, 0) # Los guerreros de un grupo no pueden atacarse entre sí
    # Normalizamos las filas para que sean estocásticas
    matriz /= matriz.sum(axis=1, keepdims=True)
    return matriz

# Función para generar la cantidad de guerreros por grupo de forma aleatoria
def generar_guerreros(n):
    guerreros = np.random.randint(5, 15, n) # Genera un número aleatorio de guerreros por grupo entre 5 y 15
    return guerreros

# Función principal
def main():
    # Número de grupos
    n = int(input("Ingresa a cantidad de grupos: "))
    # Cambiamos la salida estándar al archivo output.txt
    sys.stdout = open('output.txt', 'w')

    # Generamos los grupos y la matriz estocástica de forma aleatoria
    grupos = generar_guerreros(n)
    matriz = generar_matriz_aleatoria(n)

    print("Matriz inicial:")
    imprimir_matriz(matriz)
    print("Numero de guerreros por cada grupo")
    imprimir_grupos(grupos)

    # Comenzamos la batalla
    atacar(matriz, grupos)

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
