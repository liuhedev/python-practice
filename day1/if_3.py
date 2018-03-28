# python是一种弱类型语言，input输入的数据类型都相当于字符串类型，比如 20->"20"
age = input("请输入您的年龄:")
try:
    age_num = int(age)
    if age_num < 18  :
        print("未成年，去玩泥巴。")
    elif age_num > 80:
        print("大爷，注意身体，游戏伤身")
    else:
        print("已经成年了，可以去网吧了。")
except:
    print("请输入正确的年龄!!!!")






