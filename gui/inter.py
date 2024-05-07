import tkinter as tk


"""Модуль отображающий файл с аски артом в оконное приложение"""
def display_ascii_art(ascii_file):
    """Функция считывающая аски арт"""
    with open(ascii_file, "r") as f:
        ascii_art = f.read()
    return ascii_art

def display_ascii_in_window(ascii_file):
    """Функция, отвечающая за создание окна"""
    root = tk.Tk()
    root.title("ASCII Art Viewer")
    root.configure(bg="black") 

    ascii_label = tk.Label(root, text=display_ascii_art(ascii_file), font=("Courier", 1), bg="black", fg="white")
    ascii_label.pack()

    root.mainloop()