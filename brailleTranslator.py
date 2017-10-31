#!/usr/bin/python3
#coding: utf-8

class BrailleTranslator:
    def __init__(self,text):
        self.text = text
        self.sheet = ['','','',''] # исходный лист
        self.string = 0 # номер строки
        
    def en_translation(self):  
        for symbol in self.text:  #посимвольная обработка
            if symbol == 'a':
                self.sheet[0+self.string*4] += '* '
                self.sheet[1+self.string*4] += '  '
                self.sheet[2+self.string*4] += '  '
                self.sheet[3+self.string*4] += '  '
                
            if symbol == 'b':
                self.sheet[0+self.string*4] += '* '
                self.sheet[1+self.string*4] += '* '
                self.sheet[2+self.string*4] += '  '
                self.sheet[3+self.string*4] += '  '
            
            if symbol == 'c':
                self.sheet[0+self.string*4] += '**'
                self.sheet[1+self.string*4] += '  '
                self.sheet[2+self.string*4] += '  '
                self.sheet[3+self.string*4] += '  '
                
            if symbol == 'd':
                self.sheet[0+self.string*4] += '**'
                self.sheet[1+self.string*4] += ' *'
                self.sheet[2+self.string*4] += '  '
                self.sheet[3+self.string*4] += '  '
        
        return self.sheet