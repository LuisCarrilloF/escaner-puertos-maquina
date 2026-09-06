import tkinter as Tk
from services.port_scaner import get_listening_ports
from views import styles
from views.table_view import add_table


class PortsView(Tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=styles.BACKGROUND)
        self._build()

    def _build(self):
        panel = styles.panel(self)
        panel.pack(fill="both", expand=True)
        styles.title(panel, "[ PUERTOS ESCUCHANDO ]", styles.RED, columns=3)
        rows = get_listening_ports() or [("-", "-", "No hay puertos escuchando")]
        add_table(panel, ("Protocolo", "Dirección", "Proceso"), rows, start_row=1)
