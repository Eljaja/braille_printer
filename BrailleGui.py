#!/usr/bin/python3
#coding: utf-8

from BrailleTranslator import BrailleTranslator

import pygame as pg # Импортировал pygame сократил его до pg )))
from pygame.locals import *


class BrailleGui:
    
    def __init__(self,WIDHT=640,HEIGHT=480):
        self.RESOLUTION = (WIDHT,HEIGHT)
        self.BACKGROUND_COLOR = Color('#FFFFFF')


    def gui(self):
        
        pg.init()
        mainscreen = pg.display.set_mode(self.RESOLUTION) # создание окна
        pg.display.set_caption('Printer') # подпись окна
        background = pg.Surface(self.RESOLUTION) # создание поверхности (в данном случае бэкграунда)
        background.fill(self.BACKGROUND_COLOR) # заливка задника
        
        testtext = 'abcd'
        testsheet = BrailleTranslator(testtext).en_translation() # перевод текста в шрифт Брайля
        
        for string in testsheet:    # построчный вывод текста
            print(string)
        
        while True:
        
            for event in pg.event.get():
                if event.type == QUIT:
                    raise SystemExit # закрытие программы при нажатии на крестик в главном окне
                    
            mainscreen.blit(background,(0,0)) # отрисовка в окне заднего фона, начиная с координаты (0,0)
            pg.display.flip() # обновление изображения каждую итерацию цикла