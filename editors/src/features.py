import json
import random

from editors.config import TEXTS

def set_coordinates(max_x, max_y, min_weight=0, min_height=0, coordinates = None):
    if coordinates is None:
        coordinates = (random.randint(min_height, max_x), random.randint(min_weight, max_y))
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
        with open(TEXTS, 'r') as file:
            data = json.load(file)
        text = random.choice(data)
    return text