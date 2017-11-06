#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from BrailleTranslator import BrailleTranslation
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.textbox = QTextEdit(self)
        self.braillebox = QTextEdit(self)
        self.braillebox.setReadOnly(True)
        self.transButton = QPushButton("Translate")
        self.loadText = QPushButton("Load from File...")
        self.transButton.clicked.connect(self.buttonClicked)
        self.loadText.clicked.connect(self.showDialog)
        self.initUI()

    def initUI(self):
        self.textwindows = QHBoxLayout()
        self.buttons = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.textwindows.addWidget(self.textbox)
        self.textwindows.addWidget(self.braillebox)
        self.buttons.addWidget(self.transButton)
        self.buttons.addWidget(self.loadText)
        self.buttons.addStretch(1)
        self.vbox.addLayout(self.textwindows)
        self.vbox.addSpacing(5)
        self.vbox.addLayout(self.buttons)
        self.setLayout(self.vbox)

        self.setGeometry(300,100,640,480)
        self.setWindowTitle("Printer V0.1")
        self.show()

    def buttonClicked(self):
        self.bt = BrailleTranslation(1)
        #Вывод элементов в юникоде  
        self.braillebox.setText("".join(self.bt.translation(str(self.textbox.toPlainText()) )))
        #Вывод элементов списка как строки в правом окне

    def showDialog(self):
        try:
            fname = QFileDialog.getOpenFileNames(self, "Open file")[0][0]
        except IndexError:
            return None
        #Конструкция try-except сделана для того, чтобы пофиксить баг с вылетом
        #из-за нажатия крестика в меню выбора файла
        print(fname)
        
        with open(fname, encoding="utf-8") as FileData:
            self.textbox.setText(FileData.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())