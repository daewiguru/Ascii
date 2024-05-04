from PIL import Image as PILImage

class Image():
    def __init__(self, file_path, default_size=(512, 512)):
        try:
            self._image = PILImage.open(file_path)
        except IOError:
            raise FileNotFoundError(f"Image {file_path} not found or cannot be opened")

        self._default_size = default_size

    @property
    def width(self):
        try:
            return self._image.width
        except AttributeError:
            raise ValueError("Image is not loaded or is corrupted")

    @property
    def height(self):
        try:
            return self._image.height
        except AttributeError:
            raise ValueError("Image is not loaded or is corrupted")

    def sizeof(self):
        try:
            return self.width, self.height
        except ValueError:
            raise ValueError("Image is not loaded or is corrupted")

    def get_pixel(self, x, y):
        try:
            return self._image.getpixel((x, y))
        except AttributeError:
            raise ValueError("Image is not loaded or is corrupted")
        except IndexError:
            raise ValueError("Pixel coordinates are out of range")

    def put_pixel(self, x, y, color):
        try:
            self._image.putpixel((x, y), color)
        except AttributeError:
            raise ValueError("Image is not loaded or is corrupted")
        except IndexError:
            raise ValueError("Pixel coordinates are out of range")
        except ValueError:
            raise ValueError("Invalid color value")

    def set_size(self, size):
        try:
            self._image = self._image.resize(size)
        except AttributeError:
            raise ValueError("Image is not loaded or is corrupted")
        except ValueError:
            raise ValueError("Invalid size provided")

    @classmethod
    def open(cls, file_path):
        return cls(file_path)
