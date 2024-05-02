from .image_handler import Image

def grayscale(image_path):
    '''Функция для преобразования изображения в оттенки серого'''
    img = Image(image_path)

    width, height = img.sizeof()

    new_img = Image(image_path)

    for i in range(width):
        for j in range(height):
            r, g, b = img.get_pixel(i, j)
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            new_img.put_pixel(i, j, (gray, gray, gray))

    return new_img
