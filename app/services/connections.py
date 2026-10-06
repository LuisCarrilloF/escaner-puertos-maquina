import ipaddress

import psutil


def get_connections(collapse_loopback=False):
    connections = []
    process_names = {}
    seen_loopback = set()

    for connection in psutil.net_connections(kind="inet"):
        local = _address(connection.laddr)
        remote = _address(connection.raddr)
        pid = connection.pid
        process_name = _process_name(pid, process_names)

        if collapse_loopback and _is_loopback_pair(connection.laddr, connection.raddr):
            loopback_key = (pid, _address_key(connection.laddr), _address_key(connection.raddr))
            reverse_key = (pid, loopback_key[2], loopback_key[1])
            if reverse_key in seen_loopback:
                continue
            seen_loopback.add(loopback_key)

        connections.append(
            (
                connection.status or "-",
                pid if pid is not None else "-",
                process_name,
                local,
                remote or "-",
            )
        )
    return sorted(connections, key=lambda item: (str(item[0]), str(item[3])))


def _process_name(pid, cache):
    if pid is None:
        return "desconocido"
    if pid not in cache:
        try:
            cache[pid] = psutil.Process(pid).name()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            cache[pid] = "desconocido"
    return cache[pid]


def _address_key(address):
    if not address:
        return ""
    return (address.ip, address.port)


def _is_loopback_pair(local, remote):
    if not local or not remote:
        return False
    try:
        return ipaddress.ip_address(local.ip).is_loopback and ipaddress.ip_address(remote.ip).is_loopback
    except ValueError:
        return False


def _address(address):
    if not address:
        return ""
    return f"{address.ip}:{address.port}"
