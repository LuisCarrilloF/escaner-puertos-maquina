import tkinter as Tk
from views import styles
from views.connections_view import ConnectionsView
from views.network_view import NetworkView
from views.ports_view import PortsView
from views.system_view import SystemView


class AppView:
    def __init__(self, root):
        self.root = root
        self.views = {}
        self.tabs = {}
        self.current_tab = "SISTEMA"
        self._build_shell()
        self._build_views()
        self.show_view(self.current_tab)

    def _build_shell(self):
        self.root.title("LCarrillo.Dev - Escaner de diagnostico")
        self.root.geometry("1200x740")
        self.root.minsize(900, 600)
        self.root.configure(bg=styles.BACKGROUND)

        header = Tk.Frame(self.root, bg="#171d24", height=64)
        header.pack(fill="x", padx=18, pady=(16, 0))
        header.pack_propagate(False)
        Tk.Label(header, text="[ LCarrillo.Dev ]", font=(styles.FONT, 15, "bold"), fg=styles.BLUE, bg="#171d24").pack(side="left", padx=(20, 14))
        Tk.Label(header, text="Escaner de diagnostico del sistema", font=(styles.FONT, 10), fg=styles.MUTED, bg="#171d24").pack(side="left")
        Tk.Label(header, text="●  SISTEMA ACTIVO", font=(styles.FONT, 9, "bold"), fg=styles.GREEN, bg="#171d24").pack(side="right", padx=20)

        tabs_bar = Tk.Frame(self.root, bg=styles.HEADER, height=38)
        tabs_bar.pack(fill="x", padx=18)
        tabs_bar.pack_propagate(False)
        for tab_name in ("SISTEMA", "RED", "CONEXIONES", "PUERTOS"):
            button = Tk.Button(
                tabs_bar,
                text=tab_name,
                command=lambda name=tab_name: self.show_view(name),
                font=(styles.FONT, 9, "bold"),
                fg=styles.MUTED,
                bg=styles.HEADER,
                activeforeground=styles.BLUE,
                activebackground=styles.HEADER,
                relief="flat",
                bd=0,
                padx=18,
                pady=9,
                cursor="hand2",
            )
            button.pack(side="left")
            self.tabs[tab_name] = button

        Tk.Label(
            self.root,
            text="ESCANER GENERAL DE MAQUINA",
            font=(styles.FONT, 10, "bold"),
            fg=styles.MUTED,
            bg=styles.BACKGROUND,
            anchor="w",
        ).pack(fill="x", padx=35, pady=(22, 4))

        self.content = Tk.Frame(self.root, bg=styles.BACKGROUND)
        self.content.pack(padx=25, pady=10, fill="both", expand=True)

    def _build_views(self):
        self.views = {
            "SISTEMA": SystemView(self.content),
            "RED": NetworkView(self.content),
            "CONEXIONES": ConnectionsView(self.content),
            "PUERTOS": PortsView(self.content),
        }

    def show_view(self, tab_name):
        for view in self.views.values():
            view.pack_forget()
        self.views[tab_name].pack(fill="both", expand=True)
        for name, button in self.tabs.items():
            button.configure(fg=styles.BLUE if name == tab_name else styles.MUTED)
        self.current_tab = tab_name
