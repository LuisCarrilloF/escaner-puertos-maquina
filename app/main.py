import tkinter as Tk
from services.system_info import Get_system_info
from services.network_info import Get_network_info
def main():
    informacion_maquina = Get_system_info()
    root = Tk.Tk()
    root.title("Escaner de General de maquina")
    root.geometry("750x600")
    label = Tk.Label(root, text="Bienbenido al escaner de maquina", font=("Arial", 16))
    label.pack(pady=30)
    count = 0
    frame_Info_System = Tk.Frame(root)
    frame_Info_System.pack(pady=20)

    # Agregar información del sistema
    for dato, valor in informacion_maquina.items():
        Datos = Tk.Label
        Datos(frame_Info_System,text=dato, font=("Arial", 10, "bold")).grid(row=count, column=0, padx=10, pady=5, sticky="w")
        Datos(frame_Info_System,text =valor).grid(row=count, column=1, padx=10, pady=5, sticky="w")
        count += 1

    # Agregar información de red
    informacion_red = Get_network_info()
    frame_Info_red = Tk.Frame(root)
    frame_Info_red.pack(pady=20)
    for dato, valor in informacion_red.items():
        Redes = Tk.Label
        Redes(frame_Info_red,text=dato, font=("Arial", 10, "bold")).grid(row=count, column=0, padx=10, pady=5, sticky="w")
        Redes(frame_Info_red,text =valor).grid(row=count, column=1, padx=10, pady=5, sticky="w")
        count += 1

    root.mainloop()
    

if __name__ == "__main__":
    main()