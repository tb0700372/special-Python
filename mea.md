# 练习

## `环境搭建`

* 自己动手搭建Python开发环境
* 运行一个简单的Python程序测试自己Python环境

## `数据类型`

* 数据类型转换

## `分支结构`

* 单一分支结构

```py
print("开始。。。")

if 100 > 50:
  print("选择性语句的执行")
  print("选择性语句的执行")
  print("选择性语句的执行")

print("结束。。。")
```

* 双向分支结构

```py
num = int(input("请输入一个成绩："))

if num >= 60:
  print("成绩及格！")
else:
  print("考试未通过！")
```

* 多分支结构

```py
num = int(input("请输入一个成绩："))

if num >= 90:
  print("成绩优秀！")
elif num >= 75:
  print("成绩良好！")
elif num >= 60:
  print("成绩及格！")
else:
  print("考试未通过！")
```

* 巢状分支结构

```py
num = int(input("请输入一个成绩："))

if num >= 75:
  if num >= 90:
      print("成绩优秀！")
  else:
      print("成绩良好！")
else:
  if num >= 60:
      print("成绩及格！")
  else:
      print("成绩不及格！")
```

## `循环结构`

* while循环

```py
# 循环输出1~10的值：
i=1
while i<=10:
    print(i)
    i+=1

# 循环输出10~1的值:
i=10
while i>=1:
    print(i,end=" ")
    i-=1

# 计算1~100的累加
i, sum = 1, 0
while i<=100:
    #print(i,end=" ")
    sum+=i #将每次循环的i累加到sum变量中
    i+=1
print("100的累加值：",sum)

# 死循环的使用
while True:
    k = input("请输入一个值：")
    print("内容：",k)
    if k=='q':
        break # 跳出循环
```

* for in 循环

```py
# 遍历字串
for i in "abcd":
    print(i)

# 遍历列表
for i in [10,20,30]:
    print(i)

# 遍历元组
for i in (10,20,30):
    print(i)

# 遍历集合
for i in {40,50,60}:
    print(i)

# 遍历字典
a = {'name':'lisi','age':20,'sex':'man'}
for i in a:
    print(i,":",a[i])

# 遍历嵌套数据结构
a=[("a","AAAA"),("b","BBB"),('c','CCCC')]
for v1,v2 in a:
    print(v1,"=>",v2)
```

* range\(\)的使用

```py
    # 循环输出0~9的值：
    for i in range(10):
        print(i,end=" ")
    print("")

    # 循环输出2~6值：
    for i in range(2,7):
        print(i,end=" ")
    print("")

    # 循环输出0~50的值，递增5
    for i in range(0,51,5):
        print(i,end="  ")
    print("")

    #输出10~1的值
    for i in range(10,0,-1):
        print(i,end=" ")
    print(" ")

    #使用range（）和len（）结合遍历输出容器类的数据
    a = ["aaa","bbb","ccc"]
    for i in range(len(a)):
        print(i,"=>",a[i])
```

* 循环嵌套输出九九乘法表

```py
# 循环输出1~9的值
for i in range(1,10):
    print(i,end=" ")

# 循环9行
for j in range(1,10):
    print("")

# 循环9行，输出1~9的值
for j in range(1,10):
    for i in range(1,10):
        print(i,end=" ")
    print("")

# 循环9行，输出1~9的值, 三角形
for j in range(1,10):
    for i in range(1,j+1):
        print(i,end=" ")
    print("")

# 输出九九乘法表
for j in range(1,10):
    for i in range(1,j+1):
        print("{}*{}={:<4}".format(i,j,i*j),end=" ")
    print("")


# 输出九九乘法表
for j in range(9,0,-1):
    for i in range(1,j+1):
        print("{}*{}={:<4}".format(i,j,i*j),end=" ")
    print("")

print("="*40)

# 使用while循环输出的九九乘法表
j=1
while j<=9:
    i=1
    while i<=j:
        print("{}*{}={:<4}".format(i,j,i*j),end=" ")
        i+=1
    print("")
    j+=1
```

* break、continue、else和pass的使用

