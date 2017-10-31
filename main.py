#!/usr/bin/python3
#coding: utf-8

#####
####Загляните в техническое задание/руководство к работе
#####

from gui import *

def main():          #Иницилизация функции main для работы главного файла
    print("Hello, buys")
    
    try:
        gui()
    except Exception as err:
        if err != None:
            print("###########################")
            print(err)
            print("###########################")

if __name__ == "__main__":
    main()
