#!/usr/bin/python3
#coding: utf-8

import serial #With arduino



###
### in future - with different os
###
class AruinoWrite:
    def __init__(self,port="/dev/ttyUSB0"):
        self.port = port
        self.ser = serial.Serial(port)
    
    def find
        
    def writing(self,data):
        self.err = "Ok"
        try:
            self.ser.write(data)
        ret
            self.err = str(error)
        return self.err
    