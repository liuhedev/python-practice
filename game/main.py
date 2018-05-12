# -*- coding:utf-8 -*-
import pygame
import random
from pygame.locals import *
class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+40
        self.y  =y -20
        self.screen = screen
        self.image = pygame.image.load('./img/bullet-3.gif').convert()

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

    def move(self):
        self.y -=2
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x = x+30
        self.y = y+30
        self.screen = screen
        self.image = pygame.image.load("./img/bullet-1.gif").convert()

    def move(self):
        self.y += 2

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def judge(self):
        if self.y>890:
            return True
        else:
            return False


# 敌机
class EnemyPlane(object):
    def __init__(self,screen):
        # 设置飞机默认的位置
        self.x = 0
        self.y = 0

        # 设置要显示内容的窗口
        self.screen = screen
        self.imageName = './img/enemy-1.gif'
        self.image= pygame.image.load(self.imageName).convert()

        # 用来存储敌人飞机发射的所有子弹
        self.bulletList = []
        self.direction='right'

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        # 存放需要删除的对象信息
        needDelItemList=[]
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.bulletList.remove(i)
        # 更新飞机发射所有子弹位置
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
    # 如果碰到右边界，就往左走，如果碰到左边界就往右走
    def move(self):
        if self.direction == 'right':
                self.x+=2
        elif self.direction == 'left':
            self.x -=2

        if self.x >480-50:
            self.direction='left'
        elif self.x <0:
            self.direction='right'
    def sheBullet(self):
        num = random.randint(1,100)
        if num == 88:
            newBullet = EnemyBullet(self.x,self.y,self.screen)
            self.bulletList.append(newBullet)

# 我的飞机
class HeroPlane(object):
    def __init__(self,screen):
        # 设置飞机默认位置
        self.x = 230
        self.y = 600

        # 设置要显示内容的窗口
        self.screen = screen

        # 用来保存英雄飞机需要的图片名字
        self.imageName = './img/hero.gif'

        # 根据名字生成飞机图片
        self.image = pygame.image.load(self.imageName).convert()

        # 用来保存英雄飞机发射出的所有子弹
        self.bulletList=[]

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image,(self.x,self.y))
        # 用来存放需要删除的对象信息
        needDelItemList = []
        # 保存需要删除的对象
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        # 删除self.bulletList中需要删除的对象
        for i in needDelItemList:
            self.bulletList.remove(i)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def moveLeft(self):
        self.x -=10
    
    def moveRight(self):
        self.x +=10
    
    def sheBullet(self):
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)

'''
    1. 搭建界面，主要完成窗口和背景图的显示
    2. 检测事件，比如按键操作
    3.  使用面向过程的方式来显示一个飞机，并控制其左右移动
'''
if __name__ == '__main__':
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,800),0,32)
    # 2.创建一个和窗口大小的图片，充当背景
    background = pygame.image.load('./img/background.png').convert()
    # 3. 把背景图片放在窗口显示
    heroPlane =HeroPlane(screen)
    # 创建敌人飞机
    enemyPlane = EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))
        
        heroPlane.display()
        
        enemyPlane.move()
        enemyPlane.sheBullet()
        enemyPlane.display()

        #获取事件，比如按键等
        for event in pygame.event.get():
            # 判断是否点击了退出按钮
            if event.type == QUIT:
                print('exit')
                exit()
            # 判断是否按下了键
            elif event.type == KEYDOWN:
                # 检测首付按下了a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    heroPlane.moveLeft()
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    heroPlane.moveRight()
                elif event.key == K_SPACE:
                    print('space')
                    heroPlane.sheBullet()
              # 更新需要显示的内容
        pygame.display.update()
