# -*- coding:utf-8 -*-
class Person(object):
    country = 'china'
    # 类方法，使classmethod来修饰
    @classmethod
    def getCountry(cls):
        return cls.country


p = Person()

print(p.getCountry()) # 可以通过实例对象引用
print(Person.getCountry()) # 通过类对象引用


