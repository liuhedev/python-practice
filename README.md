# PythonNote
### python复合运算符 *=
```
In [1]: a=3
#a=a*(4+3)=21
In [2]: a*=4+3  

```
### print
> 默认换行

```
#使用end 使print不换行
print("*",end="") 
```

### break
> 就近原则

```
	i =  1
	while i<=5 :
		j = 1
		while j<=i :
			print("*",end="")
			j+=1
			break # 跳出内层的while,继续执行外层while
		print("") # 换行
		i+=1
		break
		
```

## 字符串
> 双引号或者单引号中的数据，就是字符串

```
str='liuhe'
len(str) # 计算字符串多少个字节，字节是最小处理单元。
```
### 两种组成字符串的方式

```
name = 'liuhe'

merge1 = '---' + name + '---'
merge2 = '---%s---'%name
```
### 切片
> 从字符串取出一部分，包左不包右。
切片的语法：

```
[起始:结束:步长]
```

```
In [17]: name
Out[17]: 'liuhe'

In [21]: name[2:4]
Out[21]: 'uh'

In [22]: name[2:-1] #从角标2开始，一直到倒数第二个字符
Out[22]: 'uh'

In [23]: name[2:] # 从角标2开始，一直末尾
Out[23]: 'uhe'

In [26]: name[2:-1:2]
Out[26]: 'u'
```

### 倒序

```
In [17]: name
Out[17]: 'liuhe'

In [31]: name[-1:0:-1]
Out[31]: 'ehui'

# 逆序
In [30]: name[::-1]
Out[30]: 'ehuil'
```

### 字符串操作
#### find  查找 rfind 反向查找
```
In [39]: myStr
Out[39]: 'liuhe haha zhengdejuan'

In [40]: myStr.find('zhengde')
Out[40]: 11 # 匹配的索引

In [41]: myStr.find('liuhe')
Out[41]: 0 

In [42]: myStr.find('rourou')
Out[42]: -1 # 未找到匹配值

# rfind 反向（right）查找
In [47]: myStr.rfind('he')
Out[47]: 12

In [48]: myStr.find('he')
Out[48]: 3
```

#### index 
> 使用和find类似，但是index会报异常。

```
#index 抛异常
In [50]: name.index('rou')
------------------------------------
ValueErrorTraceback (most recent call last)
<ipython-input-50-843383394ce5> in <module>()
----> 1 name.index('rou')

ValueError: substring not found

#find 返回-1
In [51]: name.find('rou')
Out[51]: -1
```

#### count 计数

```
In [59]: myStr
Out[59]: 'liuhe haha zhengdejuan'

In [60]: myStr.count('he')
Out[60]: 2
```
#### replace 替换

> 替换后，原字符串不变化

格式:

```
(原字符串，要替换的字符，替换次数[可选，不会超过count次，但是指定的个数可以超过count值])
```
  
```
In [62]: myStr.replace('n','N')
Out[62]: 'liuhe haha zheNgdejuaN'

In [63]: myStr
Out[63]: 'liuhe haha zhengdejuan'

In [4]: myStr.replace('n','N',0)
Out[4]: 'liuhe haha zhengdejuan'

In [5]: myStr.replace('n','N',1)
Out[5]: 'liuhe haha zheNgdejuan'

In [6]: myStr.replace('n','N',13)
Out[6]: 'liuhe haha zheNgdejuaN'

```
#### split 切割

```
In [7]: myStr.split(' ')
Out[7]: ['liuhe', 'haha', 'zhengdejuan']
```

#### 其它

```
# 每个单词首字母大写
In [8]: myStr.title()
Out[8]: 'Liuhe Haha Zhengdejuan'

#一个字符串第一个单词首字母大写
In [9]: myStr.capitalize()
Out[9]: 'Liuhe haha zhengdejuan'

# endswith
In [10]: fileName='xx.txt'
In [11]: fileName.endswith(".txt")
Out[11]: True
```