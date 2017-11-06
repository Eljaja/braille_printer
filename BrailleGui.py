#!/usr/bin/python3
#coding: utf-8

from BrailleTranslator import BrailleTranslator

import pygame as pg # Импортировал pygame сократил его до pg )))
from pygame.locals import *


class BrailleGui:
    
    def __init__(self,WIDHT=640,HEIGHT=480):
        self.RESOLUTION = (WIDHT,HEIGHT)
        self.BACKGROUND_COLOR = Color('#FFFFFF')
        self.TEXT_COLOR = Color('#000000')


    def gui(self):
        
        pg.init()
        mainscreen = pg.display.set_mode(self.RESOLUTION) # создание окна
        pg.display.set_caption('Printer') # подпись окна
        background = pg.Surface(self.RESOLUTION) # создание поверхности (в данном случае бэкграунда)
        background.fill(self.BACKGROUND_COLOR) # заливка задника
        
        testtext = 'bc'
        testsheet = BrailleTranslator(testtext).en_translation() # перевод текста в шрифт Брайля
        x = 340
        y = 20
        
        
        while True:
        
            for event in pg.event.get():
                if event.type == QUIT:
                    raise SystemExit # закрытие программы при нажатии на крестик в главном окне
            
            pg.draw.rect (background,self.TEXT_COLOR,(5,5,310,400),5) # cоздание рамки ввода текста (примитивного интерфейса)
            pg.draw.rect (background,self.TEXT_COLOR,(325,5,310,400),5) # cоздание рамки вывода шрифта Брайлля (примитивного интерфейса)
            
            
            for string in testsheet: # Отрисовка кружочков 
                for symbol in string:
                    if symbol == '*':
                        pg.draw.circle (background,self.TEXT_COLOR,(x+3,y+3),3)
                    x+=7
                x=340
                y+=7
            y=20    
                        
            mainscreen.blit(background,(0,0)) # отрисовка в окне заднего фона, начиная с координаты (0,0)
            
            pg.display.flip() # обновление изображения каждую итерацию цикла