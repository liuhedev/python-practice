#coding=utf-8
class BaseA(object):
    def __init__(self):
        print('----BaseA init----')

    def test(self):
        print('----BaseA test----')

class BaseB(object):
    def __init__(self):
        print('----BaseB init----')

    def test(self):
        print('----BaseB test----')

# 定义一个父类
class Child(BaseA,BaseB):
    pass

    def __init__(self):
    # 调用父类的__init__方法1(python2)
        #BaseA.__init__(self)
        # 调用父类的__init__方法2
        #super(BaseA,self).__init__()
        # 调用父类的__init__方法3
        super().__init__()
        print('-----child init----')
    
    # 子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法 
    #def test(self):
    #   print('----child  test----')


child = Child()
# 注掉Child中的__init__和test后，走BaseA的__init__和test方法
child.test()
