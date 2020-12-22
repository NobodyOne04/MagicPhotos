from PIL import Image

import cv2
from numpy import asarray

from editors.src.features import (
    set_color,
    set_size,
    set_coordinates,
)

class FiguresEditor:
    figures_dict = {
        'circle': 'add_circles',
        'rombus': 'add_rombuses',
        'heart': 'add_hearts',
        'star': 'add_stars'
    }

    @staticmethod
    def add_figures(image, user_figure_dict):
        for user_figure_name, user_figure_options_dict in user_figure_dict.items():
            image = getattr(
                FiguresEditor,
                FiguresEditor.figures_dict[user_figure_name]
            )(image, user_figure_options_dict)

        return image

    @staticmethod
    def add_circles(image, user_figure_options_dict):
        data = asarray(image)
        for user_figure_option in user_figure_options_dict:
            coordinates = set_coordinates(500, 500)
            size = set_size(user_figure_option['size'])
            color = set_color(user_figure_option['color'])

            cv2.circle(data, coordinates, size, color, 10)
        image = Image.fromarray(data)

        return image