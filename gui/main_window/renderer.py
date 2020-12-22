# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
import json

from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets
)

from gui.main_window.handlers import Handler


class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.__handler = Handler(self)
        with open('./gui/main_window/combo_boxes/filter.json') as file:
            self.__filter_data = json.load(file)
        with open('./gui/main_window/combo_boxes/figure.json') as file:
            self.__figure_data = json.load(file)
        with open('./gui/main_window/combo_boxes/frame.json') as file:
            self.__frame_data = json.load(file)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 771)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 20, 221, 751))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(201, 125, 125);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(15)
        self.frame.setObjectName("frame")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 201, 31))

        self.pushButton.clicked.connect(self.__handler.read_image)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)

        self.pushButton.setPalette(palette)
        self.pushButton.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                      "border-radius: 0px")
        self.pushButton.setObjectName("pushButton")

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 110, 201, 31))

        for item in self.__filter_data:
            self.comboBox.addItem(item)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.comboBox.setPalette(palette)
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "QComboBox::drop-arrrow\n"
                                    "{\n"
                                    "border : 2px solid green;\n"
                                    "content: \">\"\n"
                                    "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 150, 201, 31))
        self.comboBox_2.setStyleSheet("QComboBox {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QComboBox::drop-arrrow\n"
                                      "{\n"
                                      "border : 2px solid green;\n"
                                      "}")
        self.comboBox_2.setObjectName("comboBox_2")

        for item in self.__frame_data:
            self.comboBox_2.addItem(item)

        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 190, 201, 31))
        self.comboBox_3.setStyleSheet("QComboBox {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QComboBox::drop-arrrow\n"
                                      "{\n"
                                      "border : 2px solid green;\n"
                                      "}")
        self.comboBox_3.setObjectName("comboBox_3")

        for item in self.__figure_data:
            self.comboBox_3.addItem(item)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 300, 201, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 0px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.__handler.text)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 340, 201, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 0px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 450, 201, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 0px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.__handler.generate)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 670, 201, 31))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 0px")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.__handler.clear_image)

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 710, 201, 31))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 0px")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.__handler.save_image)

        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 380, 201, 31))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 0px")
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, -10, 941, 31))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 10, 31, 20))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border: none;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(860, 10, 21, 16))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border: none;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(890, 10, 31, 16))
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border: none;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(sys.exit)

        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(230, 30, 701, 731))
        self.image.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setObjectName("image")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Magic Photo"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать фото"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить текст"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить фигуру"))
        self.pushButton_4.setText(_translate("MainWindow", "Сгенерировать"))
        self.pushButton_5.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_6.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_8.setText(_translate("MainWindow", "Добавить календарь"))
        self.pushButton_7.setText(_translate("MainWindow", "↺"))
        self.pushButton_9.setText(_translate("MainWindow", "-"))
        self.pushButton_10.setText(_translate("MainWindow", "Х"))
