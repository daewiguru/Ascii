from PIL import Image as hanler
class Image(hanler):
    def __init__(self, file_path) -> None:
        try:
            self._image = hanler.open(file_path)
        except IOError:
            raise FileNotFoundError(f"Image {file_path} not found or cannot be opened")
        
    def __sizeof__(self):
        return self._image.size
    def get_pixel(self):
        return self._image.getpixel