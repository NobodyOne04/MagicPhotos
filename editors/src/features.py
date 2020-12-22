import random

def set_coordinates(max_x, max_y, coordinates = None):
    if coordinates is None:
        coordinates = (random.randint(0, max_x), random.randint(0, max_y))
    return coordinates

def set_color(color = None):
    if color is None:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def set_size(size = None):
    if size is None:
        size = random.randint(0, 500)
    return size

def set_text(text = None):
    if text is None:
        # TODO сделать вывод рандомной фразы из заготвленного списка
        text = 'Test'
    return text