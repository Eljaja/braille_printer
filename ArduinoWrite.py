#!/usr/bin/python3
#coding: utf-8

import serial  #With arduino

from sys import platform  # check os


###
### in future - with different os
###
class AruinoWrite:
    def __init__(self, port=False):
        if not port:
            self.CheckOS()
        self.ser = serial.Serial(self.port)

    def CheckOS(
            self):  # чек платформы с помощью модуля sys и переменной platform
        if platform == "linux" or platform == "linux2":
            self.port = "/dev/ttyUSB0"
        elif platform == "win32" or platform == "win64":
            self.port = "COM3"

    def writing(self, data):  #передача информации на arduino по serial
        self.err = "Ok"
        try:
            self.ser.write(data)
            return self.err
        except Exception as error:
            self.err = str(error)
        return self.err
