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
        self.pic.setPixmap(QPixmap("""./startpic.png"""))
        self.pic.setScaledContents(True)


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

        self.grid.addWidget(TranslateButton,2,0)
        self.grid.addWidget(LoadFromFileButton,2,1)
        self.grid.addWidget(PrintButton,2,2)

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
        self.newpic = Picture()
        #self.pic.resize(310,430)
        self.newpic.show()


    def resizeEvent(self, event):
        self.w = self.textbox.width()
        self.h = self.textbox.height()
        self.pic.resize(self.w,self.h)
        print("w",self.w)
        print("h",self.h)


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

class Picture(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.pic = QLabel(self)
            self.pic.setPixmap(QPixmap("""./picture.png"""))
            self.pic.setScaledContents(True)
            self.grid = QGridLayout()
            self.grid.addWidget(self.pic)
            self.setLayout(self.grid)
            self.setWindowTitle("Picture")
            self.setWindowIcon(QIcon('braille.png'))
            self.setGeometry(300,100,310,430)
            self.pic.setScaledContents(True)


if __name__ == "__main__":

    ex = BrailleGui()
    sys.exit(app.exec_())
