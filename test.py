#!/usr/bin/python3
#coding: utf-8

class BrailleTranslatorEN:
    def __init__(self):
        import constant #Импорт алфавитов
        self.alph = constant.alph
        del constant
        self.num = dict(zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "h"]))


    def Translation(self, en_str):
        isnum =  lambda char: True if char in "1234567890" else False
        
        strFlag = False
        self.res = []
        while en_str:
            char = en_str[0]
            if char.isupper():
                if strFlag:
                    self.res.append(self.alph["STR"])
                    strFlag = False
                self.res.append(self.alph["UP"])
                try:
                    self.res.append(self.alph[char.lower()])
                except KeyError:
                    pass
                en_str = en_str.replace(char, "", 1)
                
            elif isnum(char):
                self.res.append(self.alph["NUM"])
                while isnum(char):
                    self.res.append(self.alph[self.num[int(char)]])
                    en_str = en_str.replace(char, "", 1)
                    if en_str == "":
                        break
                    char = en_str[0]
                strFlag = True
                
            else:
                if strFlag:
                    self.res.append(self.alph["STR"])
                    strFlag = False
                try:
                    self.res.append(self.alph[char])
                except KeyError:
                    pass
                en_str = en_str.replace(char, "", 1)
                
                
        return self.res
        
        
        
        
a = BrailleTranslatorEN()
print(a.Translation("2"))

# Ошибка при вводе любой цифры; Пофикшено, но по дебильному, ибо брейк - зло!!!!!!!!!!!!!!!!!!!!!!!!!!