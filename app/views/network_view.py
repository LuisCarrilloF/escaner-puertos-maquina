import tkinter as Tk
from services.network_info import Get_network_info
from views import styles
from views.table_view import add_table


class NetworkView(Tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=styles.BACKGROUND)
        self._build()

    def _build(self):
        panel = styles.panel(self)
        panel.pack(fill="both", expand=True)
        styles.title(panel, "[ RED / INTERFACES ]", styles.GREEN, columns=3)
        rows = []
        for interface, data in Get_network_info().items():
            rows.append((interface, data.get("IPv4", "Sin IPv4"), data.get("MAC", "Sin MAC")))
        add_table(panel, ("Interfaz", "IPv4", "MAC"), rows, highlight_column=1, start_row=1)
