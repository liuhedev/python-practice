# -*- coding:utf-8 -*-
import pygame

'''
    1. 搭建界面，主要完成窗口和背景图的显示
'''
if __name__ == '__main__':
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,800),0,32)
    # 2.创建一个和窗口大小的图片，充当背景
    background = pygame.image.load('./img/background.png').convert()
    # 3. 把背景图片放在窗口显示
    while True:
        screen.blit(background,(0,0))
        pygame.display.update()

