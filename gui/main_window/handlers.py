from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog
from PIL import ImageQt, Image


class LoadFileButtonHandler:

    def __init__(self, instance):
        self.__window_instance = instance
        self.__image = None

    def read_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path, _ = QFileDialog.getOpenFileName(filter='All files (*.jpg *.png);;JPEG (*.jpg *.jpeg)')

        #TODO: Call Marat Class with arg path return pil.Image

        image = Image.open(path)

        qt_image = ImageQt.ImageQt(image)

        pixmap = QtGui.QPixmap.fromImage(qt_image)
        pixmap = pixmap.scaled(701, 731)

        self.__window_instance.image.setPixmap(pixmap)

    def save_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        name, _ = QFileDialog.getSaveFileName()

        # TODO: Call Marat Class with arg path return None

    def clear_image(self):
        self.__window_instance.image.clear()


