import json

from PIL import ImageQt

from PyQt5 import QtGui

from editors.base_editor import Editor


class Handler:
    def __init__(self, window):
        self.__editor = Editor()
        self.__window_instance = window
        with open('./editors/sources/backgrounds.json', 'r') as file:
            self.__colours = json.load(file)

    def __set_image(self):
        image = self.__editor.get_image()

        qt_image = ImageQt.ImageQt(image)

        pixmap = QtGui.QPixmap.fromImage(qt_image)
        pixmap = pixmap.scaled(701, 731)

        self.__window_instance.obj.image.setPixmap(pixmap)

    def add_figure(self):
        figure = self.__window_instance.comboBox.currentText()
        angle = int(self.__window_instance.lineEdit_2.text())
        colour = tuple(self.__colours[self.__window_instance.comboBox_3.currentText()])
        size = int(self.__window_instance.comboBox_4.currentText())

        figures_dict = {
            figure: [
                {
                    'color': colour,
                    'size': size,
                    'coordinates': None
                }
            ]
        }
        self.__editor.add_figures(figures_dict)
        self.__window_instance.super_handler.set_image()
