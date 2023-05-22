import random

# Función para generar un tiempo aleatorio en segundos
def tiempo_aleatorio(max_tiempo):
    return random.randint(1, max_tiempo)

# Pedir al usuario la cantidad de clientes, el tiempo máximo de llegada y de trámite
num_clientes = int(input("Ingrese la cantidad de clientes: "))
max_tiempo_llegada = int(input("Ingrese el tiempo máximo de llegada de los clientes (en segundos): "))
max_tiempo_tramite = int(input("Ingrese el tiempo máximo de trámite en el cajero (en segundos): "))

# Inicializar variables para el seguimiento de tiempos
hora_actual = 0
tiempo_espera_total = 0
tiempo_servicio_total = 0
tiempo_inactivo = 0

# Inicializar la lista de clientes
clientes = []

# Generar la lista de clientes con tiempos aleatorios de llegada y trámite
for i in range(num_clientes):
    tiempo_llegada = hora_actual + tiempo_aleatorio(max_tiempo_llegada)
    tiempo_tramite = tiempo_aleatorio(max_tiempo_tramite)
    clientes.append((tiempo_llegada, tiempo_tramite))
    hora_actual = tiempo_llegada

# Inicializar el archivo de salida
archivo_salida = open("simulacion_cajero.txt", "w")

# Recorrer la lista de clientes y calcular los tiempos de espera y de servicio
for i in range(num_clientes):
    hora_llegada = clientes[i][0]
    hora_inicio = max(hora_llegada, hora_actual)
    hora_final = hora_inicio + clientes[i][1]
    tiempo_espera = hora_inicio - hora_llegada
    tiempo_servicio = hora_final - hora_inicio
    tiempo_espera_total += tiempo_espera
    tiempo_servicio_total += tiempo_servicio
    tiempo_inactivo += hora_inicio - hora_actual
    hora_actual = hora_final

    # Escribir los resultados en el archivo de salida
    archivo_salida.write("Cliente " + str(i+1) + ":\n")
    archivo_salida.write("Hora de llegada: " + str(hora_llegada) + " segundos\n")
    archivo_salida.write("Hora de inicio de trámite: " + str(hora_inicio) + " segundos\n")
    archivo_salida.write("Hora de finalización de trámite: " + str(hora_final) + " segundos\n")
    archivo_salida.write("Tiempo de espera: " + str(tiempo_espera) + " segundos\n")
    archivo_salida.write("Tiempo de servicio: " + str(tiempo_servicio) + " segundos\n\n")

# Calcular y escribir los resultados finales en el archivo de salida
archivo_salida.write("Resultados finales:\n")
archivo_salida.write("Tiempo promedio de espera por cliente: " + str(tiempo_espera_total/num_clientes) + " segundos\n")
archivo_salida.write("Probabilidad de que un cliente espere en la fila: " + str(tiempo_espera_total/hora_actual))
