# -*- coding:utf-8 -*-
import os
# 1表示添加标识，2表示删除标识
funFlag = 1
folderName='./renameDir/'
# 获取指定路径下的文件名字
dirList= os.listdir(folderName)

print('----批量改名开始----')
# 遍历输出的文件名字
for name in dirList:
    print('----批量改名中: %s----'%name)
    if funFlag == 1:
        newName='[lh]-'+name
    elif funFlag==2:
        num = len('[lh]-')
        newName= name[num:]

    print('----批量改名中:%s----'%newName)
    os.rename(folderName+name,folderName+newName)
print('----批量改名结束----')
