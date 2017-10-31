#!/usr/bin/python3
#coding: utf-8

from pygame import *

###
### in future - create a gui class(Егор, напиши мне)
###
"""
Бля, почему крестик не работает
"""
WIDHT = 640
HEIGHT = 480
RESOLUTION = (WIDHT,HEIGHT) # задание разрешения
BACKGROUND_COLOR = Color('#FFFFFF') # задание цвета бэкграунда

def gui():
    init()
    mainscreen = display.set_mode(RESOLUTION) # создание окна
    display.set_caption('Printer') # подпись окна
    background = Surface(RESOLUTION) # создание поверхности (в данном случае бэкграунда)
    background.fill(BACKGROUND_COLOR) # заливка задника
    
    while True:
    
        for event in event.get():
            if event.type == QUIT:
                raise SystemExit # закрытие программы при нажатии на крестик в главном окне
        mainscreen.blit(background,(0,0)) # отрисовка в окне заднего фона, начиная с координаты (0,0)
        display.flip() # обновление изображения каждую итерацию цикла
gui()