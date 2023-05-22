import random
from datetime import datetime, timedelta


class Cliente:
    def __init__(self, id, tiempo_llegada, duracion_tramite):
        self.id = id
        self.tiempo_llegada = tiempo_llegada
        self.duracion_tramite = duracion_tramite
        self.tiempo_inicio = None
        self.tiempo_fin = None
        self.tiempo_espera = None


class CajeroAutomatico:
    def __init__(self):
        self.tiempo_fin = datetime.now()

    def atender(self, cliente):
        cliente.tiempo_inicio = max(cliente.tiempo_llegada, self.tiempo_fin)
        cliente.tiempo_fin = cliente.tiempo_inicio + \
            timedelta(seconds=cliente.duracion_tramite)
        self.tiempo_fin = cliente.tiempo_fin


def main(num_clientes, max_tiempo_llegada, max_duracion_tramite):
    clientes = []
    for i in range(num_clientes):
        tiempo_llegada = datetime.now() + timedelta(seconds=random.randint(0, max_tiempo_llegada))
        duracion_tramite = random.randint(1, max_duracion_tramite)
        clientes.append(Cliente(i+1, tiempo_llegada, duracion_tramite))

    cajero = CajeroAutomatico()

    with open('resultado_simulacion.txt', 'w') as file:
        for cliente in clientes:
            espera = cliente.tiempo_inicio - cliente.tiempo_llegada
            file.write(
                f"Cliente {cliente.id} se formó en la fila a las {cliente.tiempo_llegada.strftime('%H:%M:%S')}, esperó {espera.seconds} segundos\n")
            cajero.atender(cliente)
            file.write(
                f"Cliente {cliente.id} inició su trámite a las {cliente.tiempo_inicio.strftime('%H:%M:%S')}\n")
            file.write(
                f"Cliente {cliente.id} finalizó su trámite a las {cliente.tiempo_fin.strftime('%H:%M:%S')}\n")
            cliente.tiempo_espera = espera.seconds

        tiempo_inactivo = (cajero.tiempo_fin - datetime.now()).seconds
        file.write(f"El cajero estuvo inactivo {tiempo_inactivo} segundos\n")

        tiempo_espera_promedio = sum(
            [c.tiempo_espera for c in clientes]) / num_clientes
        file.write(
            f"El tiempo de espera promedio por cliente fue de {tiempo_espera_promedio:.2f} segundos\n")

        probabilidad_espera = len(
            [c for c in clientes if c.tiempo_espera > 0]) / num_clientes
        file.write(
            f"La probabilidad de que un cliente espera en la fila fue de {probabilidad_espera:.2%}\n")

        porcentaje_inactivo = tiempo_inactivo / \
            (cajero.tiempo_fin - clientes[0].tiempo_llegada).seconds
        file.write(
            f"El porcentaje de tiempo que el cajero estuvo inactivo fue de {porcentaje_inactivo:.2%}\n")

        tiempo_servicio_promedio = sum(
            [c.duracion_tramite for c in clientes]) / num_clientes
        file.write(f"El tiempo promedio de servicio fue de {tiempo_servicio}")
