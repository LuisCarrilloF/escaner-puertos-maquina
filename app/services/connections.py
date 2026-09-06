import psutil


def get_connections():
    connections = []
    for connection in psutil.net_connections(kind="inet"):
        local = _address(connection.laddr)
        remote = _address(connection.raddr)
        connections.append(
            (
                connection.status or "-",
                connection.pid or "-",
                local,
                remote or "-",
            )
        )
    return sorted(connections, key=lambda item: (str(item[0]), str(item[2])))


def _address(address):
    if not address:
        return ""
    return f"{address.ip}:{address.port}"
