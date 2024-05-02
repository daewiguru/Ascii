import json
from .grayscale import grayscale

def save_ascii_art(image_path, output_file):
    # Преобразование изображения в оттенки серого
    grayscale_image = grayscale(image_path)
    # Определение размеров ASCII-графики в символах
    ascii_width = grayscale_image.width
    ascii_height = grayscale_image.height
    # Масштабируем изображение с новыми размерами
        
    # Открываем файл для записи ASCII-графики
    with open(output_file, "w") as f:
        # Загружаем ASCII символы из файла
        with open('config/config.json', "r") as chars_file:
            ascii_chars = json.load(chars_file)

        # Проходим по каждому пикселю изображения и преобразуем его в символ ASCII
        for y in range(ascii_height):
            for x in range(ascii_width):
                pixel_brightness = grayscale_image.get_pixel(x, y)[0]
                # Вычисляем индекс символа ASCII на основе яркости пикселя
                ascii_char_index = int(pixel_brightness / 255 * (len(ascii_chars) - 1))
                f.write(ascii_chars[ascii_char_index])
            f.write("\n")
    return output_file