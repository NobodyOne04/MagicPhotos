# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import json

from PyQt5 import QtCore, QtGui, QtWidgets

from gui.text_window.handlers import Handler


class Ui_MainWindow(object):
    def __init__(self, super_handler):
        self.super_handler = super_handler
        self.__handler = Handler(self)
        with open('./gui/figure_window/combo_boxes/size.json') as file:
            self.__size_data = json.load(file)
        with open('./gui/text_window/combo_boxes/font.json') as file:
            self.__font_data = json.load(file)
        with open('./editors/sources/backgrounds.json', 'r') as file:
            self.__colours = json.load(file)

    def setupUi(self, MainWindow):
        self.obj = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 288)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 20, 361, 271))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(201, 125, 125);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(15)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(20, 70, 311, 31))
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
        for item in self.__font_data:
            self.comboBox.addItem(item)

        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 170, 141, 31))
        self.comboBox_2.setStyleSheet("QComboBox {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QComboBox::drop-arrrow\n"
                                      "{\n"
                                      "border : 2px solid green;\n"
                                      "}")
        self.comboBox_2.setObjectName("comboBox_2")
        for item in self.__size_data:
            self.comboBox_2.addItem(item)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 220, 311, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 0px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.__handler.add_text)

        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(182, 170, 151, 31))
        self.comboBox_3.setStyleSheet("QComboBox {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QComboBox::drop-arrrow\n"
                                      "{\n"
                                      "border : 2px solid green;\n"
                                      "}")
        self.comboBox_3.setObjectName("comboBox_3")

        for item in self.__colours.keys():
            self.comboBox_3.addItem(item)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 20, 311, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 120, 311, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")


        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, -10, 361, 31))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 10, 21, 16))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border: none;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 10, 31, 16))
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border: none;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление текста"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_9.setText(_translate("MainWindow", "-"))
        self.pushButton_10.setText(_translate("MainWindow", "Х"))
