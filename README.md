# Escáner de Puertos y Equipo

Herramienta para analizar las características del equipo y facilitar un diagnóstico técnico, además de verificar qué puertos están abiertos en la máquina.

## Descripción

Este proyecto está pensado para ayudar a revisar el estado del sistema y detectar servicios activos mediante un escaneo de puertos. También permite obtener información útil del equipo para apoyar diagnósticos rápidos y más claros.

## Características

- Diagnóstico básico del equipo.
- Verificación de puertos abiertos.
- Interfaz gráfica con Python y Tkinter.
- Estructura modular para facilitar mantenimiento y ampliación.

## Requisitos

- Python 3.13
- Windows 10 o 11
- pip actualizado

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/LuisCarrilloF/escaner-puertos-maquina.git
cd escaner-puertos-maquina
```

2. Crea un entorno virtual:

```powershell
& "C:\Users\luisa\AppData\Local\Programs\Python\Python313\python.exe" -m venv .venv
```

3. Activa el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Instala las dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> Si el archivo `requirements.txt` no carga correctamente, puedes instalar la dependencia principal manualmente:
>
> ```bash
> python -m pip install psutil==7.2.2
> ```

## Cómo ejecutarlo

Desde la raíz del proyecto, ejecuta:

```bash
python app\main.py
```

O bien, desde la carpeta `app`:

```bash
cd app
python main.py
```

La aplicación abrirá la interfaz gráfica y comenzará el análisis del equipo y los puertos.

## Estructura del proyecto

```text
escaner-puertos-maquina/
├── app/
│   ├── main.py
│   ├── services/
│   └── views/
├── .gitignore
├── README.md
├── requirements.txt
└── .venv/
```

## Mantenimiento

Para actualizar el archivo de dependencias, puedes ejecutar:

```bash
pip freeze > requirements.txt
```

## Licencia

Este proyecto está disponible para uso personal y educativo.