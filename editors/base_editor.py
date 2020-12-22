import os
import random

from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)

from editors.src.features import (
    set_coordinates,
    set_color,
    set_text,
)
from editors.figures_editor import FiguresEditor

class Editor:
    def __init__(self):
        self.__image = None

    def get_image(self):
        return self.__image

    def set_image(self, path_to_image):
        self.__image = Image.open(path_to_image)

    def rotate(self, angle=None):
        if angle is None:
            angle = random.randint(0, 360)
        self.__image = self.__image.rotate(angle)

    def add_text(self, coordinates=None, text=None, color=None, font=None, font_size=None):
        # TODO разобраться какие брать максимальные границы, пока 500х500
        height, width = self.__image.size
        coordinates = set_coordinates(500, 500, coordinates)
        text = set_text(text)
        color = set_color(color)

        if font is None:
            # TODO выбрать рандомный шрифт
            if font_size is None:
                font_size = random.randint(0, 400)

            font_name = random.choice(os.listdir('editors/sources/fonts'))
            font = ImageFont.truetype(f'editors/sources/fonts/{font_name}', font_size)

        ImageDraw.Draw(self.__image).text(coordinates, text, color, font)

    def add_figures(self, figures):
        self.__image = FiguresEditor.add_figures(self.__image, figures)