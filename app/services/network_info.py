import socket
import psutil


def Get_network_info():

    informacion_red = {}
    interfaces = psutil.net_if_addrs()
    estados_interfaces = psutil.net_if_stats()
    for nombre_interfaz, direcciones in interfaces.items():
        estado = estados_interfaces.get(nombre_interfaz)
        if estado is None or not estado.isup:
            continue

        informacion_red[nombre_interfaz] = {}

        for direccion in direcciones:

            if direccion.family == socket.AF_INET:
                if direccion.address.startswith("127."):
                    continue
                informacion_red[nombre_interfaz]["IPv4"] = direccion.address

            elif direccion.family == psutil.AF_LINK:
                informacion_red[nombre_interfaz]["MAC"] = direccion.address

    return informacion_red