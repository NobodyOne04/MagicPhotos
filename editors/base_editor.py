import os
import json
import random

import cv2
from numpy import asarray
from PIL import (
    Image,
    ImageFont,
    ImageDraw,
)
from editors.config import (
    CALENDAR,
    FONT_PATH,
    FRAME_PATH,
)
from editors.src.features import (
    set_coordinates,
    set_color,
    set_text,
)
from editors.figures_editor import FiguresEditor

class Editor:
    def __init__(self):
        self.__is_calendar = False
        self.__is_framed = False
        self.__is_filtered = False
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
        text = set_text(text)
        color = set_color(color)

        if font_size is None:
            font_size = random.randint(15, 40)

        if font is None:
            font_name = random.choice(os.listdir(FONT_PATH))
            font = ImageFont.truetype(os.path.join(FONT_PATH, font_name), font_size)

        font_height, font_weight = font.getsize(text)
        coordinates = set_coordinates(
            abs(height - font_height),
            width,
        )
        print(coordinates)

        ImageDraw.Draw(self.__image).text(coordinates, text, color, font)

    def append_calendar(self):
        if self.__is_calendar:
            return

        calendar = Image.open(CALENDAR)
        calendar.thumbnail(self.__image.size)
        self.__image.paste(calendar, (0, 0), calendar)
        self.__is_calendar = True


    def add_figures(self, figures):
        self.__image = FiguresEditor.add_figures(self.__image, figures)

    def add_frame(self, frame_number):
        if self.__is_framed:
            return

        with open(FRAME_PATH, 'r') as file:
            frames_const = json.load(file)
        frames_const = frames_const[frame_number]
        image = cv2.copyMakeBorder(
            asarray(self.__image),
            frames_const['top_border_weight'],
            frames_const['bottom_border_weight'],
            frames_const['left_border_weight'],
            frames_const['right_border_weight'],
            cv2.BORDER_CONSTANT,
            value=frames_const['colour']
        )
        self.__is_framed = True
        self.__image = Image.fromarray(image)