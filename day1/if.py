# python是一种弱类型语言，input输入的数据类型都相当于字符串类型，比如 20->"20"
age = input("请输入您的年龄:")
try:
    age_num = int(age)
    if age_num > 18 :
        print("已经成年，可以去网吧了")
    else:
        print("未成年，去玩泥巴")
except:
    print("请输入正确的年龄!!!!")






