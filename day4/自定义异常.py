# -*- coding:utf-8 -*-
class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self,length,atleast):
        self.length=length
        self.atleast = atleast

def main():
    try:
        s = input('请输入-->')
        if len(s) < 3:
            # raise 引发一个自定义的异常
            raise ShortInputException(len(s),3)
    except ShortInputException as result: # 将这个变量绑定到错误实例上
        print('ShortInputException:输入的长度%d,长度至少应该是%d'%(result.length,result.atleast))
    else:
        print('没有异常发生')

main()

