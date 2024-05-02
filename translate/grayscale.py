from .image_handler import Image
from PIL import Image as GrayImage

def grayscale(image_path):
    '''Функция, переводящая картинку в черно-белый вариант'''
    img = Image(image_path)

    width, height = img.sizeof()

    new_img = GrayImage.new("RGB", (width, height))  # Создаем новый экземпляр вашего класса Image без указания пути к файлу

    for i in range(width):
        for j in range(height):
            r, g, b = img.get_pixel(i, j)
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            new_img.putpixel((i, j), (gray, gray, gray))

    return new_img