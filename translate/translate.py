import json
from .grayscale import grayscale


def save_ascii_art(image_path, output_file, size = (None, None)):
    """Функция преобразующая картинку в аски символы
     и сохраняющая эти символы в файл
       """
    try:
        if size[0] and size[1] != None:
            grayscale_image = grayscale(image_path, size)
        else:
            grayscale_image = grayscale(image_path)
    except FileNotFoundError:
        print(f"Error: Image {image_path} not found or cannot be opened.")
        return None
    except Exception as e:
        print(f"An error occurred while processing the image: {str(e)}")
        return None

    try:
        ascii_width, ascii_height = grayscale_image.sizeof()

        with open(output_file, "w") as f:
            with open('config/config.json', "r") as chars_file:
                ascii_chars = json.load(chars_file)

            for y in range(ascii_height):
                for x in range(ascii_width):
                    try:
                        pixel_brightness = grayscale_image.get_pixel(x, y)[0]
                        ascii_char_index = int(pixel_brightness / 255 * (len(ascii_chars) - 1))
                        f.write(ascii_chars[ascii_char_index])
                    except ValueError as ve:
                        print(f"Error processing pixel at position ({x}, {y}): {str(ve)}")
                f.write("\n")
        return output_file
    except Exception as e:
        print(f"An error occurred while saving ASCII art: {str(e)}")
        return None
