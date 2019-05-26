## Python enumerate() 函数:
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

Python 2.3. 以上版本可用，2.6 添加 start 参数。
语法
以下是 enumerate() 方法的语法:
```python
enumerate(sequence, [start=0])
```
参数
`sequence` -- 一个序列、迭代器或其他支持迭代对象。
`start` -- 下标起始位置。
返回值:
返回 `enumerate(枚举)` 对象。
> 实例
以下展示了使用 enumerate() 方法的实例：
```
>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']  #一个简单的列表
>>> list(enumerate(seasons))  #变成枚举对象
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

```
#### 用于**for**循环的对比
普通的 for 循环

```python
>>>i = 0
>>> seq = ['one', 'two', 'three']
>>> for element in seq:
...     print (i, seq[i])
...     i +=1
... 
0 one
1 two
2 three
```
使用enumberate:
```python
>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):  #返回给i,element的是一个索引加数据
...     print (i, element)
... 
0 one
1 two
2 three

```
### Python upper()方法
描述
Python upper() 方法将字符串中的小写字母转为大写字母。

语法
upper()方法语法：
```python
str.upper()
```
参数
NA。
返回值
返回小写字母转为大写字母的字符串。

实例
以下实例展示了 upper()函数的使用方法：
```python
#!/usr/bin/python

str = "this is string example....wow!!!";

print ("str.upper() : ", str.upper())
```
以上实例输出结果如下：
```python
str.upper() :  THIS IS STRING EXAMPLE....WOW!!!
```
