import tkinter as Tk
from services.system_info import Get_system_info
from services.network_info import Get_network_info
def main():
    informacion_maquina = Get_system_info()
    root = Tk.Tk()
    root.title("SysScope - Escaner de diagnostico")
    root.geometry("1200x740")
    root.minsize(900, 600)
    root.configure(bg="#0b0f14")

    color_panel = "#151b22"
    color_border = "#303944"
    color_text = "#c7d2e0"
    color_muted = "#8393a8"
    color_blue = "#3da5ff"
    color_green = "#42d36f"

    barra_superior = Tk.Frame(root, bg="#171d24", height=64)
    barra_superior.pack(fill="x", padx=18, pady=(16, 0))
    barra_superior.pack_propagate(False)

    Tk.Label(
        barra_superior,
        text="[ SysScope ]",
        font=("Consolas", 15, "bold"),
        fg=color_blue,
        bg="#171d24",
    ).pack(side="left", padx=(20, 14))
    Tk.Label(
        barra_superior,
        text="Escaner de diagnostico del sistema",
        font=("Consolas", 10),
        fg=color_muted,
        bg="#171d24",
    ).pack(side="left")
    Tk.Label(
        barra_superior,
        text="●  SISTEMA ACTIVO",
        font=("Consolas", 9, "bold"),
        fg=color_green,
        bg="#171d24",
    ).pack(side="right", padx=20)

    pestañas = Tk.Frame(root, bg="#11161d", height=38)
    pestañas.pack(fill="x", padx=18)
    pestañas.pack_propagate(False)
    for texto, activo in (("SISTEMA", True), ("RED", False), ("CONEXIONES", False), ("PUERTOS", False)):
        Tk.Label(
            pestañas,
            text=texto,
            font=("Consolas", 9, "bold"),
            fg=color_blue if activo else color_muted,
            bg="#11161d",
            padx=18,
            pady=10,
        ).pack(side="left")

    label = Tk.Label(
        root,
        text="ESCANER GENERAL DE MAQUINA",
        font=("Consolas", 10, "bold"),
        fg=color_muted,
        bg="#0b0f14",
        anchor="w",
    )
    label.pack(fill="x", padx=35, pady=(22, 4))
    count = 0

    contenido = Tk.Frame(root, bg="#0b0f14")
    contenido.pack(padx=25, pady=10, fill="both", expand=True)
    contenido.grid_columnconfigure(0, weight=1)
    contenido.grid_columnconfigure(1, weight=1)

    frame_Info_System = Tk.Frame(contenido, bg=color_panel, bd=1, relief="solid", highlightbackground=color_border)
    frame_Info_System.grid(
        row=0, column=0, padx=(0, 8), pady=10, sticky="nsew"
    )
    frame_Info_System.grid_columnconfigure(0, weight=0)
    frame_Info_System.grid_columnconfigure(1, weight=1)

    Tk.Label(
        frame_Info_System,
        text="[ SISTEMA / HOST ]",
        font=("Consolas", 11, "bold"),
        fg=color_blue,
        bg=color_panel,
        anchor="w",
        padx=12,
        pady=8,
    ).grid(row=0, column=0, columnspan=2, sticky="ew")

    # Agregar información del sistema
    for dato, valor in informacion_maquina.items():
        fila = count + 1
        color_fila = "#151b22" if count % 2 == 0 else "#0f141a"
        Tk.Label(
            frame_Info_System,
            text=dato,
            font=("Consolas", 9, "bold"),
            bg=color_fila,
            fg=color_muted,
            anchor="w",
            padx=12,
            pady=6,
        ).grid(row=fila, column=0, padx=1, pady=1, sticky="ew")
        Tk.Label(
            frame_Info_System,
            text=valor,
            font=("Consolas", 9, "bold"),
            bg=color_fila,
            fg=color_text,
            anchor="w",
            padx=12,
            pady=6,
        ).grid(row=fila, column=1, padx=1, pady=1, sticky="ew")
        count += 1


    # Mostrar cada dato de red en su propia columna para facilitar la lectura.
    informacion_red = Get_network_info()
    frame_Info_red = Tk.Frame(contenido, bg=color_panel, bd=1, relief="solid", highlightbackground=color_border)
    frame_Info_red.grid(
        row=0, column=1, padx=(8, 0), pady=10, sticky="nsew"
    )
    frame_Info_red.grid_columnconfigure(0, weight=0)
    frame_Info_red.grid_columnconfigure(1, weight=1)
    frame_Info_red.grid_columnconfigure(2, weight=1)

    Tk.Label(
        frame_Info_red,
        text="[ RED / INTERFACES ]",
        font=("Consolas", 11, "bold"),
        fg=color_green,
        bg=color_panel,
        anchor="w",
        padx=12,
        pady=8,
    ).grid(row=0, column=0, columnspan=3, sticky="ew")

    encabezados = ("Interfaz", "IPv4", "MAC")
    for columna, encabezado in enumerate(encabezados):
        Tk.Label(
            frame_Info_red,
            text=encabezado.upper(),
            font=("Consolas", 9, "bold"),
            fg=color_blue,
            bg="#11161d",
            anchor="w",
            padx=8,
            pady=6,
        ).grid(row=1, column=columna, padx=1, pady=1, sticky="ew")

    for fila, (interfaz, datos) in enumerate(informacion_red.items(), start=2):
        valores = (
            interfaz,
            datos.get("IPv4", "Sin IPv4"),
            datos.get("MAC", "Sin MAC"),
        )
        for columna, valor in enumerate(valores):
            Tk.Label(
                frame_Info_red,
                text=valor,
                anchor="w",
                font=("Consolas", 9, "bold" if columna == 1 else "normal"),
                fg=color_text if columna != 1 else color_green,
                bg="#151b22" if fila % 2 == 0 else "#0f141a",
                padx=8,
                pady=6,
            ).grid(row=fila, column=columna, padx=1, pady=1, sticky="ew")

    root.mainloop()
    

if __name__ == "__main__":
    main()