import tkinter as Tk

from views.app_view import AppView


def main():
    root = Tk.Tk()
    AppView(root)
    root.mainloop()


if __name__ == "__main__":
    main()