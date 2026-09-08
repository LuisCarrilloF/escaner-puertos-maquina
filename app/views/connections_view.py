import tkinter as Tk
from services.connections import get_connections
from views import styles
from views.table_view import add_table


class ConnectionsView(Tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=styles.BACKGROUND)
        self._build()

    def _build(self):
        panel = styles.panel(self)
        panel.pack(fill="both", expand=True)
        styles.title(panel, "[ CONEXIONES ACTIVAS ]", styles.AMBER, columns=5)
        rows = get_connections(collapse_loopback=True) or [("-", "-", "desconocido", "Sin conexiones", "-")]
        add_table(panel, ("Estado", "PID", "Proceso", "Local", "Remota"), rows, start_row=1)
