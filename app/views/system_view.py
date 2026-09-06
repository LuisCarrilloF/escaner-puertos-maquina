import tkinter as Tk
from services.system_info import Get_system_info
from views import styles
from views.table_view import add_table


class SystemView(Tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=styles.BACKGROUND)
        self._build()

    def _build(self):
        info = Get_system_info()
        panel = styles.panel(self)
        panel.pack(fill="both", expand=True)
        styles.title(panel, "[ SISTEMA / HOST ]", columns=2)
        rows = [(key, value) for key, value in info.items()]
        add_table(panel, ("Propiedad", "Valor"), rows, start_row=1)
