#!/usr/bin/python3
#coding: utf-8

#####
####Загляните в техническое задание/руководство к работе
#####
from sys import path as PYTHONPATH
PYTHONPATH.append("//home//ubuntu//workspace//project")

from BrailleGui import BrailleGui
from NewGui import Example
#import BrailleTranslator
def main():          #Иницилизация функции main для работы главного файла
    print("Hello, buys")
    
    #a = brailleTranslator.en_translations("aaaaaaa")
    #print(a.en_translation)
    window = BrailleGui()
    window.gui()
    
    
    
if __name__ == "__main__":
    main()
