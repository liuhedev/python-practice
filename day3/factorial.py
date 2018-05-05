# -*- coding:utf-8 -*-
# 递归 完成阶乘计算
def calNum(num):
    if num >=1:
        result= num * calNum(num-1)
    else:
        result=1
    return result

ret = int(input('请输入需要计算的阶乘数：'))
print('calNum(%d)=%d'%(ret,calNum(ret)))
