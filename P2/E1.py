import random
import csv
import pandas as pd


class Cliente:
    def __init__(self, llegada, duracion):
        self.llegada = llegada
        self.duracion = duracion
        self.inicio = None
        self.fin = None
        self.espera = None

class CajeroAutomatico:
    def __init__(self):
        self.cliente_actual = None
        self.tiempo_inactivo = 0
        self.tiempo_total_servicio = 0
        self.tiempo_ultimo_servicio = 0

    def atender_cliente(self, cliente, tiempo_actual):
        cliente.inicio = tiempo_actual
        cliente.fin = tiempo_actual + cliente.duracion
        cliente.espera = tiempo_actual - cliente.llegada
        self.tiempo_total_servicio += cliente.duracion
        self.tiempo_ultimo_servicio = cliente.duracion
        self.cliente_actual = cliente

    def actualizar(self, tiempo_actual):
        if not self.cliente_actual:
            self.tiempo_inactivo += 1
        elif tiempo_actual == self.cliente_actual.fin:
            self.cliente_actual = None

def simular(num_clientes, max_llegada, max_duracion):
    clientes = []
    cajero = CajeroAutomatico()
    tiempo_actual = 0
    for i in range(num_clientes):
        llegada = tiempo_actual + random.randint(1, max_llegada)
        duracion = random.randint(1, max_duracion)
        clientes.append(Cliente(llegada, duracion))
        tiempo_actual = llegada

    with open('p2_a01703613.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Cliente', 'Tiempo de llegada', 'Duracion del tramite', 'Tiempo de inicio', 'Tiempo de finalizacion', 'Tiempo de espera'])
        for i, cliente in enumerate(clientes):
            while tiempo_actual < cliente.llegada:
                cajero.actualizar(tiempo_actual)
                tiempo_actual += 1
            cajero.atender_cliente(cliente, tiempo_actual)
            writer.writerow([i+1, cliente.llegada, cliente.duracion, cliente.inicio, cliente.fin, cliente.espera])

    tiempo_promedio_espera = sum([cliente.espera for cliente in clientes]) / num_clientes
    probabilidad_espera = sum([1 for cliente in clientes if cliente.espera > 0]) / num_clientes
    porcentaje_inactivo = cajero.tiempo_inactivo / tiempo_actual * 100
    tiempo_promedio_servicio = cajero.tiempo_total_servicio / num_clientes
    
    # Read the CSV file
    file_csv = pd.read_csv("p2_a01703613.csv")
    print(file_csv)
    print(f'Tiempo promedio de espera por cliente: {tiempo_promedio_espera:.2f}')
    print(f'Probabilidad de esperar en la fila: {probabilidad_espera*100:.2f}%')
    print(f'Porcentaje de tiempo inactivo del cajero: {porcentaje_inactivo:.2f}%')
    print(f'Tiempo promedio de servicio: {tiempo_promedio_servicio:.2f}')

simular(10, 5, 2)