import pandas as pd
import random
import datetime

# Inicialización de variables
clientes = int(input("Ingrese la cantidad de clientes: "))
tiempo_max_llegada = int(input("Ingrese el tiempo máximo de llegada de clientes (en minutos): "))
tiempo_max_transaccion = int(input("Ingrese el tiempo máximo de duración de la transacción (en minutos): "))

# Creación de DataFrame
df = pd.DataFrame(columns=['Hora de llegada', 'Hora de inicio', 'Hora de fin', 'Tiempo de espera', 'Tiempo transaccion'])

# Variables de tiempo
hora_actual = datetime.datetime.now().replace(microsecond=0, second=0)
hora_inicio = hora_actual
hora_fin = hora_actual
tiempo_transaccion_total = datetime.timedelta(0)
tiempo_inactivo_total = datetime.timedelta(0)

# Creación de clientes
for i in range(clientes):
    # Tiempo de llegada
    tiempo_llegada = datetime.timedelta(minutes=random.randint(0, tiempo_max_llegada))
    hora_llegada = hora_actual + tiempo_llegada

    # Tiempo de transacción
    tiempo_transaccion = datetime.timedelta(minutes=random.randint(1, tiempo_max_transaccion))
    tiempo_transaccion_total += tiempo_transaccion

    # Tiempo de espera
    tiempo_espera = hora_inicio - hora_llegada
    if tiempo_espera < datetime.timedelta(0):
        tiempo_espera = datetime.timedelta(0)

    df.loc[i] = [hora_llegada.time(), hora_inicio.time(), hora_fin.time(), tiempo_espera, tiempo_transaccion]

    # Actualización de variables de tiempo
    hora_inicio = hora_fin
    hora_fin += tiempo_transaccion
    tiempo_inactivo = hora_inicio - hora_fin
    if tiempo_inactivo > datetime.timedelta(0):
        tiempo_inactivo_total += tiempo_inactivo


# Cálculo de estadísticas
espera_promedio = df['Tiempo de espera'].mean()
probabilidad_espera = len(df[df['Tiempo de espera'] > datetime.timedelta(0)]) / clientes
porcentaje_inactivo = df['Tiempo de espera'].iloc[-1] / (hora_fin - hora_actual)
tiempo_promedio = (hora_fin - hora_inicio) / clientes

# Muestra de resultados
print(df)
print("El tiempo de espera promedio por cliente es:", espera_promedio)
print("La probabilidad de que un cliente espere en la fila es:", probabilidad_espera)
print("El porcentaje de tiempo que el cajero estuvo inactivo es:", porcentaje_inactivo)
print("El tiempo promedio de servicio es:", tiempo_promedio)