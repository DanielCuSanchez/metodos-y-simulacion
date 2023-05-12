# Proyecto Parcial 02: Fila de espera con un servidor
# Daniel Cu Sánchez - A01703613
import csv
import random
from datetime import datetime, timedelta
import pandas as pd

# Función para generar tiempo aleatorio
def tiempo_aleatorio(maximo):
    return random.randint(1, maximo)

# Función para generar hora aleatoria
def hora_aleatoria(maximo):
    return (datetime.now() + timedelta(minutes=random.randint(1, maximo))).strftime('%I:%M%p')

# Función para generar la tabla de datos
def generar_tabla(num_clientes, tiempo_max_llegada, tiempo_max_transaccion):
    # Variables para el primer cliente
    hora_llegada = hora_aleatoria(tiempo_max_llegada)
    inicio_servicio = hora_llegada
    tiempo_tramite = tiempo_aleatorio(tiempo_max_transaccion)
    termino_servicio = (datetime.strptime(inicio_servicio, '%I:%M%p') + timedelta(minutes=tiempo_tramite)).strftime('%I:%M%p')
    tiempo_espera_cliente = 0
    tiempo_inactividad_atm = 0

    # Lista para la tabla
    tabla = [['Cliente', 'Tiempo entre llegadas', 'Hora de llegada', 'Tiempo del tramite', 'Inicia servicio', 'Termina servicio', 'Tiempo de espera cliente', 'Tiempo inactividad del ATM']]
    tabla.append(['1', '0', hora_llegada, str(tiempo_tramite), inicio_servicio, termino_servicio, str(tiempo_espera_cliente), str(tiempo_inactividad_atm)])

    # Variables para los siguientes clientes
    for i in range(2, num_clientes + 1):
        tiempo_entre_llegadas = tiempo_aleatorio(5)
        hora_llegada = (datetime.strptime(hora_llegada, '%I:%M%p') + timedelta(minutes=tiempo_entre_llegadas)).strftime('%I:%M%p')
        tiempo_tramite = tiempo_aleatorio(5)
        inicio_servicio = max(hora_llegada, termino_servicio)
        termino_servicio = (datetime.strptime(inicio_servicio, '%I:%M%p') + timedelta(minutes=tiempo_tramite)).strftime('%I:%M%p')
        tiempo_espera_cliente = (datetime.strptime(inicio_servicio, '%I:%M%p') - datetime.strptime(hora_llegada, '%I:%M%p')).total_seconds() / 60
        tiempo_inactividad_atm = (datetime.strptime(inicio_servicio, '%I:%M%p') - datetime.strptime(termino_servicio, '%I:%M%p')).total_seconds() / 60
        tabla.append([str(i), str(tiempo_entre_llegadas), hora_llegada, str(tiempo_tramite), inicio_servicio, termino_servicio, str(tiempo_espera_cliente), str(tiempo_inactividad_atm)])

    return tabla

# Función para calcular las métricas
def calcular_metricas(tabla):
    tiempos_espera = []
    tiempos_servicio = []
    tiempo_inactividad_total = 0
    tiempo_total = 0
    clientes_en_fila = 0

    # Iterar por cada fila en la tabla
    for i in range(1, len(tabla)):
        tiempo_espera = float(tabla[i][6])
        tiempo_servicio = float(tabla[i][3])

        # Agregar el tiempo de espera del cliente a la lista
        tiempos_espera.append(tiempo_espera)

        # Agregar el tiempo de servicio del cliente a la lista
        tiempos_servicio.append(tiempo_servicio)

        # Actualizar el tiempo total
        tiempo_total += tiempo_espera + tiempo_servicio

        # Calcular el tiempo inactivo del ATM
        tiempo_inactividad_atm = abs(float(tabla[i][7]))
        tiempo_inactividad_total += max(0, tiempo_inactividad_atm)

        # Verificar si el cliente tuvo que esperar en la fila
        if tiempo_espera > 0:
            clientes_en_fila += 1

    # Calcular las métricas finales
    tiempo_promedio_espera = sum(tiempos_espera) / len(tiempos_espera)
    probabilidad_espera = clientes_en_fila / len(tabla)
    porcentaje_inactividad = (tiempo_inactividad_total / tiempo_total) * 100
    tiempo_promedio_servicio = sum(tiempos_servicio) / len(tiempos_servicio)

    # Imprimir las métricas finales
    print(f"Tiempo de espera promedio por cliente: {round(tiempo_promedio_espera, 2)} minutos")
    print(f"Probabilidad de que un cliente espera en la fila: {round(probabilidad_espera, 2)}")
    print(f"Porcentaje de tiempo que el cajero estuvo inactivo: {round(porcentaje_inactividad, 2)}%")
    print(f"Tiempo promedio de servicio: {round(tiempo_promedio_servicio, 2)} minutos")

def imprimir_tabla(tabla):
    # Imprimir tabla en consola
    for fila in tabla:
        print(fila)

def crear_csv(tabla):
    # Escribir tabla en archivo CSV
    with open('p2_a01703613.csv', mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        for fila in tabla:
            escritor_csv.writerow(fila)



def main():
    print("Program is running 🏃")
    # Inicialización de variables
    clientes = int(input("Ingrese la cantidad de clientes: "))
    tiempo_max_llegada = int(input("Ingrese el tiempo máximo de llegada de clientes (en minutos): "))
    tiempo_max_transaccion = int(input("Ingrese el tiempo máximo de duración de la transacción (en minutos): "))
    # Generar tabla con 10 clientes
    tabla = generar_tabla(clientes,tiempo_max_llegada, tiempo_max_transaccion)
    # Calcular las métricas
    calcular_metricas(tabla)
    # Generar CSV
    crear_csv(tabla)
    # Imprimir the CSV file
    file_csv = pd.read_csv("p2_a01703613.csv")
    print(file_csv)


if __name__ == "__main__":
    main()