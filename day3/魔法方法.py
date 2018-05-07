# -*- cooding:utf-8 -*-
class Car:
    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor
#在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
#当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):
        msg = '颜色%s 车轮%d的车来了'%(self.color,self.wheelNum)
        return msg

    def move(self):
        print('车在跑')

BMW  = Car(4,'白色')
print(BMW)
