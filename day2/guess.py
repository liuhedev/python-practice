import random
player = input('请输入：剪刀（0）石头（1）布（2）：')
player = int(player)
computer= random.randint(0,2)

if((player ==0 and computer ==2)) or ((player==1) and (computer==0)) or ((player==2) and (computer==1)):
    print("获胜")
elif player == computer:
    print('平局')
else:
    print('呵呵')
