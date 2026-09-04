import socket
import psutil


def Get_network_info():

    informacion_red = {}
    interfaces = psutil.net_if_addrs()

    for nombre_interfaz, direcciones in interfaces.items():

        informacion_red[nombre_interfaz] = {}

        for direccion in direcciones:

            if direccion.family == socket.AF_INET:
                informacion_red[nombre_interfaz]["IPv4"] = direccion.address

            elif direccion.family == psutil.AF_LINK:
                informacion_red[nombre_interfaz]["MAC"] = direccion.address

    return informacion_red