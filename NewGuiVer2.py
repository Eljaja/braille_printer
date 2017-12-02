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
        self.textbox.resize(310,430)
        self.textbox.move(10,10)


        self.pic = QLabel(self)
        self.pic.resize(310,430)
        self.pic.move(330,10)

        TranslateButton = QPushButton("Translate",self)
        TranslateButton.move(10,445)
        TranslateButton.resize(100,30)

        LoadFromFileButton = QPushButton("From File..",self)
        LoadFromFileButton.move(120,445)
        LoadFromFileButton.resize(100,30)
        PrintButton = QPushButton("Print!",self)

        PrintButton.move(230,445)
        PrintButton.resize(100,30)

        TranslateButton.clicked.connect(self.eventTranslate)
        LoadFromFileButton.clicked.connect(self.showDialog)
        PrintButton.clicked.connect(self.eventPrint)


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
        self.pic.resize(310,430)
        self.pic.show()

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
