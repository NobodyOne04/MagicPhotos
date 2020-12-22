from PIL import (
    ImageQt,
    Image,
)

from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog

from editors.base_editor import Editor


class Handler:

    def __init__(self, instance):
        self.__window_instance = instance
        self.__editor = Editor()
        self.__is_calendar = False
        self.__is_framed = False
        self.__is_filtered = False

    def __set_image(self):
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
        self.__set_image()

    def save_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        name, _ = QFileDialog.getSaveFileName()

        image = self.__editor.get_image()

        if image is None:
            return

        image.save(name)

    def clear_image(self):
        self.__is_calendar = False
        self.__is_framed = False
        self.__is_filtered = False
        self.__window_instance.image.clear()

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
        self.__set_image()

    def generate(self):
        filter = self.__window_instance.comboBox.currentText()
        frame = self.__window_instance.comboBox_2.currentText()
        background = self.__window_instance.comboBox_3.currentText()

        if not self.__is_filtered:
            self.__editor.add_filter(filter)
            self.__set_image()
            self.__is_filtered = True

        if not self.__is_framed:
            self.__editor.add_frame(frame)
            self.__set_image()
            self.__is_framed = True

    def append_calendar(self):
        if not self.__is_calendar:
            return
        self.__editor.append_calendar()
        self.__set_image()
        self.__is_calendar = True

    def text(self):
        self.__editor.add_text()
        self.__set_image()


