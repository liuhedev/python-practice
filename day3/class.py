# -*- coding:utf-8 -*-
class Car:
    # 类方法第一个参数是当前类本身，我们习惯使用self标识。
# 如果加入一个参数，报错TypeError: toot() takes 0 positional arguments but 1 was given
    def move(self):
        print('车在奔跑...')
   # self可以是别的名字，但是通用self 
    def toot(s):
        print('车在鸣笛...')

#普通方法不需要加一个特定参数
def addTwo(a,b):
    print(a+b)


# 创建一个对象
BMW = Car()
# 定义属性
BMW.color='黑色'
BMW.wheelNum=4 

BMW.move()
BMW.toot()

print(BMW.color)
print(BMW.wheelNum)
