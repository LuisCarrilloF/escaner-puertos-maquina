import tkinter as Tk
from views import styles


def add_table(parent, headers, rows, highlight_column=None, start_row=1):
    for column, header in enumerate(headers):
        Tk.Label(
            parent,
            text=header.upper(),
            font=(styles.FONT, 9, "bold"),
            fg=styles.BLUE,
            bg=styles.HEADER,
            anchor="w",
            padx=8,
            pady=6,
        ).grid(row=start_row, column=column, padx=1, pady=1, sticky="ew")
        parent.grid_columnconfigure(column, weight=0 if column == 0 else 1)

    for row_number, row in enumerate(rows, start=start_row + 1):
        background = styles.PANEL if row_number % 2 == 0 else styles.PANEL_DARK
        for column, value in enumerate(row):
            Tk.Label(
                parent,
                text=str(value),
                font=(styles.FONT, 9, "bold" if column == highlight_column else "normal"),
                fg=styles.GREEN if column == highlight_column else styles.TEXT,
                bg=background,
                anchor="w",
                padx=8,
                pady=6,
            ).grid(row=row_number, column=column, padx=1, pady=1, sticky="ew")
