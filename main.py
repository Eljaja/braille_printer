#!/usr/bin/python3
#coding: utf-8

#####
####Загляните в техническое задание/руководство к работе
#####

from gui import *
import brailleTranslator
def main():          #Иницилизация функции main для работы главного файла
    print("Hello, buys")
    
    #a = brailleTranslator.en_translations("aaaaaaa")
    #print(a.en_translation)
  
    try:
        pass
        gui() # тут выводится пока только в консоль? 
    except Exception as err:
        if err != None:
            print("###########################")
            print(err)
            print("###########################")

if __name__ == "__main__":
    main()
