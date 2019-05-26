## [python的各种推导式（列表推导式、字典推导式、集合推导式）](https://www.jianshu.com/p/624a924dd710)

推导式comprehensions（又称解析式），是Python的一种独有特性。推导式是可以从一个数据序列构建另一个新的数据序列的结构体。 共有三种推导，在Python2和3中都有支持：

- 列表(list)推导式
- 字典(dict)推导式
- 集合(set)推导式

 

### 一、列表推导式

**1、使用[]生成list**

**基本格式**

```python
variable = [out_exp_res for out_exp in input_list if out_exp == 2]
  out_exp_res:　　列表生成元素表达式，可以是有返回值的函数。
  for out_exp in input_list：　　迭代input_list将out_exp传入out_exp_res表达式中。
  if out_exp == 2：　　根据条件过滤哪些值可以。
```

 

例一：直接筛选

```python
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
#multiples是一个接收列表
#接收的值是一个的i
#使用for循环将传入的range(30)中的值传递给列表
#使用if语句来判断传递哪些值

# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```

 

例二：函数返回值

```python
def squared(x):  #定义一个函数
    return x*x   #返回的是传入值的平方  
#将for循环的返回值传到函数中
multiples = [squared(i) for i in range(30) if i % 3 is 0]
print (multiples)

#  Output: [0, 9, 36, 81, 144, 225, 324, 441, 576, 729]
```

 

**2、使用()生成generator**

将俩表推导式的[]改成()即可得到生成器。

```python
multiples = (i for i in range(30) if i % 3 is 0)
print(multiples)
print(type(multiples))
#  Output: <generator object <genexpr> at 0x0000022D6AC7BB10>
<class 'generator'>
```

### 二、字典推导式

字典推导和列表推导的使用方法是类似的，只不中括号该改成大括号。直接举例说明：

例子一：大小写key合并

```python
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    if k.lower() in ['a','b']
}
print mcase_frequency
#  Output: {'a': 17, 'b': 34}
```


例子二：快速更换key和value

```python
mcase = {'a': 10, 'b': 34}
mcase_frequency = {v: k for k, v in mcase.items()}
print mcase_frequency
#  Output: {10: 'a', 34: 'b'}
```

 

 

### 三、集合推导式

它们跟列表推导式也是类似的。 唯一的区别在于它使用大括号{}。

**例一：**

```python
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: set([1, 4])
```
