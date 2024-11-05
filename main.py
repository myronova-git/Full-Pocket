import tkinter as tk
import sqlalchemy as db
import sys
import sqlite3
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLineEdit

category_db = db.create_engine('sqlite:///category.db')

#Главное окно приложения
class FullPocket(QMainWindow):
    def __init__(self):
        super(FullPocket, self).__init__()
        uic.loadUi('full_pocket.ui', self)
        self.pushButton_1.clicked.connect(self.window_1)

    def window_1(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


class Window_1(QMainWindow):
    def __init__(self):
        super(Window_1, self).__init__()
        uic.loadUi('window_1.ui', self)
        # self.pushButton.clicked.connect(self.addCategory)
        self.lineEdit = self.findChild(QLineEdit, 'lineEdit')
        self.pushButton_1.clicked.connect(self.show_text)


    def show_text(self):
        if self.lineEdit.text():
            self.lineEdit_2.setText("Категория введена")

        else:
            self.lineEdit_2.setText("Введите пожалуйсто категорию")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    tab_widget = QTabWidget()
    tab_widget.addTab(Window_1(), 'Full Pocket')
    tab_widget.setFixedHeight(791)
    tab_widget.setFixedWidth(1256)
    widget.show()
    full_pocket = FullPocket()
    window1 = Window_1()
    widget.addWidget(full_pocket)
    widget.addWidget(window1)
    widget.setFixedHeight(791)
    widget.setFixedWidth(1256)
    widget.show()

    sys.exit(app.exec_())