```py
# 循环0~9的值
for i in range(10):
    if i==6:
        #break # 退出循环
        continue # 跳过本次循环，继续后面的循环执行
    print(i)

# 数据查找
a=[10,20,30,40]
m=300
for i in a:
    if m==i:
        print("存在")
        break
else:
    print("不存在！")
for i in a:
    pass
```

## `函数`

* 函数的定义方式:

```py
# 基本格式定义

#定义一个函数aa
def aa():
    print("1.aaaaaaa")
    print("2.aaaaaaa")
    print("3.aaaaaaa")
#函数的调用
aa()
aa()
aa()


# 定义带有参数的函数
def myadd(m1,m2):
    print(m1+m2)

myadd(10)


# 带有默认值得参数函数
def stu(name='zhangsan',age=20,sex='man'):
    print("姓名：{}；年龄：{}；性别：{}".format(name,age,sex))

stu()
stu('lisi')
stu('wangwu',30)
stu('zhaoliu',25,'women')


# 带关键字的函数
def stu(name='zhangsan',age=20,sex='man'):
    print("姓名：{}；年龄：{}；性别：{}".format(name,age,sex))
# 可以有效的防止参数传错
stu(name='zhaoliu',sex='women',age=25)


# 非关键字收集参数
def demo(*arg):
    #print(arg)
    sum=0
    for i in arg:
        sum+=i
    print("累加值：",sum) 
demo(10,20,30,40)


#带关键字收集参数
def demo(m,**arg):
    print(m)
    print(arg)
demo(10,name="zhangsan",age=20)


# 定义一个计算指定数值累加的函数
def sum(m):
    '''
    这是一个计算指定数值的累加函数
    参数一个，int类型，表示要累加的数值
    返回值是一个累加结果 int类型
    '''
    total=0
    for i in range(0,m+1):
        total+=i
    #print(total) #直接输出结果
    return total #返回结果
a = sum(10)
print("10的累加：",a)
print("50的累加：",sum(50))
print("100的累加：",sum(100))
```

* 函数的局部变量和全局变量

```py
#函数外定义的称全局变量
name="zhangsan"
def fun():
    global name
    print("函数内输出全局：",name)
    name = "lisi"
    age=30 #局部变量
    age += 2
    print("函数内容输出局部：",age)

fun()
fun()
print("函数外输出全局变量：",name)
#print("函数外容输出局部：",age)
```

* 匿名函数

```py
# 定义匿名函数
sum = lambda v1,v2: v1+v2
print(sum(10,20))
print(sum(100,200))
```

## `数据类型操作`

* 数据类型的操作之Number数值类型

```py
# -------------------- 数学函数 --------------------
# 内置对象
print(abs(-10))    #10  绝对值
print(round(4.5678,2))  #4.57 四舍五入，保留小数两位
# 下面参数可以是字串，列表、元组、集合和字典(键值)
print(max([20,10,30]))    #30  最大值
print(min([20,10,30]))    #10  最小值
#需要引入math
import math
print(math.fabs(-10))   #10.0 绝对值
print(math.ceil(4.01))  #5 进一取整
print(math.floor(4.99))  #4 舍去取整


# -------------------- 随机数函数 --------------------
# 需要引入random模块
import random
print(random.random())    #随机一个0~1的值
# 参数可以为字串，列表或元组
print(random.choice(["a","b","c"])) #b  从序列中随机一个值
print(random.randrange(10))   #从0~9中随机一个数值
print(random.randrange(5,10))   #从5~9中随机一个数值
print(random.randrange(0,10,2))   #从0~9中随机一个偶数值
a=[10,20,30,40]
random.shuffle(a)    #随机将序列中的元素打乱
print(a)

# -------------------- 三角函数 --------------------
#详见手册：
#需要引入math模块
#math.sin(90)
#math.cos(0)


# -------------------- 数学常量 -------------------- 
#需要引入math模块
print(math.pi)    #圆周率
print(math.e)    #自然常数
```

* 数据类型的操作之String字符串

