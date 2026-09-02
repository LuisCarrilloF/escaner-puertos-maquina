from socket import socket

import psutil

def Get_network_info():
    informacion_red = {
        "Dirección IP": psutil.net_if_addrs()['Wi-Fi'][3].address,
    }
    print(psutil.net_if_addrs())
    return informacion_red