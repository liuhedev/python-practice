# -*- coding:utf-8 -*-
# 以追加方式打开一个文件，
#f = open('file.txt','w')
#f.write('open(文件名，读写模式)')
#f.close()

# 读取文件
#如果之前close掉文件，需要重新打开，否则会报错： ValueError: I/O operation on closed file.
f = open('file.txt','r')
# 使用read(num)可以从文件中读取数据，num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据
#readContent = f.read(5)
readContent=f.readline()
print('readContent:%s'%readContent)
