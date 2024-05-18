import tkinter as tk

class ASCIIArtViewer:
    """Класс, отвечающий за создание окна для аски изображения """
    def __init__(self, root, ascii_file):
        self.root = root
        self.root.title("ASCII Art Viewer")
        self.root.configure(bg="black")

        self.ascii_art = self.load_ascii_art(ascii_file)
        self.font_size = 1  

        self.ascii_label = tk.Label(self.root, text=self.ascii_art, font=("Courier", self.font_size), bg="black", fg="white")
        self.ascii_label.pack(expand=True)

        self.root.bind("<plus>", self.zoom_in)
        self.root.bind("<minus>", self.zoom_out)

    """метод для загрузки файла"""
    def load_ascii_art(self, ascii_file):
        """Function to read ASCII art from a file."""
        with open(ascii_file, "r") as f:
            return f.read()
    """метод для увеличения маштаба"""
    def zoom_in(self, event):
        """Increase the font size."""
        self.font_size += 1
        self.ascii_label.config(font=("Courier", self.font_size))
    """метод для уменьшения маштаба"""
    def zoom_out(self, event):
        """Decrease the font size."""
        self.font_size -= 1
        self.ascii_label.config(font=("Courier", self.font_size))

"""функция, которая создает объект окна"""
def display_ascii_in_window(ascii_file):
    """Function to create the window."""
    root = tk.Tk()
    app = ASCIIArtViewer(root, ascii_file)
    root.mainloop()
