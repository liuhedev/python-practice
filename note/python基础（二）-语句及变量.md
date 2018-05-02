# python基础（二）-语句及变量

[TOC]

## 语句

### 判断语句

```
if xxx1:
        事情1
    elif xxx2:
        事情2
    elif xxx3:
        事情3
```

### 循环语句

```
while 条件:
        条件满足时，做的事情1
        条件满足时，做的事情2
        ...(省略)...
```

 
```
for 临时变量 in 列表或者字符串等:
        循环满足条件时执行的代码
    else:
        循环不满足条件时执行的代码
```
     
### break与continue

区别：
* break的作用：用来结束整个循环
* continue的作用：用来结束本次循环，紧接着执行下一次的循环

注意事项：
* break/continue只能用在循环中，除此以外不能单独使用
* break/continue在嵌套循环中，只对最近的一层循环起作用

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


### find  查找 rfind 反向查找
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

### index 
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

### count 计数

```
In [59]: myStr
Out[59]: 'liuhe haha zhengdejuan'

In [60]: myStr.count('he')
Out[60]: 2
```
### replace 替换

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
### split 切割
> 默认切割 \t和空格

```
In [7]: myStr.split(' ')
Out[7]: ['liuhe', 'haha', 'zhengdejuan']

In [37]: test = 'asdfa \t \ndfad \t fa\t ss f'
In [38]: test.split()
Out[38]: ['asdfa', 'dfad', 'fa', 'ss', 'f']
```


### title每个单词首字母大写
```
In [8]: myStr.title()
Out[8]: 'Liuhe Haha Zhengdejuan'
```
 
### capitalize一个字符串第一个单词首字母大写
```
In [9]: myStr.capitalize()
Out[9]: 'Liuhe haha zhengdejuan'
```
### endswith

```
In [10]: fileName='xx.txt'
In [11]: fileName.endswith(".txt")
Out[11]: True
```
### upper()大写 lower()小写

```
In [17]: myStr.upper()
Out[17]: 'LIUHE HAHA ZHENGDEJUAN'
```
### center(偏移值) 居中显示 rjust（偏移值） 偏右显示
```
In [20]: myStr.center(30)
Out[20]: '    liuhe haha zhengdejuan  '

In [21]: myStr.rjust(30)
Out[21]: '        liuhe haha zhengdejuan'

In [22]: myStr.ljust(30)
Out[22]: 'liuhe haha zhengdejuan        '
```

### strip 去除字符串空格 lstrip() rstrip()

```
In [25]: rjust
Out[25]: '        liuhe haha zhengdejuan        '

In [26]: rjust.strip()
Out[26]: 'liuhe haha zhengdejuan'

In [29]: rjust.rstrip()
Out[29]: '    liuhe haha zhengdejuan'
```
### partition 拆成元组

```
# 列表，切分割值‘haha’没有了
In [33]: myStr.split('haha')
Out[33]: ['liuhe ', ' zhengdejuan']

# 元组，分割值‘haha’还在
In [34]: myStr.partition('haha')
Out[34]: ('liuhe ', 'haha', ' zhengdejuan')
```

### join 将指定字符加入已有字符串或者列表中,拼接成新的字符串

```
In [40]: result
Out[40]: ['asdfa', 'dfad', 'fa', 'ss', 'f']
In [42]: "".join(result)
Out[42]: 'asdfadfadfassf'
```

## 列表

> 可以同时存储多种类型数据


```
In [14]: params=[1,2.2,'liuhe',True] # 定义一个列表

In [15]: params
Out[15]: [1, 2.2, 'liuhe', True]
```
### 增加（C）

#### append 通过append可以向列表添加元素


```
In [17]: names
Out[17]: ['唐僧', '悟空']

In [18]: names.append('八戒')

In [19]: names
Out[19]: ['唐僧', '悟空', '八戒']
```

#### insert
> insert(index, object) 在指定位置index前插入元素object


```
In [19]: names
Out[19]: ['唐僧', '悟空', '八戒']

In [20]: names.insert(0,'如来')

In [21]: names
Out[21]: ['如来', '唐僧', '悟空', '八戒']
```
#### extend
>通过extend可以将另一个集合中的元素逐一添加到列表中


```
In [29]: l1=[1,2]

In [30]: l2=[3,4]

In [31]: l1+l2
Out[31]: [1, 2, 3, 4]

In [32]: l1.extend(l2)

In [33]: l1
Out[33]: [1, 2, 3, 4]

In [34]: l2
Out[34]: [3, 4]
```
### 删除(D)

* del：根据下标进行删除
* pop：删除最后一个元素
* remove：根据元素的值进行删除

```
In [33]: l1
Out[33]: [1, 2, 3, 4]
In [35]: l1.pop()
Out[35]: 4

In [36]: l1
Out[36]: [1, 2, 3]
```

```
In [15]: list
Out[15]: [1, 2, 3, 4]

In [16]: del list[2]

In [17]: list
Out[17]: [1, 2, 4]
```
remove 第一个匹配值
```
In [6]: list
Out[6]: [2, 3, 2, 4, 5, 4]

In [7]: list.remove(4)
In [8]: list
Out[8]: [2, 3, 2, 5, 4]
```

### 修改(U)

```
In [17]: list
Out[17]: [1, 2, 4]

In [18]: list[0]='haha'

In [19]: list
Out[19]: ['haha', 2, 4]
```


### 查找(R)

*  in（存在）,如果存在那么结果为true，否则为false
* not in（不存在），如果不存在那么结果为true，否则false

列表的切片：

```
In [12]: list
Out[12]: [2, 3, 2, 5, 4]

In [11]: list[2:4]
Out[11]: [2, 5]
```



