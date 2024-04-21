import tkinter as tk

def display_ascii_art(ascii_file):
    # Открываем файл с ASCII-графикой для чтения
    with open(ascii_file, "r") as f:
        # Считываем ASCII-графику из файла
        ascii_art = f.read()
    return ascii_art

def display_ascii_in_window(ascii_file):
    # Создаем окно
    root = tk.Tk()
    root.title("ASCII Art Viewer")
    root.configure(bg="black")  # Устанавливаем черный фон окна

    # Создаем метку для отображения ASCII-графики с меньшим размером шрифта
    ascii_label = tk.Label(root, text=display_ascii_art(ascii_file), font=("Courier", 1), bg="white", fg="black")
    ascii_label.pack()

    # Запускаем главный цикл обработки событий
    root.mainloop()