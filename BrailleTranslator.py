#!/usr/bin/python3
#coding: utf-8

from constant1 import alph
class BrailleTranslation:
    def __init__(self,ids):
        self.ids = ids # 0 - Arduino, 1 - GUI (На данный момент не работает)
        self.brailleList = [] # /\id это внутренний метод, так что переименовал в id
        self.isDigit = False
        self.isAlpha = True
        self.isUpper = False



    def translation(self,string): #Замечательная функция!
        for symbol in string:
            if symbol.isalpha():
                if not self.isAlpha:
                    self.isAlpha = True
                    self.isDigit = False
                    self.brailleList.append(alph["STR"][self.ids])
                #Если символ - буква, которая стоит после цифр - выведется символ букв   
                if symbol.isupper():
                    if not self.isUpper:
                        self.isUpper = True
                        self.brailleList.append(alph["UP"][self.ids])
                #Если символ - заглавная буква, то идет проверка на триггер и последущее
                #Выведение символа большой буквы
                else:
                    self.isUpper = False
                #Иначе выключается триггер большой буквы
                self.brailleList.append(alph[symbol.lower()][self.ids])
                #Выводится буква
                    

            elif symbol.isdigit():
                if not self.isDigit:
                    self.isDigit = True
                    self.isAlpha = False
                    self.isUpper = False
                    self.brailleList.append(alph["NUM"][self.ids])
                self.brailleList.append(alph[symbol][self.ids])
                
            else:
                self.isDigit = False
                    self.isAlpha = True
                    self.isUpper = False
                self.brailleList.append(alph[symbol][self.ids])

        return self.brailleList
