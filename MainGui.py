#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from DrawList import DrawList
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from ArduinoWrite import AruduinoWrite
app = QApplication(sys.argv)



class BrailleGui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.textbox = QTextEdit(self)

        self.pic = QLabel(self)

        TranslateButton = QPushButton("Translate",self)

        LoadFromFileButton = QPushButton("From File..",self)

        PrintButton = QPushButton("Print!",self)

        TranslateButton.clicked.connect(self.eventTranslate)
        LoadFromFileButton.clicked.connect(self.showDialog)
        PrintButton.clicked.connect(self.eventPrint)

        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.textbox,0,0)
        self.grid.addWidget(self.pic,0,1)

        self.grid.addWidget(TranslateButton,1,0)
        self.grid.addWidget(LoadFromFileButton,1,1)
        self.grid.addWidget(PrintButton,1,2)


        self.setLayout(self.grid)

        self.setGeometry(300,100,640,480)
        self.setWindowTitle("Printer V0.1")
        self.setWindowIcon(QIcon('braille.png'))
        self.show()

    def eventPrint(self): #Я ещё тут подумаю
        pass

    def eventTranslate(self):

        Draw = DrawList()
        text = Draw.drawBraille(str(self.textbox.toPlainText()))
        Draw.saveFile()
        self.pic.setPixmap(QPixmap("""./picture.png"""))
        # self.pic.resize(310,430)
        # self.pic.show()


    def resizeEvent(self, event):
        self.w = self.textbox.width()
        self.h = self.textbox.height()

        print("w",self.textbox.width())
        print("h",self.textbox.height())


    def showDialog(self):
        try:
            fname = QFileDialog.getOpenFileNames(self, "Open file")[0][0]
        except IndexError:
            pass

        with open(fname, encoding="utf-8") as FileData:
            self.textbox.setText(FileData.read())


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":

    ex = BrailleGui()
    sys.exit(app.exec_())
