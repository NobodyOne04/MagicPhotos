import json
import random

from PIL import ImageQt

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QFileDialog,
    QMainWindow
)

from src.decorators import singleton
from editors.base_editor import Editor


@singleton
class Handler:

    def __init__(self, instance):
        self.__window_instance = instance
        self.__editor = Editor()
        self.__is_calendar = False
        self.__is_framed = False
        self.__is_filtered = False
        with open('./editors/sources/backgrounds.json', 'r') as file:
            self.__colours = json.load(file)
        with open('./gui/figure_window/combo_boxes/figure.json') as file:
            self.__figure_data = json.load(file)

    def set_image(self):
        image = self.__editor.get_image()

        qt_image = ImageQt.ImageQt(image)

        pixmap = QtGui.QPixmap.fromImage(qt_image)
        pixmap = pixmap.scaled(701, 731)

        self.__window_instance.image.setPixmap(pixmap)

    def read_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path, _ = QFileDialog.getOpenFileName(filter='All files (*.jpg *.png);;JPEG (*.jpg *.jpeg)')

        self.__editor.set_image(path)
        self.set_image()

    def open_window(self, obj):
        window_obj = QMainWindow(parent=self.__window_instance.obj)
        window = obj(self)
        window.setupUi(window_obj)
        window_obj.show()

    def clear_image(self):
        self.__is_calendar = False
        self.__is_framed = False
        self.__is_filtered = False
        self.__window_instance.image.clear()
        self.__editor.set_background_colour('белый')

    def add_figure(self):
        figures_dict = {
            'circle': [
                {
                    'color': None,
                    'size': None,
                    'coordinates': None
                },
                {
                    'color': None,
                    'size': None,
                    'coordinates': None
                }
            ],

        }
        self.__editor.add_figures(figures_dict)
        self.set_image()

    def add_filter(self):
        filter = self.__window_instance.comboBox.currentText()
        if not self.__is_filtered:
            self.__editor.add_filter(filter)
            self.set_image()
            self.__is_filtered = True

    def add_frame(self):
        frame = self.__window_instance.comboBox_2.currentText()
        if not self.__is_framed:
            self.__editor.add_frame(frame)
            self.set_image()
            self.__is_framed = True

    def add_background(self):
        background = self.__window_instance.comboBox_3.currentText()
        self.__editor.set_background_colour(background)
        self.set_image()

    def generate(self):
        filter = random.choice(self.__window_instance.filter_data)
        frame = random.choice(self.__window_instance.frame_data)
        background = random.choice(self.__window_instance.bg_data)

        if not self.__is_filtered:
            self.__editor.add_filter(filter)
            self.__is_filtered = True

        if not self.__is_framed:
            self.__editor.add_frame(frame)
            self.__is_framed = True

        self.__editor.add_text()

        figure_dict = dict()
        for figure in self.__figure_data:
            figures_list = list()
            for _ in range(random.randint(1, 10)):
                figures_list.append(
                    {
                        'color': tuple(random.choice(list(self.__colours.values()))),
                        'size': random.randint(10, 20),
                        'coordinates': None
                    }
                )
            figure_dict[figure] = figures_list

        self.__editor.add_figures(figure_dict)

        self.__editor.set_background_colour(background)
        self.set_image()

    def append_calendar(self):
        if not self.__is_calendar:
            return
        self.__editor.append_calendar()
        self.set_image()
        self.__is_calendar = True
