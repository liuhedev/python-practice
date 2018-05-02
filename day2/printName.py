# 打印功能提示
print('='*50)
print('名字管理系统(输入exit 退出)'.center(30))
print('1:添加一个名字')
print('2:删除一个名字')
print('3:修改一个名字')
print('4:查询一个名字')
print('='*50)

# 获取用户输入
names=[] # 定义一个空的列表，存储添加的名字
# 根据用户选择，执行响应功能
while(True):
    
    try:
      num = int(input('请输入功能序号'))
    except:
        print('异常输入，清新输入序号：')
        continue

    newName=input('请输入名字:')
    if newName.lower() =='exit':
        print('退出系统！')
        break
    
    elif num == 1:
        names.append(newName)
        print(names)
    
    elif num == 2:
        try:
           index = names.index(newName)
           # remove删除值 del 删除索引对应的值
           del names[index]
           print('找到删除此值,', end='')
           print(names)
        except:
            print('查无此人,无法删除！')
        pass

    elif num == 3:
        try:
           index = names.index(newName)
           names[index]=newName
           print('找到修改了：'+names[index])
        except:
            print('查无此人,无法修改！')

    elif num == 4:
        findName=newName in names
        if(findName):
            print("找到了!")
        else:
            print('查无此人！')
else:
    print('请继续输入！')