```py
# -------------------- Python转义字符 --------------------
# \\   \'单引号  \"双引号 \n 换行  \t tab键 
print("aaa\\bbb\"ccc\nddd\teeee")

# -------------------- 字符串的运算符 --------------------
print("aa"+"bb") #字串连接
print("abc"*2)	 #重复字串
s="zhangsan"
print(s[1])	#通过索引获取字符串
print(s[0:5]) #截取字串的一部分
print("san" in s) #判读是否包含指定字串
print("san" not in s) #判断是否不包含指定字串
print(r"aa\nbb\\cc")	#输出原始字串，让转义无效

# -------------------- %格式化字串 -------------------- 
print("我叫%s，今年%d岁"%('小明',20)) #字串和十进制数值
print("110的八进制：0o%o；十六进制：0x%x"%(110,110))
print("12.45678保留小数后两位：%0.2f"%(12.45678))


# -------------------- 字串的内建函数 --------------------
print(len("zhangsan"),max("abc"),min("abc")) #长度，最大字符，最小字符
print("ZhangSan".lower(),"ZhangSan".upper()) # 小写，大写转换
print("zhangsan字串中出现an的次数：","zhangsan".count("an"))
print("10:20:30".replace(":","@")) #10@20@30　字串替换
print("10:20:30".split(":")) #字串拆分，变成列表类型
print("zhangsan".find("an")) #2 字串查找，返回首次出现索引位置（找不到返回-1）
print("zhangsan".index("an")) #2 字串查找，返回首次出现索引位置(找不到报异常)
print("zhangsan".rfind("an")) #6 字串查找，从后面(右侧)开始查找首次出现索引位置
print(" aa  ".strip()) #执行lstrip()和rstrip() 去除两次多余空格或指定字符
# 其他转码后面再讲。
```

* 数据类型的操作之List列表

```py
# -------------------- 列表的基础操作 --------------------

# 定义
list0 = [] # 创建一个空列表 或者  变量 = list()
list1 = ['Google','Python',1997,2000];
list2 = [1,2,3,4,5,6,7];

#输出
print ("list1[0]: ",list1[0])  # Google
print ("list2[1:5]: ",list2[1:5]) # [2, 3, 4, 5]

#更新其中的值
print ("第三个元素为 : ",list1[2])    # 2000
list1[2] = 2001
print ("更新后的第三个元素为 : ",list1[2])  # 2001

#删除其中一个元素
del list1[2]
print ("删除第三个元素 : ",list1)  #  ['Google', 'Python', 2000]

# -------------------- 列表的遍历 --------------------
a=[10,20,30,40,50]
#使用for...in遍历
for i in a:
	print(i)

#使用while遍历
i=0
while i<len(a):
	print(a[i])
	i+=1

#遍历等长二级列表
b = [[10,20],[30,40],[50,60]]
for v1,v2 in b:
	print(v1,v2)

#遍历不等长二级列表
b = [[10,20],[30,40,50,60],[70,80,90]]
for v in b:
	for i in v:
		print(i,end=" ")
	print()


# -------------------- 列表的操作符 --------------------
a=[1,2,3]
b=[4,5,6,7]
print(len(a)) #3 列表长度
print(a+b)  #[1,2,3,4,5,6,7] 组合列表
print(a*2)  #重复列表
print(6 in b) #判断一个值是否在一个列表中
#获取
print(b[2])  #6
print(b[-2])  #6
print(b[1:]) #[5,6,7]
print(b[1:3]) #[5,6]


# -------------------- 列表的函数和方法 --------------------
# 函数有：len--长度  max--最大  min--最小  list()--转换
a=["zhangsan","lisi"]
a.append('xiaoliu') #在列表尾部添加新的一个元素
a.extend(["wangwu","zhaoliu"]) #在列表尾部添加多个值
a.insert(3,'lisi') #插入元素（在索引位置3）

print(a) #['zhangsan', 'lisi', 'xiaoliu', 'lisi', 'wangwu', 'zhaoliu']

print(a.count('lisi'))  #获取lisi字串在列表中出现的次数
print(a.index('lisi'))  #查询a中首次出现list的位置
print(a.pop(2)) #弹出列表中索引位置为2的元素 

print(a) # ['zhangsan', 'lisi', 'lisi', 'wangwu', 'zhaoliu']

a.remove("lisi")  #删除指定元素一个
a.reverse()  #反向列表中的元素
print(a) #['zhaoliu', 'wangwu', 'lisi', 'zhangsan']

a.sort() #排序 (升序)
print(a) # ['lisi', 'wangwu', 'zhangsan', 'zhaoliu']

b=a #为a起个别名b
c=a.copy() #复制一个独立的列表
print(id(a),id(b),id(c)) #41181064 41181064 41147976

a.clear() # 清空列表
print(a) #[]
```

