# -*- coding:utf-8 -*-
class Car:
    def __init__(self,newWheelNum,newColor):
        self.wheelNum=newWheelNum
        self.color=newColor
    def move(self):
        print('车在跑，目标->云南')

# 创建对象
BMW=Car(4,'white')
BENCHI=Car(4,'black')

print('车的颜色：%s'%BMW.color)
print('车轮胎数量：%d'%BMW.wheelNum)
