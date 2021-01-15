import os
import json
import random

import cv2
from numpy import asarray
from PIL import (
    Image,
    ImageFont,
    ImageStat,
    ImageDraw,
    ImageOps,
)
from editors.config import (
    CALENDAR,
    FONT_PATH,
    FRAME_PATH,
    BACKGROUNDS,
)
from editors.src.features import (
    set_coordinates,
    set_color,
    set_text,
)
from editors.figures_editor import FiguresEditor
from editors.filter_editor import FilterEditor
from src.decorators import singleton


@singleton
class Editor:
    def __init__(self):
        self.__image = None
        self.background_colour = (255, 255, 255, 255)

    def set_background_colour(self, colour):
        with open(BACKGROUNDS, 'r') as file:
            bg = json.load(file)
        self.background_colour = tuple(bg[colour])

    def set_background(self, image=None):
        if not image:
            image = self.__image

        background = Image.new('RGBA', (701, 731), self.background_colour)

        bg_w, bg_h = background.size
        image.thumbnail((bg_w, bg_h))
        width, height = self.__image.size

        offset = ((bg_w - width) // 2, (bg_h - height) // 2)

        background.paste(image, offset)
        return background

    def get_image(self):
        return self.set_background()

    def set_image(self, path_to_image, image=None):
        if image:
            self.__image = image
            return
        self.__image = Image.open(path_to_image)

    def rotate(self, angle=None):
        if angle is None:
            angle = random.randint(0, 360)
        self.__image = self.__image.rotate(angle)

    def add_text(self, text=None, color=None, font=None, font_size=None):
        height, width = self.__image.size
        text = set_text(text)
        color = set_color(color)

        if font_size is None:
            font_size = random.randint(15, 40)

        if font is None:
            font = random.choice(os.listdir(FONT_PATH))
        else:
            font = f'{font}.ttf'

        font = ImageFont.truetype(os.path.join(FONT_PATH, font), font_size)

        font_height, font_weight = font.getsize(text)
        coordinates = set_coordinates(
            abs(height - font_height),
            width,
        )

        ImageDraw.Draw(self.__image).text(coordinates, text, color, font)

    def add_filter(self, filter):
        self.__image = FilterEditor.add_filter(self.__image, filter)

    def add_figures(self, figures):
        self.__image = FiguresEditor.add_figures(self.__image, figures)

    def add_frame(self, frame_number):
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
        return Image.fromarray(image).resize(self.__image.size)

    def brightness(self, image):
        im = image.convert('L')
        stat = ImageStat.Stat(im)
        return stat.rms[0]

    # side - бывает top или bottom
    # month_png -
    def append_calendar(self, side, month_image_path, image=None):
        if not image:
            image = self.__image

        background = Image.new('RGBA', (701, 731), self.background_colour)

        bg_w, bg_h = background.size
        image.thumbnail((bg_w, bg_h))
        width, height = image.size

        offset = ((bg_w - width) // 2, (bg_h - height) // 2)

        background.paste(image, offset)

        month_image = Image.open(month_image_path, 'r').convert("RGBA")
        month_image_w, month_image_h = month_image.size
        width, height = image.size
        bg_w, bg_h = background.size
        offset_w = (bg_w - width) // 2
        offset_h = (bg_h - height) // 2

        if self.brightness(background) < 100:
            r, g, b, a = month_image.split()
            rgb_month_image = Image.merge('RGB', (r, g, b))
            month_image_inverted = ImageOps.invert(rgb_month_image)
            r2, g2, b2 = month_image_inverted.split()
            month_image = Image.merge('RGBA', (r2, g2, b2, a))
        if side == 'top':
            background.paste(month_image, ((bg_w - month_image_w) // 2, (offset_h - month_image_h) // 2),
                             mask=month_image)
        else:
            background.paste(month_image,
                             ((bg_w - month_image_w) // 2, (offset_h + height) + ((offset_h - month_image_h) // 2)),
                             mask=month_image)

        return background

