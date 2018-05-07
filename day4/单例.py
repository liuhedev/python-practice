# -*- coding:utf-8 -*-
# 实例化一个单例
class Singleton(object):
    __instance = None
    __first_init=False # 创建单例时，为保证执行一次__init__方法，标识。
    def __init__(self,age,name):

       ''' 确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，单例模式是一种对象创建型模式。'''
       
       if not self.__first_init:
           print('init')
           self.age = age
           self.name = name
           Singleton.__first_init = True
       # print('init')

    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance= object.__new__(cls)
        return cls.__instance

a = Singleton(18,'liuhe')
b = Singleton(8,'liuhe')

print(id(a))
print(id(b))

a.age = 19
print(b.age)
