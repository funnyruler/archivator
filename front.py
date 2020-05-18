# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow { background-image: url(:/background/tsvet1.jpg); }\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(0, 0, 131, 23))
        self.btnBrowse.setObjectName("btnBrowse")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 131, 151))
        self.listWidget.setObjectName("listWidget")
        self.btnArch = QtWidgets.QPushButton(self.centralwidget)
        self.btnArch.setGeometry(QtCore.QRect(30, 170, 81, 23))
        self.btnArch.setObjectName("btnArch")
        self.browseArch = QtWidgets.QPushButton(self.centralwidget)
        self.browseArch.setGeometry(QtCore.QRect(170, 0, 131, 23))
        self.browseArch.setObjectName("browseArch")
        self.exlist = QtWidgets.QListWidget(self.centralwidget)
        self.exlist.setGeometry(QtCore.QRect(170, 20, 131, 151))
        self.exlist.setObjectName("exlist")
        self.exButton = QtWidgets.QPushButton(self.centralwidget)
        self.exButton.setGeometry(QtCore.QRect(190, 170, 91, 23))
        self.exButton.setObjectName("exButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Archivator"))
        self.btnBrowse.setText(_translate("MainWindow", "Выбрать..."))
        self.btnArch.setText(_translate("MainWindow", "Архивировать"))
        self.browseArch.setText(_translate("MainWindow", "Выбрать архив"))
        self.exButton.setText(_translate("MainWindow", "Извлечь"))


class Dialog(QtWidgets.QDialog):                                                   # +++
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        label = QtWidgets.QLabel("Выберите:")
        self.rbDir = QtWidgets.QRadioButton('Папку', self)
        self.rbPath = QtWidgets.QRadioButton('Файл', self)
        btnOk = QtWidgets.QPushButton("Ok", clicked=self.hide)

        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(label, 0, 0, 1, 3)
        layout.addWidget(self.rbDir, 1, 1, 1, 1)
        layout.addWidget(self.rbPath, 2, 1, 1, 1)
        layout.addWidget(btnOk, 3, 2, 1, 1)
