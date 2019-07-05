描述
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

### 语法
join()方法语法：
```python
str.join(sequence)
```
### sequence -- 要连接的元素序列。
### 返回值
返回通过指定字符连接序列中元素后生成的新字符串。
### 实例
以下实例展示了join()的使用方法：就是在元素的中间位置都插入一个str1
```python
str1="a"

b=("b","c","d")

str1.join(b)
Out[6]: 'bacad'
```
常用的例子将列表转换成字符串
```python
a=["a","b","c"]

b="".join(a)

b
Out[9]: 'abc'

```
