# -*- coding:utf-8 -*-
import time
class Animal:
    # 初始化方法
    # 创建完对象后自动调用
    def __init__(self,name):
        print('__init__方法被调用')
        self.__name=name
        self.color='red'

    def __test(self):
        print('__test调用')
        print(self.__name)
        print(self.color)

    def test(self):
        print('test 调用')

    # 析构方法
    # 当对象呗删除时，自动调用
    def __del__(self):
        print('__del__方法被调用')
        print('%s对象马上被干掉了。。。'%self.__name)

# 创建对象
dog = Animal('哈皮狗')

dog.test()

# 删除对象
del dog