* 数据类型的操作之Tuple元组

```py
# 元组是不可修改的元素列表
 
# -------------------- 元组的基础操作 --------------------
# 定义元组的方式：
tup0 = ()  #定义一个空元组 或者 变量 = tuple()
tup1 = ('Google', 'Python', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

# 输出元组：
print ("tup1[0]: ", tup1[0])       # tup1[0]:  Google
print ("tup2[1:5]: ", tup2[1:5])   # tup2[1:5]:  (2, 3, 4, 5)

# 注意下面这种定义不加逗号，类型为整型
tup4 = (50)
print(type(tup4))  # <class 'int'>

# 正确定义方式加上逗号，类型为元组
tup5 = (50,)
print(type(tup5))  # <class 'tuple'>

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup0;

# -------------------- 元组的遍历（和列表一样）--------------------
a=(10,20,30,40,50)
#使用for...in遍历
for i in a:
	print(i)

#使用while遍历
i=0
while i<len(a):
	print(a[i])
	i+=1

#遍历等长二级元组
b = ((10,20),(30,40),(50,60))
for v1,v2 in b:
	print(v1,v2)

#遍历不等长二级元组
b = ((10,20),(30,40,50,60),(70,80,90))
for v in b:
	for i in v:
		print(i,end=" ")
	print()


# -------------------- 元组的操作符 --------------------
a=(1,2,3)
b=(4,5,6,7)
print(len(a)) #3 元组长度
print(a+b)  #(1,2,3,4,5,6,7) 组合元组
print(a*2)  #重复元组
print(6 in b) #判断一个值是否在一个元组中
#获取
print(b[2])  #6
print(b[-2]) #6
print(b[1:]) #(5,6,7)
print(b[1:3]) #(5,6)


# -------------------- 元组的函数 --------------------
# 函数有：len--长度  max--最大  min--最小  tuple()--转换

```

* 数据类型的操作之Set集合

```py
#集合是一个无序不重复元素的序列

# -------------------- 集合的基础操作 --------------------
# 定义集合的方式：
# 集合的定义
set1 = set()  #定义一个空的集合
set2 = {1,2,3}

# 增加一个元素
set1.add(5)  

#增加多个：参数可以是列表或元组
set1.update([5,6,7,8]) 

#删除某个值（参数为元素值，没有会报错）
set2.remove(1)
set2.discard(50) # 删除不存在元素的值不会报错

#查：无法通过下标索引
#改：不可变类型无法修改元素

# 清空集合
set2.clear()

a={10,20,30}
b={20,50}
print(a - b)     # a和b的差集 

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素

# -------------------- 集合的遍历 --------------------
a={10,20,30,40,50}
#使用for...in遍历
for i in a:
	print(i)

#遍历等长二级集合
b = {(10,20),(30,40),(50,60)}
for v1,v2 in b:
	print(v1,v2)

# -------------------- 集合的操作符 --------------------
a={1,2,3}
print(len(a)) #3 集合长度
print(6 in a) #判断一个值是否在一个集合中


# -------------------- 集合的函数和方法 --------------------
# 函数有：len--长度  max--最大  min--最小  tuple()--转换

# 集合的方法
# add -- 增加集合元素
# update--更新已有集合
# remove--移除指定集合元素
# discard--移除元素
# clear--清空集合元素
# copy--浅拷贝
# difference -- 求差集
# union--并集，创建新的对象
# difference_update---删除当前set中的所有包含在 new set 里的元素
# intersection--取交集,建立新的set集合
# intersection_update--取交集,更新原来的set集合
# isdisjoint--判断没有交集，返回True,否则,返回False
# issubset--判断是否是子集
# issuperset--判断是否是父集
# pop--移除集合元素
# symmetric_difference--去两个集合的差集，建立新的set集合对象
# symmetric_difference_update--去两个集合的差集，更新原来的集合对象
```

