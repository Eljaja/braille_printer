#!/usr/bin/python3
#coding: utf-8

#from pygame import *
import pygame

"""
Егор, тут некоторые ошибки с обращением к модулем:
когда ты импортируешь все классы модуля не надо обращаться к ним pygame.

"""
###
### in future - create a gui class(Егор, напиши мне)
###
WIDHT = 640
HEIGHT = 480
RESOLUTION = (WIDHT,HEIGHT) # задание разрешения
BACKGROUND_COLOR = pygame.Color('#FFFFFF') # задание цвета бэкграунда

def gui():
    pygame.init()
    mainscreen = pygame.display.set_mode(RESOLUTION) # создание окна
    pygame.display.set_caption('Printer') # подпись окна
    background = pygame.Surface(RESOLUTION) # создание поверхности (в данном случае бэкграунда)
    background.fill(BACKGROUND_COLOR) # заливка задника
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit # закрытие программы при нажатии на крестик в главном окне
        
        mainscreen.blit(background,(0,0)) # отрисовка в окне заднего фона, начиная с координаты (0,0)
        pygame.display.flip() # обновление изображения каждую итерацию цикла
gui()