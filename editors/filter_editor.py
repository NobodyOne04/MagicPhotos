from PIL import Image

class FilterEditor:
    filter_dict = {
        'black_and_white': 'make_black_and_white',
        'sepia': 'make_sepia',
        'bright': 'make_bright'
    }

    @staticmethod
    def add_filter(image, user_filter):
    # TODO Проверка на тот случай, если передавать словарь с настройками для цвета, но это в будущем
        return getattr(FilterEditor, FilterEditor.filter_dict[user_filter])(image)

    @staticmethod
    def make_black_and_white(image):
        result = Image.new('RGB', image.size)
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                r, g, b = image.getpixel((x, y))
                gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
                result.putpixel((x, y), (gray, gray, gray))
        return result

    @staticmethod
    def make_sepia(image):
        result = Image.new('RGB', image.size)
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                r, g, b = image.getpixel((x, y))
                red = int(r * 0.393 + g * 0.769 + b * 0.189)
                green = int(r * 0.349 + g * 0.686 + b * 0.168)
                blue = int(r * 0.272 + g * 0.534 + b * 0.131)
                result.putpixel((x, y), (red, green, blue))
        return result

    @staticmethod
    def make_bright(image):
        brightness = 2
        result = Image.new('RGB', image.size)
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                r, g, b = image.getpixel((x, y))

                red = int(r * brightness)
                red = min(255, max(0, red))

                green = int(g * brightness)
                green = min(255, max(0, green))

                blue = int(b * brightness)
                blue = min(255, max(0, blue))

                result.putpixel((x, y), (red, green, blue))
        return result
