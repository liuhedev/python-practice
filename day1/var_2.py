score = 100 # pytho定义变量方式：变量名= 变量值
totalScore = score * 6 # 如果totalScore是第一次使用，也是相当于定义了一个变量
score = 120 # 定义的变量用来使用，相当于重新赋值操作

# 使用input获取必要的信息
name = input("请输入用户姓名：")
score = input("请输入面试成绩（满分100分）：")# python3中，input输入的是字符串，会原样输出

# 使用print打印必要信息
print("您的名字是：%s"%name)
print("您的成绩是：%s"%score)


