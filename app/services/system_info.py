import platform
import psutil

def Get_system_info():
    bytes_por_gb = 1024 ** 3
    informacion = {
        "Sistema operativo": platform.system(),
        "Versión": platform.version(),
        "Arquitectura": platform.architecture(),
        "Nombre del Equipo": platform.node(),
        "Procesador": platform.processor(),
        "Núcleos": psutil.cpu_count(logical=False),
        "RAM Total": str(round(psutil.virtual_memory().total / bytes_por_gb, 2)) + " GB",
        "Almacenamiento Total": str(round(psutil.disk_usage('/').total / bytes_por_gb, 2)) + " GB",
        
    }
    
    return informacion