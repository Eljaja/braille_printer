#!/usr/bin/python3
#coding: utf-8
#
from constant import alph


class BrailleTranslator:
    def __init__(self, ids=0):
        self.ids = ids  # 0 - Arduino, 1 - GUI (На данный момент не работает)
        self.brailleList = []  # /\id это внутренний метод, так что переименовал в ids
        self.isDigit = False
        self.isAlpha = True
        self.isUpper = False

    def translation(self, string):
        for symbol in string:
            if symbol.isalpha():
                if not self.isAlpha:
                    self.isAlpha = True
                    self.isDigit = False
                    self.brailleList.append(alph["STR"])
                #Если символ - буква, которая стоит после цифр - выведется символ букв
                if symbol.isupper():
                    if not self.isUpper:
                        self.isUpper = True
                        self.brailleList.append(alph["UP"])
                #Если символ - заглавная буква, то идет проверка на триггер и последущее
                #Выведение символа большой буквы
                else:
                    self.isUpper = False
                #Иначе выключается триггер большой буквы
                self.brailleList.append(alph[symbol.lower()])
                #Выводится буква

            elif symbol.isdigit():
                if not self.isDigit:
                    self.isDigit = True
                    self.isAlpha = False
                    self.isUpper = False
                    self.brailleList.append(alph["NUM"])
                self.brailleList.append(alph[symbol])

            else:
                self.isDigit = False
                self.isAlpha = True
                self.isUpper = False
                self.brailleList.append(alph[symbol])

        return self.brailleList
