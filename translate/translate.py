import json
from .grayscale import grayscale


def save_ascii_art(image_path, output_file):
    try:
        # Преобразование изображения в оттенки серого
        grayscale_image = grayscale(image_path)
    except FileNotFoundError:
        print(f"Error: Image {image_path} not found or cannot be opened.")
        return None
    except Exception as e:
        print(f"An error occurred while processing the image: {str(e)}")
        return None

    try:
        # Определение размеров ASCII-графики в символах
        ascii_width, ascii_height = grayscale_image.sizeof()

        # Открываем файл для записи ASCII-графики
        with open(output_file, "w") as f:
            # Загружаем ASCII символы из файла
            with open('config/config.json', "r") as chars_file:
                ascii_chars = json.load(chars_file)

            # Проходим по каждому пикселю изображения и преобразуем его в символ ASCII
            for y in range(ascii_height):
                for x in range(ascii_width):
                    try:
                        pixel_brightness = grayscale_image.get_pixel(x, y)[0]
                        # Вычисляем индекс символа ASCII на основе яркости пикселя
                        ascii_char_index = int(pixel_brightness / 255 * (len(ascii_chars) - 1))
                        f.write(ascii_chars[ascii_char_index])
                    except ValueError as ve:
                        print(f"Error processing pixel at position ({x}, {y}): {str(ve)}")
                f.write("\n")
        return output_file
    except Exception as e:
        print(f"An error occurred while saving ASCII art: {str(e)}")
        return None
