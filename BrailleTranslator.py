#!/usr/bin/python3
#coding: utf-8

from constant1 import alph
class BrailleTranslation:
    def __init__(self,ids):
        self.ids = ids # 0 - Arduino, 1 - GUI (На данный момент не работает)
        self.brailleList = [] # /\id это внутренний метод, так что переименовал в id
        self.isDigit = False
        self.isLower = True
        self.isUpper = False



    def translation(self,string): #Замечательная функция!
        for symbol in string:
            if symbol.isupper():
                if not self.isUpper:
                    self.isDigit = False
                    self.isLower = False
                    self.isUpper = True
                    self.brailleList.append(alph["UP"][self.ids])
                self.brailleList.append(alph[symbol.lower()][self.ids])

            elif symbol.isdigit():
                if not self.isDigit:
                    self.isDigit = True
                    self.isLower = False
                    self.isUpper = False
                    self.brailleList.append(alph["NUM"][self.ids])
                self.brailleList.append(alph[symbol][self.ids])

            elif symbol.islower():
                if not self.isDigit:
                    self.isDigit = False
                    self.isLower = True
                    self.isUpper = False
                    self.brailleList.append(alph["STR"][self.ids])
                self.brailleList.append(alph[symbol][self.ids])

            else:
                self.brailleList.append(alph[symbol][self.ids])

        return self.brailleList
