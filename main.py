#!/usr/bin/python3
#coding: utf-8

#####
####Загляните в техническое задание/руководство к работе
#####
#from sys import path as PYTHONPATH
#PYTHONPATH.append("//home//ubuntu//workspace//project")

from BrailleGui import BrailleGui
#import BrailleTranslator
def main():          #Иницилизация функции main для работы главного файла
    print("Hello, buys")
    
    #a = brailleTranslator.en_translations("aaaaaaa")
    #print(a.en_translation)
    window = BrailleGui()
    window.gui()
    
'''
    try:
        pass
    except Exception as err:
        if err != None:
            print("###########################")
            print(err)
            print("###########################")
'''
if __name__ == "__main__":
    main()
