# -*- coding: utf-8 -*-
import sys
import punch_clock
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Journeyman")

        button = QPushButton(text="Punch", parent=self)
        button.setGeometry(0,0,100,50)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
