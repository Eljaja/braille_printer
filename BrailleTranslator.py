#!/usr/bin/python3
#coding: utf-8

from constant1 import alph
class BrailleTranslation:
    def __init__(self,id):
        self.id = id # 0 - Arduino, 1 - GUI (Работает частично)
        self.brailleList = []
        self.isDigit = False



    def translation(self,string):
        for symbol in string:
            if symbol.isupper():
                self.brailleList.append(alph["UP"][self.id])
                self.brailleList.append(alph[symbol.lower()][self.id])

            elif symbol.isdigit():
                if not self.isDigit:
                    self.isDigit = True
                    self.brailleList.append(alph["NUM"][self.id])
                self.brailleList.append(alph[symbol][self.id])

            else:
                self.isDigit = False
                self.brailleList.append(alph[symbol][self.id])

        return self.brailleList

test = BrailleTranslation(0)
print(test.translation("12"))