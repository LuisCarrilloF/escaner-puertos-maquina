import platform
import psutil
from services.utils import Convertidor_bytes_to_gb

def Get_system_info():

    informacion = {
        "Sistema operativo": platform.system(),
        "Versión": platform.version(),
        "Arquitectura": platform.architecture(),
        "Nombre del Equipo": platform.node(),
        "Procesador": platform.processor(),
        "Núcleos": psutil.cpu_count(logical=False),
        "RAM Total": str(Convertidor_bytes_to_gb(psutil.virtual_memory().total)) + " GB",
        "Almacenamiento Total": str(Convertidor_bytes_to_gb(psutil.disk_usage('/').total)) + " GB",
        
    }
    
    return informacion