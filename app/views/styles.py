BACKGROUND = "#0b0f14"
PANEL = "#151b22"
PANEL_DARK = "#0f141a"
HEADER = "#11161d"
BORDER = "#303944"
TEXT = "#c7d2e0"
MUTED = "#8393a8"
BLUE = "#3da5ff"
GREEN = "#42d36f"
AMBER = "#f2bd4b"
RED = "#ff6b6b"
FONT = "Consolas"


def panel(parent):
    import tkinter as Tk
    return Tk.Frame(parent, bg=PANEL, bd=1, relief="solid", highlightbackground=BORDER)


def title(parent, text, color=BLUE, columns=1):
    import tkinter as Tk
    label = Tk.Label(
        parent,
        text=text,
        font=(FONT, 11, "bold"),
        fg=color,
        bg=PANEL,
        anchor="w",
        padx=12,
        pady=8,
    )
    label.grid(row=0, column=0, columnspan=columns, sticky="ew")
    return label
