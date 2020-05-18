import front
import sys
import os
import zipfile
import traceback
import re
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, front.Ui_MainWindow):
    directory, pathFile = '', ''

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле front.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации дизайна
        self.setStyleSheet('''.QWidget {background-image: url(tsvet1.jpg);} 
        .QPushButton {background-color: Chartreuse;  border-radius: 10px}
        .QPushButton:pressed{background-color: LimeGreen;border-style: inset;}
        
        ''')  # css стили для виджетов
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.btnArch.clicked.connect(self.arch_folder)
        self.browseArch.clicked.connect(self.browse_arch)
        self.exButton.clicked.connect(self.extract)

        self.dialog = front.Dialog()

    def browse_folder(self):
        self.directory, self.pathFile = '', ''
        self.dialog.exec_()
        if self.dialog.rbDir.isChecked():
            self.listWidget.clear()  # На случай, если в списке уже есть элементы
            self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

            if self.directory:  # не продолжать выполнение, если пользователь не выбрал директорию
                for file_name in os.listdir(self.directory):  # для каждого файла в директории
                    self.listWidget.addItem(file_name)  # добавить файл в listWidget
        elif self.dialog.rbPath.isChecked():
            self.pathFile, _ = QtWidgets.QFileDialog.getOpenFileName(
                self,
                'Open File', './',
            )
            if self.pathFile:
                self.listWidget.addItem(self.pathFile)  # добавить файл в listWidget

    def arch_folder(self):  # архивация
        dirfiles = []
        if self.pathFile == '':
            try:
                dirfiles = os.listdir(self.directory)
            except FileNotFoundError:
                QtWidgets.QMessageBox.information(None, 'Ошибка', 'Выберите папку')
        else:
            pass
        if dirfiles:
            archive = zipfile.ZipFile('test.zip', 'w')
            try:
                for file in dirfiles:
                    try:
                        archive.write(self.directory+"/"+file, compress_type=zipfile.ZIP_DEFLATED)
                    except:
                        QtWidgets.QMessageBox.information(None, 'Ошибка', 'Что-то пошло не так')
            except:
                QtWidgets.QMessageBox.information(None, 'Ошибка', 'Что-то пошло не так')
            else:
                QtWidgets.QMessageBox.information(None, 'Успех', 'Архивирование успешно завершено')
        if self.pathFile:
            archive = zipfile.ZipFile('test.zip', 'w')
            try:
                archive.write(self.pathFile, compress_type=zipfile.ZIP_DEFLATED)
            except:
                QtWidgets.QMessageBox.information(None, 'Ошибка', 'Что-то пошло не так')
            else:
                QtWidgets.QMessageBox.information(None, 'Успех', 'Архивирование успешно завершено')
            archive.close()

    def browse_arch(self):  # выбор архива для извлечения
        self.exlist.clear()
        self.archive = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите архив", filter="Archives (*.zip)")
        if self.archive[0] != '':
            zip_arch = zipfile.ZipFile(self.archive[0], 'r')
            for filename in zip_arch.namelist():
                print(re.search(r'[^/]*$', filename).group())
                self.exlist.addItem(filename)

    def extract(self):  # извлечение
        try:
            if self.archive[0] != '':
                extract_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку для извлечения")
                if extract_path:
                    zip_arch = zipfile.ZipFile(self.archive[0], 'r')
                    try:
                        zip_arch.extractall(extract_path)
                    except:
                        QtWidgets.QMessageBox.information(None, 'Ошибка', 'Что-то пошло не так')
                    else:
                        QtWidgets.QMessageBox.information(None, 'Успех', 'Извлечение успешно завершено')
                    zip_arch.close()
                self.exlist.clear()
        except AttributeError:
            QtWidgets.QMessageBox.information(None, 'Ошибка', 'Выберите архив')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
