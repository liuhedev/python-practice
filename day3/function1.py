# -*- coding:utf-8 -*-
# 定义一个全局变量
a=10
def test1():
    global a 
    '''
        如果不声明global，下边用到的a会当做局部变量使用，
        会报错UnboundLocalError: local variable 'a'referenced before assignment'
    '''
    print('--test1--修改前--a=%d'%a)
    a=300
    print('--test1--修改后--a=%d'%a)

def test2():
    print('--test2--a=%d'%a)

print('你好，世界')
test1()
test2()