* 数据类型的操作之Dictionary字典

```py
#字典是另一种可变容器模型，且可存储任意类型对象

# -------------------- 字典的基础操作 --------------------
# 定义字典的方式：
# 字典的定义
d0 = {} #或dict()  #定义一个空的字典
d1 = {'Name': 'Python', 'Age': 17, 'Class': 'First'}

# 输出子典中的信息
print ("d1['Name']: ", d1['Name']) #Python
print ("d1['Age']: ", d1['Age'])   #17

# 输出错误信息：KeyError: 'Alice'
#print ("d1['Alice']: ", d1['Alice'])

# 修改和添加内容
d1['Age'] = 18;              # key存在则更新 Age
d1['School'] = "云课堂"      # key不存在则添加信息

# 删除信息
del d1['Name'] # 删除键 'Name'一个元素值
d1.clear()     # 清空字典
del d1         # 删除字典

# -------------------- 字典的遍历 --------------------
d1 = {'Name': 'Python', 'Age': 17, 'Class': 'First'}
#使用for...in遍历(默认遍历键)
for k in d1:
	print(k,"=>",d1[k])

#遍历键和值（使用items()）
for k,v in d1.items():
	print(k,"=>",v)

# -------------------- 字典内涵/字典推导式 --------------------
d = {"name":"zhangsan","age":22,"sex":"man"}

# 普通字典内涵：遍历d，重新创建一个a
a={key:value for key,value in d.items()}
print(a) 

# 有条件的字典的内涵
a={key:value for key,value in d.items() if key=="name"}
print(a)

# -------------------- 字典的函数和方法 --------------------
# 函数有：len--长度  max--最大  min--最小  str()--转换字串形态
# 
# 字典的方法
d = {'a': 'AAA', 'b': 'BBB', 'c': 'CCC'}
d2 = d.copy()  #复制一个字典给d2
print(d2) #{'a': 'AAA', 'b': 'BBB', 'c': 'CCC'}

d2.clear() #清空字典
print(d2)  # {}

c = dict.fromkeys(('a','b','c'),100)  #构建新字典
print(c) #{'a': 100, 'b': 100, 'c': 100}

print(d.get('b'))  #获取指定键的值
print(d.get('d'))  #获取指定键的值（没有返回：None）

print('c' in d)  #True  判断指定键是否存在字典中

# 返回字典中的键值元组
print(d.items()) # dict_items([('a', 'AAA'), ('b', 'BBB'), ('c', 'CCC')])
print(d.keys())  # dict_keys(['a', 'b', 'c'])	
print(d.values())# dict_values(['AAA', 'BBB', 'CCC'])

d.setdefault('d','DDD') #键不存在时则添加，第二参数指定值，没有默认None 
print(d) #{'a': 'AAA', 'b': 'BBB', 'c': 'CCC', 'd': 'DDD'}

#批量修改，没有对应key的则做添加操作
d.update({'b':'BB2', 'c':'CC2','e':'EE2'})
print(d) #{'a': 'AAA', 'b': 'BB2', 'c': 'CC2', 'd': 'DDD', 'e': 'EE2'}

print(d.pop('e')) #EE2 删除指定参数键对应的值，并返回。
print(d)  #{'a': 'AAA', 'b': 'BB2', 'c': 'CC2', 'd': 'DDD'}

print(d.popitem()) #('d','DDD') 随机删除并返回字典中一个键值对（一般删除末尾）
print(d)  #{'a': 'AAA', 'b': 'BB2', 'c': 'CC2'}
```
