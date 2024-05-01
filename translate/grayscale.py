from PIL import Image

def grayscale(image, max_size=(512,512)):
    '''Функция, переводящая картинку в черно-белый вариант'''
    img = Image.open(image)

    img.thumbnail(max_size)

    width, height = img.size

    new_img = Image.new("RGB", (width, height))

    for i in range(width):
        for j in range(height):
            r, g, b = img.getpixel((i, j))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            new_img.putpixel((i, j), (gray, gray, gray))
    return new_img
