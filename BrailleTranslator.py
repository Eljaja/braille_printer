#!/usr/bin/python3
#coding: utf-8

from constant1 import alph
class BrailleTranslation:
    def __init__(self,id):
        self.id = id # 0 - Arduino, 1 - GUI (На данный момент не работает)
        self.brailleList = []
        self.isDigit = False
        self.isLower = True
        self.isUpper = False



    def translation(self,string):
        for symbol in string:
            if symbol.isupper():
                if not self.isUpper:
                    self.isDigit = False
                    self.isLower = False
                    self.isUpper = True
                    self.brailleList.append(alph["UP"][self.id])
                self.brailleList.append(alph[symbol.lower()][self.id])

            elif symbol.isdigit():
                if not self.isDigit:
                    self.isDigit = True
                    self.isLower = False
                    self.isUpper = False
                    self.brailleList.append(alph["NUM"][self.id])
                self.brailleList.append(alph[symbol][self.id])

            elif symbol.islower():
                if not self.isDigit:
                    self.isDigit = False
                    self.isLower = True
                    self.isUpper = False
                    self.brailleList.append(alph["STR"][self.id])
                self.brailleList.append(alph[symbol][self.id])

            else:
                self.brailleList.append(alph[symbol][self.id])

        return self.brailleList
