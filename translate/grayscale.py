from translate.image_handler import Image

def grayscale(image_path, size=(None, None)):
    '''Функция для преобразования изображения в оттенки серого'''
    img = Image(image_path)
    
    if size[0] and size[1] is not None:
        img.set_size((int(size[0]), int(size[1])))
        width, height = img.sizeof()
        new_img = Image.open(image_path)  # Создаем новое изображение с исходным размером
        new_img.set_size((int(size[0]), int(size[1])))
    else:
        width, height = img.sizeof()
        new_img = Image.open(image_path)
        
    for i in range(width):
        for j in range(height):
            r, g, b = img.get_pixel(i, j)
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            new_img.put_pixel(i, j, (gray, gray, gray))

    return new_img
