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
        return self._image.width

    @property
    def height(self):
        return self._image.height

    def sizeof(self):
        return self.width, self.height

    def get_pixel(self, x, y):
        return self._image.getpixel((x, y))

    def put_pixel(self, x, y, color):
        self._image.putpixel((x, y), color)

    def set_size(self, size):
        self._image = self._image.resize(size)

    @classmethod
    def open(cls, file_path):
        return cls(file_path)
