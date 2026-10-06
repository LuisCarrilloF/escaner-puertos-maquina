import psutil
import socket


def get_listening_ports():
    ports = []
    for connection in psutil.net_connections(kind="inet"):
        if connection.status != psutil.CONN_LISTEN:
            continue
        address = _address(connection.laddr)
        process = _process_name(connection.pid)
        protocol = "TCP" if connection.type == socket.SOCK_STREAM else "UDP"
        ports.append((protocol, address, process))
    return sorted(ports, key=lambda item: item[1])


def _address(address):
    if not address:
        return "-"
    return f"{address.ip}:{address.port}"


def _process_name(pid):
    if not pid:
        return "Sistema"
    try:
        return psutil.Process(pid).name()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return f"PID {pid}"
