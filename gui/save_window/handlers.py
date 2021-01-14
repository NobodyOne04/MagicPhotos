from PyQt5.QtWidgets import QFileDialog

from editors.base_editor import Editor


class Handler:
    def __init__(self, window):
        self.__window_instance = window
        self.__editor = Editor()

    def save_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        name, _ = QFileDialog.getSaveFileName()

        image = self.__editor.get_image()
        image = image.convert('RGB')

        if image is None:
            return

        selected = self.__window_instance.comboBox.currentText()
        weight, hight = selected.split('x')
        weight, hight = int(weight), int(hight)

        image = image.resize((weight, hight))

        self.__window_instance.obj.close()

        image.save(name)
